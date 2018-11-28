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
#pragma comment(linker, "/STACK:102400000,102400000")

using namespace std;
#define   MAX           100005
#define   MAXN          6005
#define   maxnode       15
#define   sigma_size    30
#define   lson          l,m,rt<<1
#define   rson          m+1,r,rt<<1|1
#define   lrt           rt<<1
#define   rrt           rt<<1|1
#define   middle        int m=(r+l)>>1
#define   LL            long long
#define   ull           unsigned long long
#define   mem(x,v)      memset(x,v,sizeof(x))
#define   lowbit(x)     (x&-x)
#define   pii           pair<int,int>
#define   bits(a)       __builtin_popcount(a)
#define   mk            make_pair
#define   limit         10000

//const int    prime = 999983;
const int    INF   = 0x3f3f3f3f;
const LL     INFF  = 0x3f3f;
const double pi    = acos(-1.0);
//const double inf   = 1e18;
const double eps   = 1e-8;
const LL    mod    = 1e9+7;
const ull    mx    = 133333331;

/*****************************************************/
inline void RI(int &x) {
      char c;
      while((c=getchar())<'0' || c>'9');
      x=c-'0';
      while((c=getchar())>='0' && c<='9') x=(x<<3)+(x<<1)+c-'0';
 }
/*****************************************************/

double p[205];
int main(){
    freopen("B-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,kase=0;
    cin>>t;
    while(t--){
        int n,k;
        kase++;
        cin>>n>>k;
        for(int i=0;i<n;i++) scanf("%lf",&p[i]);
        double ans=0;
        for(int i=0;i<(1<<n);i++){
            int num=bits(i);
            if(num==k){
                vector<double> v;
                for(int j=0;j<n;j++) if(i&(1<<j)) v.push_back(p[j]);
                double temp=0;
                for(int j=0;j<(1<<k);j++){
                    int ret=bits(j);
                    if(ret==k/2){
                        double tmp=1;
                        for(int h=0;h<k;h++){
                            if(j&(1<<h)) tmp*=v[h];
                            else tmp*=(1-v[h]);
                        }
                        temp+=tmp;
                    }
                }
                ans=max(ans,temp);
            }
        }
        printf("Case #%d: %.8f\n",kase,ans);
    }
    return 0;
}
