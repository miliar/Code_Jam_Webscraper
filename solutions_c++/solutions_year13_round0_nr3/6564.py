#include<cstdio>
#include<iostream>
using namespace std;

void main()
{
	freopen ("C-Small.in","r",stdin);
	freopen ("C-Small.txt","w",stdout);
	int n;
	cin>>n;
	int* c1=new int[n];
	int* c2=new int[n];
	long long a,b;

	long long arr[26]={1 , 4 , 9 , 121 , 484 , 10201 , 12321 , 14641 , 40804 , 44944 , 1002001 , 1234321 , 4008004 , 100020001 , 102030201 , 104060401 , 121242121 , 123454321 , 125686521 , 400080004 , 404090404 , 10000200001 , 10221412201 , 12102420121 , 12345654321 , 40000800004};
	
	for (int i=0 ; i<n ; i++)
	{
		c1[i]=0;
	}

	for (int i=0 ; i<n ; i++)
	{
		cin>>a>>b;
		for (int v=0 ; v<26 ; v++)
		{
			if (arr[v]>=a && arr[v]<=b)
			{
				c1[i]++;
			}
		}
	}

	for (int i=0 ; i<n ; i++)
	{
		cout<<"Case #"<<i+1<<": "<<c1[i]<<endl;
	}
}