#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
int main()
{
	int t;
	freopen("B-large.in","rt",stdin);
	freopen("abhinavOutput.cpp","wt",stdout);
	cin>>t;
	for(int c=1;c<=t;c++)
	{
		char a[105];
		cin>>a;
		int count1=0,count2=0;
		
		if(a[0]=='+')
		{ int flag=0;
			for(int i=0;a[i]!='\0';i++)
			{
				if(a[i]=='-')
				flag=1;
				if(a[i]=='+'&&flag==1)
				{
					count2+=2;
					flag=0;
				}
			}
			if(a[strlen(a)-1]=='-')
			count2+=2;
				cout<<"Case #"<<c<<":"<<" "<<count2<<endl;
		}
		else
		{ int flag=0,flag2=0,flag3=0;
			for(int i=1;a[i]!='\0';i++)
			{
				if(a[i]=='+'&&flag==0)
				{
					flag=1;
					count2++;
					
				}
				else if(a[i]=='-'&&flag==1)
				flag2=1;
				else if(a[i]=='+'&&flag==1&&flag2==1)
				{
					count2+=2;
					flag2=0;
					
					
				}
			}
			for(int i=0;a[i]!='\0';i++)
			{
				if(a[i]=='+')
				{
					flag3=1;
					break;
				}
			}
			if(flag3==1)
			{
			
			if(a[strlen(a)-1]=='-'&&strlen(a)>1)
			   count2+=2;
			   else if(a[strlen(a)-1]=='-'&&strlen(a)==1)
			   count2++;
		}
		else
		{
			count2++;
		}
			   
				cout<<"Case #"<<c<<": "<<count2<<endl;
			
		}
	}
}
