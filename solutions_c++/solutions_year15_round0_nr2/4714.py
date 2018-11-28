#include<iostream>
#include<bits/stdc++.h>
#define MAX 100000000
using namespace std;

int main()
{
	int test;
	int d;
	int arr[1005];
	cin>>test;
	int i;
	int maxer=0;
	int miner;
	int sum,temp,j;
	int caser=1;
	while(test--)
	{
		cin>>d;
		for(i=0;i<d;i++)
		scanf("%d",&arr[i]);
		maxer=0;

		for(i=0;i<d;i++)
		{
			if(arr[i]>maxer)
				maxer=arr[i];
		}
		miner=MAX;
		for(i=1;i<=maxer;i++)
		{
			sum=0;
			for(j=0;j<d;j++)
			{
				if(arr[j]>i)
				{
					temp=(arr[j]-i)/i;
				if(((temp*i)+i)!=arr[j])
					temp++;

				sum=sum+temp;
				}
			}
			sum=sum+i;
			//cout<<sum<<'\t';
			if(sum<miner)
				miner=sum;
		}
		cout<<"Case #"<<caser<<": "<<miner<<endl;
		caser++;
	}
	return 0;
}
