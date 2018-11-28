#include <iostream>
#include<iomanip>
using namespace std;

int main() {
// your code goes here
int t;
double c,f,x,T,rate,balance,wait,farm,temprate;
cin>>t;
for(int k=1;k<=t;k++)
{
T=0;
rate=2;
balance=0;
cin>>c>>f>>x;
if(x<=c)
{
T=x/rate;
cout<<"Case #"<<k<<": "<<fixed<<setprecision(7)<<T<<endl;
}
else
{
wait=x/rate;
farm=c/rate;
while(1)
{
rate=rate+f;
if(farm+x/rate>wait)
{
break;
}
T+=farm;
farm=c/rate;
wait=x/rate;
}
T+=wait;
cout<<"Case #"<<k<<": "<<fixed<<setprecision(7)<<T<<endl;

}
}
return 0;
}