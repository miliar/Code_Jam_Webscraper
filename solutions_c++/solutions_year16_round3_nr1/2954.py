#include<iostream>
#include<list>
#include<string>
#include<cstring>
#include<sstream>
#include<cctype>
#include<string.h>
#include<algorithm>
#include<cmath>
#include<stack>
#include<fstream>
#include<cstdlib>
#include<vector>
#include<map>
#include<set>
#include<utility>
#include<iomanip>
#include<queue>
using namespace std;

#define LL long long int
#define uLL unsigned long long int

#define S(a) scanf("%d",&a)
#define S2(a,b) scanf("%d%d",&a,&b)
#define S3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define SLL(a) scanf("%lld",&a)
#define SLL2(a,b) scanf("%lld%lld",&a,&b)
#define SLL3(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define SC(a) scanf("%c",&a)
#define P(a) printf("%d",a)
#define PS(a) printf("%s",a)
#define PLL(a) printf("%lld",a)
#define PCASE(kk) printf("Case %d: ",kk++)
#define PCASENL(kk) printf("Case %d:\n",kk++)
#define NL puts("")

#define pb(a) push_back(a)
#define mp(a,b) make_pair(a,b)
#define pi (2.0*acos(0.0))
#define pii pair<int,int>

template<typename T>inline T POW(T B,T P)
{
    if(P==0) return 1;
    if(P&1) return B*POW(B,P-1);
    else return SQR(POW(B,P/2));
}
template <typename T>inline T ModInv (T b,T m)
{
    return BigMod(b,m-2,m);
}
template<typename T>inline T ABS(T a)
{
    if(a<0)return -a;
    else return a;
}
template<typename T>inline T gcd(T a,T b)
{
    if(a<0)return gcd(-a,b);
    if(b<0)return gcd(a,-b);
    return (b==0)?a:gcd(b,a%b);
}
template<typename T>inline T lcm(T a,T b)
{
    if(a<0)return lcm(-a,b);
    if(b<0)return lcm(a,-b);
    return a*(b/gcd(a,b));
}
template <class T> inline T BMOD(T p,T e,T m)
{
    T ret=1;
    while(e)
    {
        if(e&1) ret=(ret*p)%m;
    }
    return (T)ret;
}

//for(__typeof(pp.begin()) i=pp.begin(); i!=pp.end(); i++ )

//knight and king move....

//int Dx[]={-2,-1,1,2,1,2,-2,-1};
//int Dy[]={-1,-2,2,1,-2,-1,1,2};
//int dx[]={-1,1,0,0};
//int dy[]={0,0,-1,1};
//int dx[]= {-1,-1,0,0,1,1};
//int dy[]= {-1,0,-1,1,0,1};
int dx[]= {-1,-1,-1,0,0,1,1,1};
int dy[]= {-1,0,1,-1,1,-1,0,1};
//////////////

int n;
struct let{
int id,cn;
}arr[30];

bool cmp(let x,let y)
{
    if(x.cn<y.cn)return true;
    return false;
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);

    int t,tc=1;
    S(t);
    while(t--)
    {
        S(n);
        int tot=0;
        for(int i=1;i<=n;i++)
        {
            S(arr[i].cn);
            tot+=arr[i].cn;
            arr[i].id=i;
        }

        sort(arr+1,arr+1+n,cmp);
        printf("Case #%d: ",tc++);


        while(tot)
        {
            int mx1=arr[n].id;
            int mx2=arr[n-1].id;

            int t1=arr[n].cn;
            int t2=arr[n-1].cn;
//            int t3=arr[n-1].cn;

            int hlf=(tot+1)/2;

            int hf1=(tot-2)/2;
//            int hf2=(tot)/2;

            if( (t1-2)<=t2 && t2<=hf1)
            {
//                cout<<t1<<" "<<t2<<" "<<hf1<<endl;
                printf(" %c%c",((arr[n].id-1)+'A') ,((arr[n].id-1)+'A') );
                tot-=2;
                arr[n].cn-=2;
            }
            else if((t1-2)>t2 && arr[n].cn-2<=hf1)
            {
                printf(" %c%c",((arr[n].id-1)+'A') ,((arr[n].id-1)+'A') );
                tot-=2;
                arr[n].cn-=2;

            }
            else
            {
                if(tot==3)
                {
                    printf(" %c",((arr[n].id-1)+'A'));
                    tot--;
                    arr[n].cn-=1;
                }
                else if(max(t1-1,t2-1)<=hf1)
                {
                    printf(" %c%c",((arr[n].id-1)+'A') ,((arr[n-1].id-1)+'A') );
                    tot-=2;
                    arr[n].cn-=1;
                    arr[n-1].cn-=1;

                }

            }

//            if(tot==3)
//            {
//                printf(" %c")
//            }
            sort(arr+1,arr+1+n,cmp);



        }
        NL;



    }
    return 0;
}
