#include<iostream>
using namespace std;
#include<string.h>
char a[1010];
int t,i,j,k,l=0,q=1;
char b,c[2010];
int main()
{
	FILE *fout = freopen("output.txt", "w", stdout);
	cin>>t;
	while(t--)
	{
		cout<<endl;
		cin>>a;
		l=strlen(a);
		c[1000]=a[0];
		i=1000;
		k=i;
		
		for(j=1;j<=(l-1);j++)
      	{
		b=a[j];
		if(b>=c[i])
		c[--i]=b;
		else
        c[++k]=b;
		
		
			
		}
	//	cout<<endl<<k<<endl<<i;
		cout<<"\nCase #"<<q<<": ";
		q++;
		
		for(i;i<=k;i++)
		cout<<c[i];
		
	}
}
