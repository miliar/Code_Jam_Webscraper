#include<iostream>
using namespace std;
char st[100];
int chk_st(char s[],int n)
{
	for(int i=0;i<n;i++)
	{
		if(s[i]!='+')
			return 0;
	}
	return 1;
}
int flip(int l)
{
	int i,flag=0,j;
	if(st[l-1]=='-')
	{
		for(i=l-2;i>=0;i--)
		{
			if(st[i]=='+')
			{
				flag=1;
				break;
			}
		}
	}
	if(st[l-1]=='+')
	{
		for(i=l-2;i>=0;i--)
		{
			if(st[i]=='-')
			{
				flag=2;
				break;
			}
		}
	}
	if(flag==0)
	{
		for(i=0;i<l;i++)
			st[i]='+';
		return 1;
	}
	else if(flag==1)
	{
		for(j=i+1;j<l;j++)
			st[j]='+';
		return 1;
	}
	else
	{
		while(st[i]=='-')
			st[i--]='+';
		return 2;
	}
}
int main()
{
	int t;
	int c=0;
	cin>>t;
	while(t--)
	{
		c++;
		int count=0,i;
		string str;
		cin>>str;
		int l=str.length();
		int j=l-1;
		for(i=0;i<l;i++)
			st[j--]=str[i];
		while(chk_st(st,l)==0)
		{
			count+=flip(l);
		}
		cout<<"Case #"<<c<<": "<<count<<endl;
	}
}
