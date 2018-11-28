#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main()
{
	int t, k;
	cin>>t;
	k = 1;
	while(t--)
	{
		int temp = 0;
		long long int count1 = 0, count2 = 0;
		int n,i,  m[1010] = {0};
		cin>>n;
		for(i = 0;i<n;i++)
			cin>>m[i];
		for(i=0;i<=n-2;i++)
		{
			if(m[i] > m[i+1])
				count1 += (m[i] - m[i+1]);
			// cout<<i<<" ";
			// cout<<count1<<" ";
		}
			// cout<<m[0]<<" "<<m[1];

		// cout<<m[0]<<m[1]<<m[2]<<m[3];
		for(i=0;i<=n-2;i++)
		{
			if((m[i] - m[i+1]) > temp)
				temp = (m[i] - m[i+1]);
		}
		// cout<<temp;
		for(i=0;i<n-1;i++)
		{
			// if(m[i+1] < m[i])
			// {
				if(m[i] > temp)
					count2 += temp;
				else
					count2 += m[i];
			// }
		}
		cout <<"Case #"<<k<<": "<<count1<<" "<<count2<<endl;
		k++;
	}
	return 0;
}