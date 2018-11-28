#include<bits/stdc++.h>
#define up(j,k,i) for(i=j;i<k;i++)
#define down(j,k,i) for(i=j;i>k;i--)
#define M 1000010
#define pp(n) printf("%lld\n",n)
#define is(n) scanf("%lld",&n)
#define ss(s) scanf("%s",s)
#define cool 0
typedef int l;
typedef float f;
typedef double d;
typedef long long int lld;
using namespace std;
lld binpow(lld base,lld pow)
{
if(pow>0)
{
if(pow%2==1)
{
pow--;
return(base*binpow(base,pow/2)*binpow(base,pow/2));
}
else
return(binpow(base,pow/2)*binpow(base,pow/2));
}
else
return 1;
}
lld bin(lld t)
{
if(t<2)
return t;
return (t%2+10*bin(t/2));
}
int main()
{
fstream O,I;
bool flag=0,flag2=0;
O.open("out.txt",ios::out);
I.open("in.in",ios::in);
lld input1,input2;
I>>input1;
I>>input1>>input2;
lld i=0,t,c=0,lm=0,N,j;
O<<"Case #1:"<<endl;
N=1000000000000001;
O<<N;
up(2,11,i)O<<' '<<i+1;
O<<endl;
c=1;
while(lm<49)
{
i=2;
while(i+c<=15)
{
t=N+binpow(10,i-1)+binpow(10,i+c-1);
O<<t;
up(2,11,j)O<<' '<<j+1;
O<<endl;
lm++;
i++;
}
//cout<<lm<<endl;
c+=2;
}
return 0;
} 
