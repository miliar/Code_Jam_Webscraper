#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cmath>
#include <string>
#include <vector>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#pragma comment(linker,"/STACK:102400000,102400000")

using namespace std;
#define   MAX           100005
#define   MAXN          1000005
#define   maxnode       55
#define   sigma_size    30
#define   lson          l,m,rt<<1
#define   rson          m+1,r,rt<<1|1
#define   lrt           rt<<1
#define   rrt           rt<<1|1
#define   middle        int m=(r+l)>>1
#define   LL            long long
#define   LD            long double
#define   ull           unsigned long long
#define   mem(x,v)      memset(x,v,sizeof(x))
#define   lowbit(x)     (x&-x)
#define   pii           pair<int,int>
#define   bits(a)       __builtin_popcount(a)
#define   mk            make_pair
#define   limit         10000

const int    prime = 999983;
const int    INF   = 0x3f3f3f3f;
const LL     INFF  = 0x3f3f;
const double pi    = acos(-1.0);
const double inf   = 1e18;
const double eps   = 1e-8;
const LL     mod   = (LL)1e9+7;
const ull    mx    = 133333331;
const int    ma    = 1e9;

/*****************************************************/
inline void RI(int &x) {
      char c;
      while((c=getchar())<'0' || c>'9');
      x=c-'0';
      while((c=getchar())>='0' && c<='9') x=(x<<3)+(x<<1)+c-'0';
 }
/*****************************************************/

int n,t;
string s;

int main(){
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    cin>>t;
    for(int ii=1;ii<=t;ii++){
        cin>>s;
        int ans=0;
        for(int i=1;i<s.size();i++){
            if(s[i]!=s[i-1])
                ans++;
        }
        if(s[s.size()-1]=='-')
            ans++;
        printf("Case #%d: %d\n",ii,ans);
    }
    return 0;
}
