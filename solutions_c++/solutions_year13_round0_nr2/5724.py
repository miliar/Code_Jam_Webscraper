#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
	int t, n, m, i, j, k, f,start=1;
	int a_sum[10], b_sum[10];
	cin>>t;
	while(start<=t)
	{
		cin>>n >>m;
		int arr[n][m];
		for(j=0;j<n;j++) 
		{
			a_sum[j]=0;
			for(k=0;k<m;k++)
			{
				cin>>arr[j][k];
				a_sum[j]+=arr[j][k];
			}
		}
		for(k=0;k<m;k++)
		{
			b_sum[k] = 0;
			for(j = 0; j < n; j++)
			{
				b_sum[k]+=arr[j][k];
			}
		}

		f = 0;
		for(j=0;j<n;j++) 
		{
			for(k=0;k<m;k++) 
			{
				if(arr[j][k]==1)
				{
				    if(a_sum[j]!=m && b_sum[k]!=n) 
				    {
						f = 1;
						break;
					}
				}
			}
		}

		if(f)
		{
			cout<<"Case #"<<start<<": NO\n";
		}
		else
		{
			cout<<"Case #"<<start<<": YES\n";
		}
		start++;;
	}
	return 0;
}