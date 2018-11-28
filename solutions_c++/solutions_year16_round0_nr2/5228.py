#include<iostream>
#include<stdio.h>
#include<cstring>
#include<math.h>
using namespace std;
int main()
{
	//char s[20];
	int a,i,j,k=0,l=0,t,z,m;
	cin>>t;
	string s[t];
	for(i=0;i<t;i++)
	{
		cin>>s[i];
	}
	while(l<t)
	{
		//cin>>s;
		//s=s[l];
		k=0;
		for(i=0;s[l][i]!='\0';i++)
		{
			z=0;
			for(m=i;s[l][m]!='\0';m++)
			{
				if(s[l][m]!=43)
				{
					z=1;
				}
			}
			if(z==0)
			{
				break;
			}
			a=s[l][i]-43;
			while(s[l][i]==s[l][i+1])
			{
				i++;
			}
			for(j=0;j<=i;j++)
			{
				if(a==0)
				{
					s[l][j]=43;
				}
				else
				{
					s[l][j]=45;
				}
			}
			k++;
		}
		if(s[l][0]==45)
		{	
			for(i=0;s[l][i]!='\0';i++)
			{
				s[l][i]=43;
			}
		}
		cout<<"Case #"<<l+1<<": "<<k<<"\n";
		l++;
	}
	return 0;
}
