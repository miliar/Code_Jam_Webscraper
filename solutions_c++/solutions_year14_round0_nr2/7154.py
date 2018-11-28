#include<iostream>
#include<iomanip>
using namespace std;

long double c,f,x,t,cur,rate;

bool tobuy()
{if(((x-cur)/rate)<((x-cur+c)/(rate+f))) return false;
return true;}

void init()
{rate=2;cur=t=0;
cin>>c>>f>>x;}

long double process()
{init();
if(c<x)
while(cur<x)
{if(cur>=c) {if(tobuy()) {cur-=c;rate+=f;}
else {t+=(x-cur)/rate;break;}}
else {t+=(c-cur)/rate;cur=c;}
}
else t=x/rate;
return t;}

int main()
{int test;cin>>test;cout<<fixed;
for(int c=1;c<=test;c++)
{long double x=process();cout<<"Case #"<<setprecision(7)<<c<<": ";
cout<<x<<'\n';}}


