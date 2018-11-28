#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<iostream>
#include<sstream>
#include<map>
#include<set>
#include<string>
using namespace std;

#define MAX(a,b) a>b?a:b
#define MIN(a,b) a<b?a:b
#define PI acos(-1.0)
#define SQ(x) ((x)*(x))
#define CUBE(x) ((x)*(x)*(x))
#define MAX_INT 2147483647
#define inf 1<<30
#define FOR(i,a,b) for(i=(a);i<=(b);i++)
#define FORV(i,a,b) for(i=(a);i>=(b);i--)
#define REP(i,n) for(i=0;i<(n);i++)
#define pb push_back
#define pf push_front
#define ppb pop_back
#define ppf pop_front
#define nl printf("\n")
#define set(A,x) memset(A,x,sizeof(A))
#define in(x) scanf("%d",&x)
#define inll(x) scanf("%lld",&x)
#define LL long long
//#define LL __int64
#define MX 10000

template<class T>inline T _abs(T n){return n<0?-n:n;}
template<class T>inline T _gcd(T a, T b){return b==0?a:_gcd(b,a%b);}
template<class T>inline T _lcm(T a, T b){return a/_gcd(a,b)*b;}

int setb(int N,int pos){return N= N | (1<<pos);}
int resetb(int N,int pos){return N= N & ~(1<<pos);}
bool checkb(int N,int pos){return (bool)(N & (1<<pos));}



int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output_large_a.txt","w",stdout);
    int test;
    int cases=0;
    LL n;

    in(test);
    while(test--)
    {
        inll(n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",++cases);
        }
        else
        {
            int i=1;
            LL ans;
            set<int>S;
           // printf("size %d\n",S.size());
            while(S.size()!=10)
            {
                ans= n*i;
                i++;
                //printf("ans %lld\n",ans);
                LL temp = ans;
                while(temp!=0)
                {
                    S.insert(temp%10);
                    temp/=10;
                }
            }
            printf("Case #%d: %lld\n",++cases,ans);
        }
    }

    return 0;
}
