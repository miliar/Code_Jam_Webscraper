#include<iostream>
#include<stdlib.h>
using namespace std;

int flip(char arr[],int a,int b)
{
	int n;
	if(a==0 || b==0)
	{
		if(a==0)
			n=--b;
		else
			n=--a;
		for(int i=0;i<=n;i++)
		{
			if(arr[i]=='+')
				arr[i]='-';
			else
				arr[i]='+';
		}
		return 1;
	}
	else return 0;
}

int len(char a[])
{
	int i=0;
	while(a[i]=='-' || a[i]=='+')
	{
		i++;
	}
	a[i]='\0';
	return i--;
}

int find_plus(char arr[],int n)
{
	for(int i=0;i<=n;i++)
	{
		if(arr[i]=='+')
			return i;
	}
	return -1;
}

int find_minus(char arr[],int n)
{
	for(int i=0;i<=n;i++)
	{
		if(arr[i]=='-')
			return i;
	}
	return -1;
}

int main()
{
	char pie[101];
	int cnt,a,b,t,count=0,chk,flag=0,t1=1;
	cin>>t;
	while(t>0)
	{
		count=0;
		cin>>pie;
		cnt=len(pie);
		flag=0;
		while(!flag)
		{
			a=find_plus(pie,cnt);
			if(a==-1)
			{
				a=cnt;
			}			
			b=find_minus(pie,cnt);
			if(b==-1)
			{
				flag=1;
				break;
			}
			if(a>=0 && b>=0)
			{
				chk=flip(pie,a,b);
				if(chk==1)
					count++;
			}
		}
		cout<<"Case #"<<t1<<": "<<count<<endl;
		t1++;
		t--;
	}
}
