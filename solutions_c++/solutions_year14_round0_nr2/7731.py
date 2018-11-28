#include<fstream>
#include<iostream>
#include<stdio.h>
#include<iomanip>
using namespace std;

int main()
{

ifstream in;
ofstream ou;
int t,i=1;
double c,f,x,p=2,n,time,k=1;

in.open("B-large.in",ios::in);
if(!in)
{
cout<<"input File error";
return 0;
}
ou.open("B-large.txt",ios::out);
if(!ou)
{
cout<<"ouput File error";
return 0;
}
in>>t;
cout<<t;
while(i<=t)
{
p=2;
ou<<"Case #"<<i<<": ";
in>>c>>f>>x;
	time=x/2;
		n=c/p;	
		while(time>(n+(x/(p+f))))
		{
			time=(n+x/(p+f));
			p=p+f;
			n=n+c/p;
			k=k;
		}
ou<<setprecision(12)<<time<<"\n";
cout<<k;
i++;			
}

in.close();
ou.close();
return 0;

}
