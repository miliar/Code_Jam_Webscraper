//Bismillahir Rahmanir Rahim
//Md. Jahidul Hasan Shakil
//Dept. of ICT, Comilla University

#include<bits/stdc++.h>
using namespace std;

#define i64 long long int
#define u64 unsigned long long int
#define fin(a) freopen(a,"r",stdin)
#define fout(a) freopen(a,"w",stdout)
#define repc(i,a,b) for(__typeof(b) i=(a); i<=(b); i++)
#define repr(i,a,b) for(__typeof(b) i=(a); i>=(b); i--)
#define clr(a) a.clear()
#define sz(a) (int)a.size()
#define mem(a,b) memset(a,b,sizeof a)
#define ERASE(a) a.erase(a.begin(),a.end())

#define sc scanf
#define S(z) scanf("%d",&z)
#define SL(z) scanf("%I64d",&z)
#define S2(xx,zz) scanf("%d %d",&xx,&zz)
#define SL2(xx,zz) scanf("%I64d %I64d",&xx,&zz)
#define SC(z) scanf("%s",&z)

#define pf printf
#define pfn printf("\n")
#define pfs printf(" ")
#define PF(z) printf("%d",z)
#define PFL(z) printf("%I64d",z)
#define PF2(x,y) printf("%d %d",x,y)
#define PFS(z) printf("%s",z)
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define inf 2000000007
#define pi  acos(-1.0)
#define MAX 200007
#define MOD 1000000007LL
#define eps 1e-11

template <class T>T sqr(T x) {return x*x;}
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template <class T> inline T bigmod(T p,T e,T M)
{
    if(e==0) return 1;
    if(e%2==0){i64 t=bigmod(p,e/2,M);return (T)((t*t)%M);}
    return (T)((i64)bigmod(p,e-1,M)*(i64)p)%M;
}
template <class T> inline T bigexp(T p,T e)
{
    if(e==0)return 1;
    if(e%2==0){i64 t=bigexp(p,e/2);return (T)((t*t));}
    return (T)((i64)bigexp(p,e-1)*(i64)p);
}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}

int dx4[]={1,0,-1,0};int dy4[]={0,1,0,-1}; //4 Direction
int dx8[]={1,1,0,-1,-1,-1,0,1};int dy8[]={0,1,1,1,0,-1,-1,-1};//8 direction
int month[]={31,28,31,30,31,30,31,31,30,31,30,31};
/*
struct Graph
{
    int u,v,w;
    bool operator<(const Graph& p)
    const {return w<p.w;} // oporerta chotor jnne
}edge[10];
struct compare
{
    bool operator()(const int&l,const int&r)
    {
        return l>r;
    }
};
priority_queue<int,vector<int>,compare>pq;

i64 ncr[1005][1005];
void nCr()
{
    repc(i,0,1002) ncr[i][0]=1LL;
    repc(i,1,1002)
    repc(j,1,i)
    ncr[i][j]=(ncr[i-1][j-1]+ncr[i-1][j])%MOD;
}

*/
/******************* Code Starts here *******************/

int a[(100000005/32)+10],pr[20000000],c,t,ln,tot,dn,co;
i64 x[20],d[15],sq;
bool check(int N ,int pos)
{
    return (N & 1<<pos);
}
int sett(int N, int pos)
{
    return N=(N | (1<<pos));
}
void sieve()
{
    int sqt=(int)sqrt(100000005);
    for(int i=3;i<=sqt;i+=2)
        if((bool)check(a[i/32],i%32)==false)
        for(int j=i*i;j<=100000000;j+=(2*i))
        a[j/32]=sett(a[j/32],j%32);
        pr[++c]=2;
        for(int i=3;i<=100000000;i+=2)
        if((bool)check(a[i/32],i%32)==false) pr[++c]=i;
}

int main()
{
    fin("C-small-attempt0.in");
    fout("C output large222.txt");
    sieve();
    S(t);
    S2(ln,tot);
    pf("Case #%d:\n",++co);
    t=0;
    x[1]=1;
    x[16]=1;

    repc(i,0,1)
    {
        x[9]=i;
      repc(j,0,1)
      {
          x[10]=j;
           repc(k,0,1)
           {
               x[11]=k;
             repc(l,0,1)
             {
                 x[12]=l;
              repc(m,0,1)
              {
                  x[13]=m;
               repc(n,0,1)
               {
                   x[14]=n;
                repc(o,0,1)
                 {
                   x[15]=o;
                   dn=0;
                   bool bl=false;
                   for(i64 z=2;z<=10;z++)
                   {
                       i64 tmp=1,p=1;
                       bool bl1=false;
                       repc(s,1,15)
                       {
                          p=p*z;
                          tmp+=(p*x[16-s]);
                       }
                       if(tmp%2==0)
                       {
                           d[++dn]=2;
                           bl1=true;
                       }
                       else
                       {
                          sq=sqrt(tmp);
                          for(i64 h=1;pr[h]<=sq && h<=c;h++)
                          {
                              if(tmp%pr[h]==0)
                              {
                                d[++dn]=pr[h];
                                bl1=true;
                                break;
                              }
                          }
                       }
                       if(bl1==false)
                       {
                           bl=true;
                           break;
                       }
                   }
                   if(bl==true) continue;
                   else
                   {
                      for(int h=1;h<=16;h++)
                        pf("%lld",x[h]);
                      for(int h=1;h<=dn;h++)
                        pf(" %lld",d[h]);
                        pfn;
                      t++;
                      if(t==tot) return 0;
                   }
                 }
               }
              }
             }
           }
      }
    }

    return 0;
}
