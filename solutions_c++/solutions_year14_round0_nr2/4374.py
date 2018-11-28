#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
   int y;
cin>>y;

for(int k=1;k<=y;k++) 
   {
double c,f,x;
cin>>c>>f>>x;
long double t,p;
t=p=x/2;
for(long n=1; ; n++)
   {
     t=t+(c/(2+(n-1)*f))-(x/(2+(n-1)*f))+(x/(2+n*f));
     if (p<=t)
        break;
     else 
        p=t;
   }
cout<<"Case #"<<fixed<<setprecision(7)<<k<<": "<<p<<"\n";
}
return 0;
}