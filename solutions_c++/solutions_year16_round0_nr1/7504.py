#include<iostream>
#include<string.h>
#include <stdio.h>
#include<cstdio>
using namespace std;

int main()
{



	long long int i,j,k,n,t,ans=0;
	freopen ("ans2016-a.txt","w",stdout);
	freopen ("A-large.in","r",stdin);
	
	cin>>t;

	
	
	for(i=0;i<t;i++)
	{
		cin>>n;
		if(n==0)
		{		
			cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		}
		else
		{
			int a[10];
			for(j=0;j<10;j++)
			{
				a[j]=0;
			}
			
			for(j=1;;j++)
			{
				long long int ans=1,temp;
				temp=n*j;
				while(temp)
				{
					int s=temp%10;
					a[s]=1;
					temp=temp/10;
				}
				
				for(k=0;k<10;k++)
				{
					ans=ans & a[k];
				}
				if(ans==1)
				{
					break;
				}
			}
				cout<<"Case #"<<i+1<<": "<<n*j<<endl;
			
		}
		
	}

   	fclose (stdout);
	fclose(stdin);
	return 0;
}
