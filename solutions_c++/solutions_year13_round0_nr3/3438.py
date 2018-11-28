#include<fstream>
#include<iostream>
#include<math.h>
using namespace std;
bool ispalin(int n)
{
	char a[5];
	int i,l=0;
	for(i=n;i>0;i/=10)
	{
		a[l++]=i%10;
	}
	for(i=0;i<l/2;i++)
	if(a[i]!=a[l-1-i])
	return false;
	return true;
}
int main()
{
	int t,k,a,b,count,i;
	ifstream f("1.in");
	ofstream g("1.out");
	f>>t;
	for(k=1;k<=t;k++)
	{
		f>>a>>b;
		count=0;
		for(i=a;i<=b;i++)
		{
			int l=sqrt(i);
			if(ispalin(i)&&(l*l==i)&&ispalin(l))
			count++;
		}
		g<<"Case #"<<k<<": "<<count<<endl;
	}
	return 0;
}
