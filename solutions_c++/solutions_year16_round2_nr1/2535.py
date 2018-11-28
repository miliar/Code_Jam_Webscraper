// ==========================================================================
//
//                   Bismillahir-Rahmanir-Rahim
//
// ==========================================================================
#include <bits/stdc++.h>
#define        ll                              long long
#define        f(x,y,z)                        for(int x=y;x<z;x++)
#define        pii                             pair<int,int>
#define        pll                             pair<ll,ll>
#define        CLR(a)                          memset(a,0,sizeof(a))
#define        SET(a)                          memset(a,-1,sizeof(a))
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
int ar[200];

int main()
{
    string s[11]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
    ///ios_base::sync_with_stdio(0); cin.tie(0);
   // freopen("out.txt","w",stdout);
    int test=nxt();
    int cs=1;
    while(test--){
         string st;
         cin>>st; vector<int>v;
         for(int i=0;i<st.length();i++){
            ar[st[i]]++;
        }
        while(ar['Z']){
            v.pb(0);
            for(int i=0;i<4;i++)
                  ar[s[0][i]]--;

        }
        while(ar['W']){
            v.pb(2);
            for(int i=0;i<3;i++)
                  ar[s[2][i]]--;

        }
        while(ar['G']){
            v.pb(8);
            for(int i=0;i<5;i++)
                  ar[s[8][i]]--;

        }

        while(ar['X']){
            v.pb(6);
            for(int i=0;i<3;i++)
                  ar[s[6][i]]--;

        }
        while(ar['U']){
            v.pb(4);
            for(int i=0;i<4;i++)
                  ar[s[4][i]]--;

        }
        while(ar['R']){
            v.pb(3);
            for(int i=0;i<5;i++)
                  ar[s[3][i]]--;

        }
        while(ar['S']){
            v.pb(7);
            for(int i=0;i<5;i++)
                  ar[s[7][i]]--;

        }
        while(ar['F']){
            v.pb(5);
            for(int i=0;i<4;i++)
                  ar[s[5][i]]--;

        }
        while(ar['O']){
            v.pb(1);
            for(int i=0;i<3;i++)
                  ar[s[1][i]]--;

        }
       while(ar['N']){
            v.pb(9);
            for(int i=0;i<4;i++)
                  ar[s[9][i]]--;

        }
        sort(v.begin(),v.end());
        printf("Case #%d: ",cs++);
        for(int i=0;i<v.size();i++)
              printf("%d",v[i]);
      printf("\n");
      CLR(ar);

    }


      return 0;
}

