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

int v[35],now=0,a[50],sz=0,n,m,sum;
map<ll,int>g;
void dfs(int x,int K){
    if(sum==m)return;
    if(x>0){
        now++;
        a[sz++]=n-K;
        rep(i,0,sz)v[a[i]]=v[K+a[i]]=now;
        sum++;sz--;
        ll w=0;
        per(k,0,n+1)if(v[k]==now)printf("1"),w=w*2+1;else printf("0"),w=w*2;
        if(g.count(w))DBG("??????")
        g[w]=1;
        printf(" ");
        rep(k,2,11){
            ll s=1;
            rep(i,0,K)s=s*k;
            printf("%lld ",s+1);
        }
        puts(" ");
        if(sum==m)return ;
    }
    
    rep(i,x+K+1,n){
        if(i+K>=n-K)break;
        a[sz++]=i;
        //cerr<<i<<" "; 
        dfs(i,K);
        sz--;
    }
}
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int T,ca=0;
    scanf("%d",&T);
    while(T--){
        printf("Case #%d:\n",++ca);
        scanf("%d%d",&n,&m);n--;
        int K=(n+1)/3+1;sum=0;

        rep(i,1,K){
            int y=min(i-1,n-2*i-1);
            if(y<0)break;            
            rep(j,0,1<<y){
                sum++;now++;
                rep(k,0,y)if(j>>k&1)v[k+1]=now,v[i+k+1]=now;
                v[0]=v[n-i]=v[n]=v[i]=now;
                ll w=0;
                per(k,0,n+1)if(v[k]==now)printf("1"),w=w*2+1;else printf("0"),w=w*2;
                if(g.count(w))DBG("??????")
                g[w]=1;
                printf(" ");
                rep(k,2,11){
                    ll s=1;
                    rep(l,0,i)s=s*k;
                    printf("%lld ",1+s);
                }
                puts("");
                //DBG(i)
                if(sum==m)break;
            }
            if(sum==m)break;
        }
        //DBG(".......................")
        //DBG(sum)
        if(sum<m){
            rep(i,1,5){
                sz=0;a[sz++]=0;
                dfs(0,i);
            }
        }
        if(sum<m)DBG("??")
    }
    return 0;
}