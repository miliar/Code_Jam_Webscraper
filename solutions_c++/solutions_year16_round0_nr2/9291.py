#include<iostream>
#include<fstream>
#include<string.h>
//#include<conio.h>
using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output","w",stdout);
	int i,j,k,t,l,x,count;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		char a[101];
		count=0;
		cin>>a;
		l=strlen(a);
		j=0;
		while(j<l)
		{
			k=0;
			while(a[k]==a[k+1] && k<l-1)
			{
				k++;
			}
			if(k==l-1 && a[k]=='+')
			break;
			if(a[k]=='-')
			for(x=0;x<=k;x++)
			{
				a[x]='+';
			}
		 	else if(a[k]=='+')
			for(x=0;x<=k;x++)
			{
				a[x]='-';
			}
			count++;			
		}
		cout<<"Case #"<<i<<": "<<count<<"\n";
	}
	return 0;
}
