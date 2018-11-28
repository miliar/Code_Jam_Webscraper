#pragma comment(linker, "/STACK:102400000,102400000")
#include <bits/stdc++.h>
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
#define N 100010
 
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

double p[202],dp[202][202],q[202];
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int j,k,i,T,ca=0,n,m,K;
    scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",++ca);
        scanf("%d%d",&n,&K);
        rep(i,0,n)scanf("%lf",&p[i]);
        sort(p,p+n);
        int x=K/2,sz=0;
        double ans=0;
        rep(r,1,1<<n){
            sz=0;
        rep(l,0,n)if(r>>l&1)q[sz++]=p[l];
        if(sz!=K)continue;
        memset(dp,0,sizeof(dp));
        dp[0][0+x]=1;
        rep(i,0,K){
            rep(j,-x,x+1){
                if(j<x)dp[i+1][j+1+x]+=dp[i][j+x]*q[i];
                if(j>-x)dp[i+1][j-1+x]+=dp[i][j+x]*(1-q[i]);
            }
        }
        Max(ans,dp[K][x]);
        }
        printf("%lf\n",ans);
    }
    //cerr<<1.*clock()/CLOCKS_PER_SEC<<"s\n";
    return 0;
}