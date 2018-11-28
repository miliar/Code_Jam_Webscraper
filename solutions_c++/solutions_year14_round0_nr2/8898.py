#include<iostream>
#include<iomanip>
#include<cmath>
using namespace std;
double F;

double timefunction(double P,double C, double X)
{
if((C/P) + X/(P+F) > (X/P))
return (X/P);
return min((X/P), (C/P) + timefunction(P+F,C,X) );
}

int main()
{
cout<<fixed;
cout<<setprecision(7);
int t;
cin>>t;
double C,X;
double time;
for(int i=1;i<=t;i++)
{
	cin>>C>>F>>X;
	time=timefunction(2.0000000,C,X);
	cout<<"Case #"<<i<<": "<<time<<endl;
}
return 0;
}
