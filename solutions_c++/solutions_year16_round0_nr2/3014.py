#pragma comment(linker, "/STACK:102400000,102400000")
#include <iostream>
#include <stdio.h>
#include <queue>
#include <algorithm>
#include <map>
#include <string.h>
#include <assert.h>
#include <set>
using namespace std;
#define vi vector<int>
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define all(x) x.begin(),x.end()
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
#define N 1100010

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

char s[110];
int dp[110][2],a[110];
int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int T,ca=0;
    scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",++ca);
        scanf("%s",s);
        int n=strlen(s);
        rep(i,0,n)a[i]=s[i]=='+'?0:1;
        memset(dp,63,sizeof(dp));
        dp[0][0]=dp[0][1]=0;
        rep(i,0,n){
            int k=a[i];
            dp[i+1][k]=min(dp[i][k],dp[i][k^1]+1);
            dp[i+1][k^1]=min(dp[i][k^1]+2,dp[i][k]+1);
        }
        printf("%d\n",dp[n][0]);
    }
    return 0;
}