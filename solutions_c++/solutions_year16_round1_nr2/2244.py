#pragma comment(linker, "/STACK:102400000,102400000")
#include <iostream>
#include <stdio.h>
#include <queue>
#include <algorithm>
#include <map>
#include <string.h>
#include <assert.h>
#include <set>
#include <cmath>
using namespace std;
#define vi vector<int>
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define all(x) x.begin(),x.end()
#define SZ(x) (int)(x.size())
#define rep(i,a,b) for(int i=a;i<b;i++)
#define per(i,a,b) for(int i=b-1;i>=a;i--)
#define inf 1000000007
#define mod 1000000007
#define x first
#define y second
#define pi acos(-1.0)
#define DBG(x) cerr<<(#x)<<"="<<x<<"\n";
//#define dprintf(...) 
#define hash _hash
//#define dprintf(...) fprintf(outFile,__VA_ARGS__)
 
#define FOREACH(it,x) for(__typeof(x.begin()) it=x.begin();it!=x.end();it++)
#define ull unsigned long long
#define ll long long
#define N 2000010
 
template <class T,class U>inline void Max(T &a,U b){if(a<b)a=b;}
template <class T,class U>inline void Min(T &a,U b){if(a>b)a=b;}
 
//FILE* outFile;
 
inline void add(int &a,int b){a+=b;while(a>=mod)a-=mod;}
 
int pow(int a,int b){
    int ans=1;
    while(b){
        if(b&1)ans=ans*(ll)a%mod;
        a=(ll)a*a%mod;b>>=1;
    }
    return ans;
}


int sz,a[105][55],vis[105];
int d[105],dp[105],n,m,b[55];
vi g[105];
bool cal(int x,int y){
    rep(j,0,sz){
        int i=b[j];
        if(a[x][j]!=a[i][y])return 0;
    }
    return 1;
}
bool check(){
    int cnt=0;
    rep(i,0,n){
        bool ok=0;
        rep(j,0,m)if(!vis[j]){
            if(cal(j,i)){ok=1;break;}
        }
        if(!ok)cnt++;
    }
    return cnt<=1;
}
bool dfs(int x,int y=1){
    if(y==n)return 1;
    //cerr<<x<<" "<<y<<"\n";
    FOREACH(it,g[x]){
        int j=*it;
        if(vis[j]||dp[j]!=dp[x]+1)continue;
        vis[j]=1;b[sz++]=j;
        if(check()&&dfs(j,y+1))return 1;
        sz--;vis[j]=0;
    }
    return 0;
}
bool check(int x){
    rep(i,0,m)if(!vis[i]){
        if(cal(i,x))return 1;
    }
    return 0;
}

int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int T,ca=0,i,j,k;
    scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",++ca);
        scanf("%d",&n);
        memset(vis,0,sizeof(vis));
        m=2*n-1;
        rep(i,0,m){
            rep(j,0,n)scanf("%d",&a[i][j]);
            g[i].clear();
            d[i]=0;
        }
        rep(i,0,m)
            rep(j,0,m)if(i!=j){
                bool ok=1;
                rep(k,0,n){
                    if(a[i][k]>=a[j][k]){ok=0;break;}
                }
                if(ok)g[i].pb(j),d[j]++;
            }
        queue<int>q;
        rep(i,0,m)if(d[i]==0)q.push(i),dp[i]=1;
        while(!q.empty()){
            int u=q.front();q.pop();
            FOREACH(it,g[u]){
                j=*it;
                d[j]--;
                if(d[j]==0){
                    q.push(j);
                    dp[j]=dp[u]+1;
                }
            }
        }
        vi ans;
        int ok=0;
        rep(i,0,m)if(dp[i]==1){
            vis[i]=1;sz=0;b[sz++]=i;
            if(dfs(i,1)){
                rep(j,0,n)if(!check(j)){
                    rep(k,0,n)ans.pb(a[b[k]][j]);
                    break;
                }
                ok=1;
                break;
            }
            vis[i]=0;
        }
        //DBG(ok)
        assert(ok);
        rep(i,0,n)printf("%d ",ans[i]);puts("");
    }
    return 0;
}