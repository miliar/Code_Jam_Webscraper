#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{	freopen("input.in","r",stdin);
	//freopen("output.in","w",stdout);
		int t,s;
	//int a[2000],test[2000];
	char a[1500];
	int i,rescount,pcount,m;
	
	cin>>t; m=1;
	while(t--)
	{	pcount=0; rescount=0;
		cin>>s;
		
		scanf("%s",a);
		//cout<<a[0]-'0'<<endl;
		pcount=a[0]-'0';
		
		for(i=1;i<=s;i++)
		{	
			if(pcount>=i)
			{
				pcount+=(a[i]-'0');
			}
			else
			{
				rescount+=(i-pcount);
				pcount+=(i-pcount)+(a[i]-'0');
			}
		}
		
		printf("Case #%d: %d\n",m,rescount);
		m++;
		
	}
	
}
