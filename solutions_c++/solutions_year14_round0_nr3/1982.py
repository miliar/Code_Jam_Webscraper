#include <algorithm>
#include <iostream>
#include <string.h>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <map>

#define INF 2147483647
#define LLINF 2000000000000000000
#define ll long long
#define PI 3.1415926535897932384626433832795
#define all(a) a.begin(), a.end()
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define y1 yonigga1
#define y0 yonigga2
#define left lololol
#define right ololololol
#define m0(a) memset(a,0,sizeof(a))
using namespace std;

typedef long double ld;

const int step[8][2]={ {1,0},{-1,0},{0,1},{0,-1}, {1,1},{-1,-1},{1,-1},{-1,1} };

int T,r,c,m,resx,resy;
int ma[11][11], temp[11][11], cnt, a[40];
vector<int> p;
pair<int, int> ind[300];
bool fnd;

bool ok(int x, int y){
    return (x>=1&&x<=r&&y>=1&&y<=c);
}
void dfs(int x, int y){
    ++cnt;
    temp[x][y]=2;
    
    for(int it=0;it<8;++it){
        int nx=x+step[it][0],ny=y+step[it][1];
        if (!ok(nx,ny))continue;
        if (temp[nx][ny]==1) return;
    }

    for(int it=0;it<8;++it){
        int nx=x+step[it][0],ny=y+step[it][1];
        if (!ok(nx,ny))continue;
        if (temp[nx][ny]>=1)continue;
        dfs(nx,ny);
    }
}

void trans(){
    memset(temp, 0, sizeof(temp));
    for(int i=1;i<=r*c;++i){
        int x=ind[i].F, y=ind[i].S;
        temp[x][y]=a[i];
        ma[x][y]=a[i];
    }
}

void print(){
    fnd=1;
    for(int i=1;i<=r;++i){
        for(int j=1;j<=c;++j){
            if (i==resx&&j==resy){
                cout<<'c';
                continue;
            }
            if (ma[i][j]==0)cout<<'.';
            else cout<<'*';
        }
        cout<<'\n';
    }
}

void go(){
    cnt=0;
    trans();
    for(int i=1;i<=r;++i)
        for(int j=1;j<=c;++j){
            if (temp[i][j]!=0)continue;
            cnt=0;
            trans();
            dfs(i,j);
            if (cnt==r*c-m){
                resx=i;
                resy=j;
                print();
                return;
            }
        }
}


bool next_combination (vector<int> & a, int n) {
	int k = (int)a.size();
	for (int i=k-1; i>=0; --i)
		if (a[i] < n-k+i+1) {
			++a[i];
			for (int j=i+1; j<k; ++j)
				a[j] = a[j-1]+1;
			return true;
		}
	return false;
}

void solve(){
    cin>>r>>c>>m;
    int cur=0;
    for(int i=1;i<=r;++i)
        for(int j=1;j<=c;++j){
            ++cur;
            ind[cur]=mp(i,j);
        }
    p.clear();
    memset(a, 0, sizeof(a));
    for(int i=1;i<=m;++i)
        p.pb(i);
    fnd=0;
    for(;;){
        memset(a, 0, sizeof(a));
        for(int i=0;i<m;++i)
            a[p[i]]=1;
        go();
        if (fnd)return;
        if(!next_combination(p, r*c))break;
    }
    if (!fnd)cout<<"Impossible"<<'\n';
}


int main(){
    freopen("C-small-attempt2.in.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin>>T;
    for(int it=1;it<=T;++it){
        cout << "Case #"<<it<<": "<<'\n';
        solve();
    }
    
    
    
    return 0;
}
