#include<iostream>
using namespace std;
int a[26];
int check(int n)
{
	for(int i=0;i<n;i++)
	{
		if(a[i]!=1)
			return 0;
	}
	return 1;
}
int main()
{
	int t;
	cin>>t;
	char ch;
	for(int m=0;m<t;m++)
	{
		cout<<"Case #"<<m+1<<": ";
		int total=0;
		int n;
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>a[i];
			total=total+a[i];
		}
		while(check(n)==0)
		{
			int i;
			int max=0;
			for(i=0;i<n;i++)
			{
				if(a[max]<a[i])
					max=i;
			}
			for(i=0;i<n;i++)
			{
				if(i==max)
					continue;
				if(a[max]==a[i])
					break;
			}
			if(i==n)
			{
				if(a[max]==2)
				{
					a[max]--;
					ch='A'+max;
					cout<<ch<<" ";
				}
				else
				{
					a[max]-=2;
					ch='A'+max;
					cout<<ch<<ch<<" ";
				}
			}
			else
			{
				a[max]--;
				a[i]--;
				ch='A'+max;
				cout<<ch;
				ch='A'+i;
				cout<<ch<<" ";
			}
		}
		if(n%2==0)
		{
			for(int i=0;i<n;i+=2)
			{
				ch='A'+i;
				cout<<ch;
				ch='A'+i+1;
				cout<<ch<<" ";
			}
		}
		else
		{
			ch='A';
			cout<<ch<<" ";
			for(int i=1;i<n;i+=2)
			{
				ch='A'+i;
				cout<<ch;
				ch='A'+i+1;
				cout<<ch<<" ";
			}
		}
		cout<<endl;
	}
	return 0;
}
