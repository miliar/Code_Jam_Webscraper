#include<cstdio>
#include<iostream>
#include<cassert>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<list>
#include<queue>
#include<set>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); --x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) __typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define MP make_pair
#define PB push_back
#define ST first
#define ND second

const int MAXN = 110;
const int MHIGH = 101;

int a[MAXN][MAXN];

int n,m,t;

void readData(){
    scanf("%d%d",&n,&m);
    REP(i,n){
        REP(j,m){
            scanf("%d",a[i] + j);
        }
    }
}

bool check(){
    int k[MAXN];
    int w[MAXN];
    REP(i,MAXN){
        k[i] = 0;
        w[i] = 0;
    }
    REP(i,n){
        REP(j,m){
            w[i] = max(w[i], a[i][j]);
            k[j] = max(k[j], a[i][j]);
        }
    }
    REP(i,n){
        REP(j,m){
           if (a[i][j] < min(w[i], k[j])) return false; 
        }
    }
    return true;
}

int main(){
    scanf("%d",&t);
    REP(i,t){
        readData();
        if (check()){
            printf("Case #%d: YES\n", i + 1);
        }
        else {
            printf("Case #%d: NO\n", i + 1);
        }
    }
}

