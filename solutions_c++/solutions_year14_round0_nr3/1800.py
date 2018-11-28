//                                                  به نام خداوند بخشنده ی مهربان
#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <fstream>
#include <complex>
#include <vector>
#include <string>
#include <cstdio>
#include <queue>
#include <deque>
#include <cmath>
#include <map>
#include <set>

# define xx first
# define yy second
# define pb push_back
# define pp pop_back
# define eps 1e-9
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vint;
int n,m,M,ted;
bool flag[10][10];
int matx[]={-1,-1,-1,0,1,1,1,0};
int maty[]={-1,0,1,1,1,0,-1,-1};
void dfs(int x,int y,int Mines){
    ted++;
    flag[x][y]=true;
    vector<pii> v;bool mark=true;
    for(int i=0 ; i<8 ; i++){
        int tmpx=x+matx[i],tmpy=y+maty[i];
        if(tmpx>0 && tmpx<n+1 && tmpy<m+1 && tmpy>0){
            if(((Mines)>>(((tmpx-1)*m+tmpy)-1)) & 1){
                mark=false;
                break;
            }
            else
                v.pb(pii(tmpx,tmpy));
        }
    }
    if(!mark)
        return ;
    for(int i=0 ; i<(int)v.size() ; i++)if(!flag[v[i].xx][v[i].yy])
        dfs(v[i].xx,v[i].yy,Mines);
}
bool check(int Mines){
    bool mark=false;
    int x,y;
    for(x=1 ; x<=n ; x++){
        for(y=1 ; y<=m ; y++){
            if(!(((Mines)>>(((x-1)*m+y)-1)) & 1)){
                memset(flag,false,sizeof flag);
                ted=0;dfs(x,y,Mines);
                if(ted==(n*m-(__builtin_popcount(Mines)))){
                    mark=true;
                    break;
                }
            }
        }
        if(mark)
            break;
    }
    if(mark){
        for(int i=1 ; i<=n ; i++){
            for(int j=1 ; j<=m ; j++){
                if(i==x && j==y)
                    cout<<'c';
                else if((Mines)>>(((i-1)*m+j)-1) & 1)
                    cout<<'*';
                else
                    cout<<'.';
            }
            cout<<'\n';
        }
    }
    return mark;
}
int main(){
    ios_base::sync_with_stdio(false);
    freopen("C-small-attempt0.in","r",stdin);
    freopen("ans.out","w",stdout);
    int T;cin>>T;
    for(int t=1 ; t<=T ; t++){
        cin>>n>>m>>M;
        cout<<"Case #"<<t<<":\n";
        bool mark=false;
        for(int i=0 ; i<(1<<(n*m)) ; i++){
            if(__builtin_popcount(i)==M){
                if(check(i)){
                    mark=true;
                    break;
                }
            }
        }
        if(!mark)
            cout<<"Impossible\n";
    }
    return 0;
}
