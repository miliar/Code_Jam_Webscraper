// ==========================================================================
//
//                   Bismillahir-Rahmanir-Rahim
//
// ==========================================================================
#include <bits/stdc++.h>
#define        ll                              long long
#define        f(x,y,z)                        for(int x=y;x<z;x++)
#define        take1(a);                       scanf("%d",&a);
#define        take2(a,b);                     scanf("%d%d",&a,&b);
#define        take3(a,b,c);                   scanf("%d%d%d",&a,&b,&c);
#define        take4(a,b,c,d);                 scanf("%d%d%d%d",&a,&b,&c,&d);
#define        pii                             pair<int,int>
#define        mem(a,x)                        memset(a,x,sizeof(a))
#define        N                               1000010
#define        M                               1000000007
#define        pi                              acos(-1.0)
#define        ff                              first
#define        ss                              second
#define        pb                              push_back
#define        inf                             (int)1e9
using namespace std;
int dx[]={0,0,1,-1,-1,-1,1,1};
int dy[]={1,-1,0,0,-1,1,1,-1};
template < class T> inline T gcd(T a, T b){while(b){a%=b;swap(a,b);}return a;}
template <typename T> string NumberToString ( T Number ) { ostringstream ss; ss << Number; return ss.str(); }
inline int nxt(){int aaa;scanf("%d",&aaa);return aaa;}
inline ll lxt(){ll aaa;scanf("%lld",&aaa);return aaa;}
template <class T> inline T bigmod(T p,T e,T m){T ret = 1;
for(; e > 0; e >>= 1){
    if(e & 1) ret = (ret * p) % m;p = (p * p) % m;
} return (T)ret;}
#define sayed
#ifdef sayed
     #define debug(args...) {cerr<<"Debug: "; dbg,args; cerr<<endl;}
#else
    #define debug(args...)  // Just strip off all debug tokens
#endif
struct debugger{
    template<typename T> debugger& operator , (const T& v){
        cerr<<v<<" ";
        return *this;
    }
}dbg;
///******************************************START******************************************
vector<ll> v[100];
void prime(ll n,int head){
  int sq=sqrt(n);
  for(ll i=2;i<=sq;i++){
      if(n%i==0) {
        v[head].pb(i);
        break;
      }
  }
}
void go(ll n,int head){
    ll p=0,q=n;
    for(ll i=2;i<=10;i++){
           ll j=0;q=n,p=0;ll m=1;
            while(q){
                 p+=((q%10))*m;
                  m=m*i;
                q/=10;
            }

           prime(p,head);
    }
}
ll ar[]={1000000000000001,1000000000000101,1000000000001001,1000000100000001,1000010000000011,1000010000001001,1000010000100001,1000010010000001,1000010100000001,1000011000000001,1000100000000001,1001000000000001,1001000000000011,1001000000001001,1001000000010001,1001000000100001,1001000010000001,1001000100000001,1001001000000001,1001100000000001,1010000000000011,1010000000000101,1010000000010001,1010000001000001,1010000100000001,1010001000000001,1010010000000001,1011000000000001,1100000000000011,1100000000001001,1100000000100001,1100000010000001,1100001000000001,1100100000000001,1110000000000001,1110000000001001,1110000000010001,1110100000000011,1110100000000101,1111000000000011,1111000000000101,1111000000001001,1111000000010001,1111000000100001,1111000001000001,1111000010000001,1111000100000001,1111001000000001,1111010000000001,1111100000000001,0};
    int main()
{
     //freopen("out.txt","w",stdout);
      for(int i=0;i<50;i++) go(ar[i],i);
      int a,b,c;
    cin>>a>>b>>c;
    printf("Case #1:\n");
     for(int i=0;i<50;i++){
         printf("%lld",ar[i]);
         for(int j=0;j<v[i].size();j++)
              printf(" %lld",v[i][j]);
         printf("\n");

     }
      return 0;
}

