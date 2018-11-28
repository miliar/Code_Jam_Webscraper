#include<iostream>
#include<iomanip>
using namespace std;

int main()
{
double c,f,x,time1,time2,s;
int l,t;
cin>>t;
l=t;
while(t--)
{
    s=2;
    cin>>c>>f>>x;
    time1=x/s;
    s=s+f;
    time2=c/(s-f)+x/(s);
    if(time1<=time2);
    else{
    while(time2<time1)
    {
        time1=time2;
    s=s+f;
        time2=time1-x/(s-f)+c/(s-f)+x/(s);
    }
    }
   cout<<"Case #"<<l-t<<": "<<fixed<<setprecision(7)<<time1<<endl;

}



return 0;
}
