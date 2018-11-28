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

vi g[1005];
int v[1005],dp[1005],a[1005],d[1005],s[1005],top;
void dfs(int u){
    dp[u]=1;
    FOREACH(it,g[u]){
        int j=*it;
        if(!v[j]){
            v[j]=1;dfs(j);
            dp[u]=max(dp[u],dp[j]+1);
        }
    }
}

int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int T,ca=0,i,j,k,n;
    scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",++ca);
        scanf("%d",&n);
        rep(i,0,n)g[i].clear(),d[i]=0;
        rep(i,0,n){
            scanf("%d",&a[i]);a[i]--;
            g[a[i]].pb(i);
            d[a[i]]++;
        }
        memset(v,0,sizeof(v));
        int w=0;
        rep(i,0,n)if(!v[i]){
            j=a[i];
            if(a[j]==i){
                v[i]=1;v[j]=1;
                dfs(i);
                w+=dp[i];
                dfs(j);
                w+=dp[j];
            }
        }
        int ans=0;
        
        rep(i,0,n)if(!v[i]){
            //DBG(i)
            int x=i,y=0;top=0;
            do{
                v[x]=1;s[top++]=x;
                x=a[x];
            }while(!v[x]);
            rep(j,0,top)if(s[j]==x){
                y=top-j;break;
            }
            Max(ans,y);
            //cerr<<y<<" "<<x<<"\n";
        }//*/
        Max(ans,w);
        printf("%d\n",ans);
    }
    return 0;
}