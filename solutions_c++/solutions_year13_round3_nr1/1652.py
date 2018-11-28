/// BIS-MILLAHIR RAHMANIR RAHIM

#include<algorithm>
#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>
#include<deque>
#include<climits>

using namespace std;

#define I1(n) scanf("%d",&n)
#define LL1(n) scanf("%lld",&n)
#define I2(n1,n2) scanf("%d%d",&n1,&n2)
#define LL2(n1,n2) scanf("%lld%lld",&n1,&n2)
#define I3(n1,n2,n3) scanf("%d%d%d",&n1,&n2,&n3)
#define LL3(n1,n2,n3) scanf("%lld%lld%lld",&n1,&n2,&n3)

#define F(i, a, b) for(  i = (a); i <= (b); i++ )
#define FR(i, a, b) for(  i = (a); i < (b); i++ )
#define FRR(i, a, b) for(  i = (a); i >b; i-- )
#define Fs(i, sz) for( size_t i = 0; i < sz.size (); i++ )
#define Fe(it, x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++)
#define Pr(x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++) cout << *it << " "; cout << endl;

#define all(a) a.begin(),a.end()
#define pb push_back
#define pi acos(-1.0)
#define MEM(a,val) memset(a,val,sizeof(a))
#define eps 1e-9
#define Max(a,b) (a>b?a:b)
#define Min(a,b) (a<b?a:b)
#define sz(a) ((int)(a).size())
#define IN  freopen("input.txt","r",stdin)
#define OUT freopen("output.txt","w",stdout)
#define CLR(n) n.clear()
#define SQR(n) (n*n)
#define LEFT (idx<<1)
#define RIGHT (LEFT+1)
#define PC printf("Case %d:",cas++);
#define NL printf("\n");

template<typename T>inline T POW(T B,T P){ if(P==0) return 1; if(P&1) return B*POW(B,P-1);  else return SQR(POW(B,P/2));}
template<typename T>inline T Bigmod(T b,T p,T m){ if(p==0) return 1; else if (!(p&1)) return SQR(Bigmod(b,p/2,m)) % m;else return ((b % m) * Bigmod(b,p-1,m)) % m;}
template<typename T>inline T Dis(T x1,T y1,T x2, T y2){return sqrt( sqr(x1-x2) + SQR(y1-y2) );}

int Set(int N,int pos){return N=N | (1<<pos);}
int Reset(int N,int pos){return N= N & ~(1<<pos);}
bool Check(int N,int pos){return (bool)(N & (1<<pos));}
int toInt(string s)  { int sm; stringstream ss(s); ss>>sm; return sm; };
int toLlint(string s) { long long int sm; stringstream ss(s); ss>>sm; return sm;};

//// sieve (prime generate)
/*
#define Prime_M 10000003
bool is_prime[Prime_M];
vector<int>prime;
void prime_generate()
{
    int i,j;
    for(i=3;i<=3163;i+=2) if(!is_prime[i])for(j=i+i+i;j<Prime_M;j+=(i+i)) is_prime[j]=true;
    prime.pb(2); for(i=3;i<Prime_M;i+=2) if(!is_prime[i]) prime.pb(i);
}
*/

bool isvowel(char ch)
{
    if(ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u' ) return true;
    return false;
}

char name[105];
bool is[105];

int nv;

bool test(int st,int ed)
{
   bool flag = false;
   int s=st,e,cnt = 0;

   for(int i=st;i<=ed&&!flag;i++)
   {
       if( is[i] )
       {
           s = i+1;
       }
       else
       {
           flag = ((i-s+1)>=nv);
       }
   }

   return flag;
}

int main()
{

     freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);

    int tc,cas=1;
    int a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,cnt=0;

    I1(tc);

    while(tc--)
    {
        scanf("%s %d",name,&nv);
        cnt = 0;

        l = strlen(name);

        FR(i,0,l) is[i]  = isvowel(name[i]);

        for(i=0;i<l;i++)
        {
            for(j=i;j<l;j++)
            {
                cnt += (int)test(i,j);
            }
        }

        printf("Case #%d: %d\n",cas++,cnt);
    }

    return 0;
}
