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

const int M=1025;
int dp[M][M][12][3];
vi res[M][M][12][3];
int solve(int a,int b,int c,int k,int n){
    assert(a+b+c==(1<<n));
    
    int &ret=dp[a][b][n-1][k];
    if(ret+1)return ret;
    ret=0;
    vi &v=res[a][b][n-1][k];v.clear();
    if(n==1){
        rep(i,0,b)v.pb(0);
        rep(i,0,a)v.pb(1);
        rep(i,0,c)v.pb(2);
        //assert(SZ(v)==(1<<n));
        if(k==0)return ret=(a&&c);
        if(k==1)return ret=(a&&b);
        return ret=(b&&c);
    }
    int m=1<<n-1;
    rep(i,0,a+1)
        rep(j,0,b+1){
            if(i+j>m)break;
            int l=m-i-j;
            if(l>c)continue;
            if(i==m||j==m||l==m||a-i==m||b-j==m||c-l==m)continue;
            if(solve(i,j,l,k,n-1)&&solve(a-i,b-j,c-l,(k+2)%3,n-1)){
                ret=1;
                vi v1=res[i][j][n-2][k],v2=res[a-i][b-j][n-2][(k+2)%3];
                //assert(SZ(v1)==SZ(v2));
                FOREACH(it,v2)v1.pb(*it);
                if(v.empty()||v>v1){
                    v=v1;
                }
            }
            if(solve(i,j,l,(k+2)%3,n-1)&&solve(a-i,b-j,c-l,k,n-1)){
                ret=1;
                vi v1=res[i][j][n-2][(k+2)%3],v2=res[a-i][b-j][n-2][k];
                //assert(SZ(v1)==SZ(v2));
                FOREACH(it,v2)v1.pb(*it);
                if(v.empty()||v>v1){
                    v=v1;
                }
            }
        }
    //if(ret)assert(SZ(v)==(1<<n));
    return ret;
}
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int j,k,i,T,ca=0,n,m;
    scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",++ca);
        int a,b,c;
        scanf("%d%d%d%d",&n,&a,&b,&c);
        memset(dp,-1,sizeof(dp));
        rep(i,0,3)solve(a,b,c,i,n);
        vi ans;
        rep(i,0,3)if(dp[a][b][n-1][i]==1){
            if(ans.empty()||ans>res[a][b][n-1][i])ans=res[a][b][n-1][i];
        }
        if(ans.empty())puts("IMPOSSIBLE");
        else{
            //DBG((1<<n))
            //DBG(SZ(ans))
            rep(i,0,(1<<n)){
                if(ans[i]==0)printf("%c",'P');
                else if(ans[i]==1)printf("%c",'R');
                else printf("%c",'S');
            }
            puts("");
        }

    }
    //cerr<<1.*clock()/CLOCKS_PER_SEC<<"s\n";
    return 0;
}