#include<fstream>
#include<iostream>
#include<stdio.h>
#include<iomanip>
using namespace std;

int main()
{

ifstream in;
ofstream ou;
long t,i=1,a,b,k,m,n,total;

in.open("input.in",ios::in);
if(!in)
{
cout<<"input File error";
return 0;
}
ou.open("B-small.txt",ios::out);
if(!ou)
{
cout<<"ouput File error";
return 0;
}
in>>t;
cout<<t;
while(i<=t)
{
	total=0;
ou<<"Case #"<<i<<": ";
in>>a>>b>>k;

for(m=a-1;m>=0;m--)
for(n=b-1;n>=0;n--)
{
	if((m&n)<k)
	{
	
	total++;
//	cout<<m<<", "<<n<<", "<<(m&n)<<", "<<k<<","<<total<<"\n";
}
}
/*
for(m=b;m>=0;m--)
for(n=a;n>=0;n--)
{
	if((m&n)<=k)
	total++;
}*/

ou<<total<<"\n";
i++;			
}

in.close();
ou.close();
return 0;

}
