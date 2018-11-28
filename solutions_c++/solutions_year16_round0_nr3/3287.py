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

const int    prime1 = 999983;
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

bool prime[MAX];
int pr[MAX];
int num;

void init(){
    mem(prime,0);
    num=0;
    for(int i=2;i<sqrt(MAX);i++){
        if(!prime[i]){
            for(int j=i*i;j<MAX;j+=i) prime[j]=1;
        }
    }
    for(int i=2;i<MAX;i++){
        if(!prime[i]) pr[num++]=i;
    }
}
int main(){
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    init();
    for(int ii=1;ii<=t;ii++){
        int n,J;
        cin>>n>>J;
        int sum=0;
        printf("Case #%d:\n",ii);
        for(int i=0;i<(1<<(n-2));i++){
            int x=(i<<1)+(1<<(n-1))+1;
            string s="";
            while(x){
                s=(char)(x%2+'0')+s;
                x/=2;
            }
            int f=0;
            vector <int> ans;
            for(int j=2;j<=10;j++){
                LL temp=0;
                for(int k=0;k<s.size();k++)
                    temp=temp*j+(s[k]-'0');
                int bool1=0;
                for(int k=0;k<num && (LL)pr[k]*pr[k]<=temp;k++){
                    if(temp%pr[k]==0){
                        ans.push_back(pr[k]);
                        bool1=1;
                        break;
                    }
                }
                if(bool1==0){
                    f=1;
                    break;
                }
            }
            if(f)
                continue;
            else{
                cout<<s;
                for(int k=0;k<ans.size();k++) printf(" %d",ans[k]);
                cout<<endl;
                sum++;
            }
            if(sum==J)
                break;
        }
    }
    return 0;
}
