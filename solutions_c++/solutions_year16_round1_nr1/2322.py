#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;

int main()
{
	freopen("Aa.in","r",stdin);
	freopen("output","w",stdout);
	int t,i,j,l,k;
	cin>>t;
	for(j=1;j<=t;j++)
	{
		char a[1001],b[2000],beg=1000,last=1000;
		cin>>a;
		l=strlen(a);
		b[beg]=a[0];
		for(i=1;i<l;i++)
		{
			if(a[i]>=b[beg])
			{
				beg--;
				b[beg]=a[i];	
			}
			else
			{
				last++;
				b[last]=a[i];
			}		
		}
		cout<<"Case #"<<j<<": ";
		for(k=beg;k<=last;k++)
		cout<<b[k];
		cout<<"\n";
	}
	return 0;
}
