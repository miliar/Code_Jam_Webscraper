#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t,p=0;
	cin>>t;
	while (t--)
	{
		int n;
		cin>>n;
		int arr[2009];
		memset(arr,0,sizeof(arr));
		for (int i=0; i<n; i++)
		{
			int temp;
			cin>>temp;
			arr[temp]++;
		}
		int ans = 10000;
		for (int i=1; i<=2000; i++)
		{
			int total = 0;
			for (int j = i+1; j<=2000; j++)
			{
				if (j%i == 0)
					total += arr[j] * (j/i - 1);
				else
					total += arr[j] * (j/i);
			}
			ans = min(ans,total + i);
		}
		cout<<"Case #"<<++p<<": "<<ans<<endl;
	}
	return 0;
}