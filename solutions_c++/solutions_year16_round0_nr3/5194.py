#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <algorithm>
using namespace std;

#define nln        puts("")                         ///prLLInewline
#define getLLI(a)  scanf("%d",&a);
#define mx3(a,b,c) mx(a,mx(b,c))                  ///3 ta theke mx
#define min3(a,b,c) min(a,min(b,c))                  ///3 ta theke min

#define FOR1(i,n)  for(LLI i=1;i<=n;i++)
#define FOR0(i,n)  for(LLI i=0;i<n;i++)                 ///looping
#define FORR(i,n)  for(LLI i=n-1;i>=0;i--)
#define ALL(p)     p.begin(),p.end()

#define SET(p)     memset(p,-1,sizeof(p))
#define CLR(p)     memset(p,0,sizeof(p))            ///memset
#define MEM(p,v)   memset(p,v,sizeof(p))

#define READ(f)    freopen(f, "r", stdin)           /// file
#define WRITE(f)   freopen(f, "w", stdout)

#define SZ(c)      (LLI)c.size()
#define PB(x)      push_back(x)                     ///STL defines
#define MP(x,y)    make_pair(x,y)
#define ff         first
#define ss         second

#define LI         long LLI
#define LLI        long long
#define f64        long double
#define PI         acos(-1.0)                        ///PI er value

LLI Set(LLI N,LLI pos)
{
    return N=N | (1ll<<pos);
}
LLI reset(LLI N,LLI pos)
{
    return N= N & ~(1ll<<pos);
}
bool check(LLI N,LLI pos)
{
    return (bool)(N & (1ll<<pos));
}
void CI(LLI &_x)
{
    scanf("%d",&_x);
}

void CO(LLI &_x)
{
    cout<<_x;
}

template<typename T> void getarray(T a[],LLI n)
{
    for(LLI i=0; i<n; i++) cin>>a[i];
}
template<typename T> void prLLIarray(T a[],LLI n)
{
    for(LLI i=0; i<n-1; i++) cout<<a[i]<<" ";
    cout<<a[n-1]<<endl;
}

const double EPS=1e-9;                              ///constatnts
const LLI INF=0x7f7f7f7f;

LLI dr8[8]= {1,-1,0,0,1,-1,-1,1};            ///8 direction move
LLI dc8[8]= {0,0,-1,1,1,1,-1,-1};
LLI dr4[4]= {0,0,1,-1};                      ///4 direction move
LLI dc4[4]= {-1,1,0,0};                      ///or adjacent dir.
LLI kn8r[8]= {1,2,2,1,-1,-2,-2,-1};          ///knight moves
LLI kn8c[8]= {2,1,-1,-2,-2,-1,1,2};


//prime genrator sieve
#define mx 1000000
bool statue[mx+7];
vector<long long>prime;
void sieve()
{
    memset(statue,true,sizeof statue);
    for(unsigned long long i=3; i*i<=mx; i+=2)
        if(statue[i]==true)
            for(unsigned long long j=i*i; j<=mx; j+=i+i)
                statue[j]=false;
    prime.push_back(2);
    for(unsigned long long i=3; i<=mx; i+=2)
        if(statue[i]==true)
            prime.push_back(i);


}
LLI N;
bool divide(LLI mask,LLI base,LLI d)
{

    LLI num=0,temp=0;
    for(LLI i=N-1; i>=0; i--)
    {
if(temp<3*mx)
temp=((temp*base)%d+check(mask,i));
        num=((num*base)%d+check(mask,i))%d;

    }
    if(temp<mx && temp==d)return 0;
    if(num==0)return 1;
    return 0;

}
bool visit[mx+7];
LLI P_(LLI a,LLI b)
{

    if(b==0)return 1;
    if(b%2)return a*P_(a,b-1);
    else
    {
        LLI temp=P_(a,b/2);

        return temp*temp;
    }

}
LLI func(LLI mask)
{
    vector<LLI>V;
    LLI sz=prime.size();
//    memset(base,0,sizeof base);
    for(LLI i=2; i<=10; i++)
    {
        bool p=0;
        LLI num=0;
        for(int j=0; j<N; j++)if(check(mask,j))num+=P_(i,j);
      //  cout<<"FF "<<i<<" : "<<num<<"\n";
        for(LLI j=0; j<sz; j++)
            if(num%prime[j]==0&&num!=prime[j])
            {
//                cout<<"SS "<<num<<" "<<prime[j]<<"\n";
                V.PB(prime[j]);
                break;
            }

//            if(V[i].size()<10)return 0;
//       // if(visit[prime[j]]==0)
//        {
//            if(divide(mask,i,prime[j]))
//            {
//                p=1;
//                V.PB(prime[j]);
//                break;
//
//            }
//
//        }
//        if(p==0)return 0;

    }
//    for(LLI i=0; i<V.size(); i++)visit[prime[i]]=1;
//cout<<"FFF NNNNNNNN \n";
    if(V.size()<9)return 0;
//    puts("OKK");
    for(LLI k=N-1; k>=0; k--)
        cout<<check(mask,k);
    for(LLI i=0; i<V.size(); i++)
        cout<<" "<<V[i];
    puts("");
    return 1;
}
int main()
{
    READ("input.txt");
    WRITE("output.txt");

    sieve();
    LLI t,kase=1;
    cin>>t;
    while(t--)
    {
        LLI J;
        cin>>N>>J;
        cout<<"Case #1:\n";
        LLI mask=0;
        mask=Set(mask,0);
        mask=Set(mask,N-1);
        LLI lim=1<<(N-2);
        lim--;
        for(LLI i=0; J>0&&i<=lim; i++)

            {
                LLI n_mask=mask+(i*2);


                if(func(n_mask))
                {


                    J--;
                }
              //  break;

            }



    }

    return 0;
}


