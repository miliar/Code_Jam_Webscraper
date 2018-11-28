#include<stdio.h>
#include<stdlib.h>
#include<cstring>
#include<iostream>
#include<ctype.h>
#include<algorithm>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<cmath>
#include<bitset>
#include<iomanip>
#include<complex>
#include<utility>
 
#define X first
#define Y second
#define gc getchar_unlocked
#define REP(i,n) for(int i=0;i<(n);i++)
#define REP_1(i,n) for(int i=1;i<=(n);++i)
#define REP_2(i,a,b) for(int i=(a);i<(b);++i)
#define REP_3(i,a,b) for(int i=(a);i<=(b);++i)
#define REP_4(i,a,b,c) for(int i=(a);i<(b);i+=(c))
#define DOW_0(i,n) for(int i=(n)-1;-1<i;--i)
#define DOW_1(i,n) for(int i=(n);0<i;--i)
#define DOW_2(i,a,b) for(int i=(b);(a)<i;--i)
#define DOW_3(i,a,b) for(int i=(b);(a)<=i;--i)
#define FOREACH(a,b) for(typeof((b).begin()) a=(b).begin();a!=(b).end();++a)
#define RFOREACH(a,b) for(typeof((b).rbegin()) a=(b).rbegin();a!=(b).rend();++a)
#define PB push_back
#define PF push_front
#define MP make_pair
#define IS insert
#define ES erase
#define IT iterator
#define RI reserve_iterator
#define PQ priority_queue
#define LB lower_bound
#define UB upper_bound
#define ALL(x) x.begin(),x.end()
 
#define PI 3.1415926535897932384626433832795
#define EXP 2.7182818284590452353602874713527
#define MOD7 10000007
#define MOD9 1000000009
using namespace std;
 
typedef long double LL;
typedef long double LD;
typedef double DB;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef pair<int,PII> PIII;
//typedef pair<LD,int> PLDI;
typedef vector<PII> VII;
 
template<class T>
T Mul(T x,T y,T P){
T F1=0;
while(y)
{
if(y&1)
{
F1+=x;
if(F1<0||F1>=P)F1-=P;
}
x<<=1;
if(x<0||x>=P)x-=P;
y>>=1;
}
return F1;
}
 
template<class T>
T Pow(T x,T y,T P){
T F1=1;x%=P;
while(y)
{
if(y&1)
{
F1=Mul(F1,x,P);
}
x=Mul(x,x,P);
y>>=1;
}
return F1;
}

template<class T>
T Swap(T &x,T &y)
{
	int tmp=x;
	x=y;
	y=tmp;
}
 
template<class T>
T Gcd(T x,T y){
if(y==0)return x;
T z;
while(z=x%y){
x=y,y=z;
}
return y;
}

template<class T>
T Abs(const T x){
return x<0?-x:x;
}

/*------------------------------------------------------------------------------------------------------------------------------------------*/

int main()
{
 LL c,x,t,f,i,r,time;
 scanf("%Lf",&t);
 for(i=1;i<=t;i++)
 {
  
scanf("%Lf%Lf%Lf",&c,&f,&x);
  r=2;
  time=0;
  while(true)
  {
   if((c/r+x/(r+f))<x/r)
    {   
     time+=c/r;
    r+=f;
    }
   else
    {
      time+=x/r;
       break;    
    }
  }

  printf("Case #%.0Lf: %.7Lf\n",i,time);
 }

return 0;
}


