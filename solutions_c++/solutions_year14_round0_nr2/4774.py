#include<iostream>
#include<iomanip>
#include<fstream>
using namespace std;

double time (double c, double ps, double f, double x)
{
    if (c/ps+x/(ps+f)<x/ps)
    {
        ps+=f;
        return c/(ps-f)+time(c,ps,f,x);
    }
    else
        return x/ps;
}

int main()
{
ifstream cin("input2.txt");
ofstream cout("output2.txt");
long t;
double c,f,x,ans;
cin>>t;
long d=1;
double ps=2.0;
while(d<=t)
{
cin>>c>>f>>x;
cout<<"Case #"<<d<<": "<<setprecision(7)<<fixed<<time(c,ps,f,x)<<endl;
d++;
}
}
