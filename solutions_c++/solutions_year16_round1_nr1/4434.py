#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,k=1;
	cin>>t;
	while(t--)
	{
		char c[1005]={},d[1005]={};
		int i,j;
		cin>>c;
		d[0]=c[0];
		for(i=1;i<strlen(c);i++)
		{
			if(c[i]<d[0])	d[i]=c[i];
			else
			{
			 j=strlen(d);
			 for(j;j>0;j--)	d[j]=d[j-1];
			d[0]=c[i];
			}
		}
		cout<<"Case #"<<k++<<": "<<d<<endl;
		}
}
