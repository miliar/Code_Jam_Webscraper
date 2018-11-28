#include <bits/stdc++.h>
#define ll long long 
using namespace std;


ll dp[1005][1005]={0};

void function()
{
	int i,j;
	for(i=2;i<=1000;i++)
	{
		for(j=1;j<i;j++)
		{
			     dp[i][j]=dp[i-j][j]+1;
		}
	}
}



int main(int argc, char const *argv[])
{
	ll t,i,j,k,min,arr[1005],d;
	cin >>t;

	function();
	for(i=1;i<=t;i++)
	{
		cin >> d;
		for(j=1;j<=d;j++)
		{
			cin >> arr[j];
		}

		ll hello[1005]={0};

		for(j=1;j<=1000;j++)
		{
			for(k=1;k<=d;k++)
			{
				hello[j]+=dp[arr[k]][j];
			}
		}

		min=1+hello[1];

		for(j=2;j<=1000;j++)
		{
             if(min>j+hello[j])
             	min=j+hello[j];
		}
		cout << "Case #" << i << ": "  << min << endl;
	}
	return 0;
}