// code jam.cpp : �������̨Ӧ�ó������ڵ㡣
//
#include "stdafx.h"
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int t;
int s[101];
int main()
{
	freopen("lin.txt","r",stdin);
	freopen("lout.txt","w",stdout);
	int T;
	cin>>T;
	int a,n;
	for(int t=1;t<=T;t++)
	{
		cin>>a>>n;
		for(int i=0;i<n;i++)
			cin>>s[i];
		sort(s,s+n);
		cout<<"Case #"<<t<<": ";
		int ans=n;
		if(a==1)
		{
			cout<<n<<endl;
			continue;
		}
		for(int i=0;i<=n;i++)
		{
			int sum=n-i;
			int size=a;
			for(int j=0;j<i;j++)
			{
				if(size>s[j])
					size+=s[j];
				else
				{
					while(size<=s[j])
					{
						size+=size-1;
						sum++;
					}
					size+=s[j];
				}
			}
			if(sum<ans)
				ans=sum;
		}
		cout<<ans<<endl;
	}

	return 0;
}

