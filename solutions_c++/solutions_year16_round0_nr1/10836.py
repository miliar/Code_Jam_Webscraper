/*This is by Technical Bangla from University of Dhaka*/
#include <bits/stdc++.h>
using namespace std;

#define pi acos(-1.0)
#define e 2.7182818284590451
#define eps 1e-14
#define in_d(x) scanf("%d",&x)
#define nl printf("\n")
#define MAX 100100
#define Mod 1000000007
#define inf 1e18
#define MOD(a,m) ((a)%(m)+(m))%(m)
#define filein freopen("/home/intelligence/Downloads/A-large.in","r",stdin)
#define fileout freopen("/home/intelligence/Downloads/A-large.out","w",stdout)
typedef long long int ll;
typedef unsigned long long int llu;

template <class T> T sqr(T x) {return x*x;}
template <class T> T distsqr(T x,T y,T a,T b) {return sqr(x-a)+sqr(y-b);}
double cosine_angle(double a,double b,double c) {return (double)(sqr(a)+sqr(b)-sqr(c))/((double)2.0*a*b);}

template <class T> T Maximum(T a, T b) {return a>b?a:b;}
template <class T> T Minimum(T a, T b) {return a<b?a:b;}
template <class T> T GCD(T a, T b) {if(!b) return a;return GCD(b,a%b);}
template <class T> void SWAP(T &a, T &b) {T temp=a;a=b;b=temp;return ;}
template <class T> T sign(T a) {return a<0?-1:1;}
template <class T> T BigMod(T a,T n,T mod) {if(!n) return (T)1%mod;ll power=BigMod(a,n>>1,mod);power%=mod;power*=power;power%=mod;if(n&1) power*=a%mod,power%=mod;return power;}
template <class T> T ExtendedEuclid(T a,T b,T c) {if(!a) return 0;return (b*ExtendedEuclid(b%a,a,-c)+c)/a;}
template <class T> T ModInverse(T a,T m) {return MOD(ExtendedEuclid(a,m,(T)GCD(a,m)),m);}

bool digit[10];

bool Check()
{
    int i;bool state=1;
    for(i=0;i<10;i++) state=state&&digit[i];
    return state;
}

void Split(ll n)
{
    while(n)
    {
        digit[n%10]=1;
        n/=10;
    }
    return ;
}

ll Solving(int n)
{
    if(!n) return -1;
    int i;ll x=0;
    for(i=0;i<10;i++) digit[i]=0;
    do
    {
        x+=n;
        Split(x);
    }
    while(!Check());
    return x;
}

void Generate(int n)
{
    FILE *fp=fopen("input.txt","w");
    int i;
    fprintf(fp,"%d\n",n);
    for(i=0;i<n+1;i++) fprintf(fp,"%d\n",i);
    fclose(fp);
    return ;
}

int main()
{
    filein;
    fileout;
    int i,n,t,caseno=0;ll val;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        printf("Case #%d: ",++caseno);
        val=Solving(n);
        if(val==-1) printf("INSOMNIA");else printf("%lld",val);nl;
    }
    return 0;
}
