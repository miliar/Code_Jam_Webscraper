#include<fstream>
#include<iostream>
#include<stdio.h>
#include<iomanip>
using namespace std;

int main()
{

ifstream in;
ofstream ou;

int t,i,smax,n=1,a,f;
char arr1[1001];

in.open("A-small-attempt0.in",ios::in);
if(!in)
{
cout<<"input File error";
return 0;
}
ou.open("A-small.txt",ios::out);
if(!ou)
{
cout<<"ouput File error";
return 0;
}
in>>t;
cout<<t;
while(n<=t)
{
	
ou<<"Case #"<<n<<": ";

in>>smax;


in>>arr1;
a=0;
f=0;
for(i=0;i<=smax;i++)
{
	if(i>a&&((arr1[i]-48)>0))
	{
		f=f+(i-a);
		a=a+f;
	}
	a=a+(arr1[i]-48);
	
}
ou<<f<<"\n";
n++;
}

in.close();
ou.close();
return 0;

}
