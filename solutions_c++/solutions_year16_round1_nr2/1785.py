#include <bits/stdc++.h>

using namespace std;

int k = 1;
void solve()
{
	int n;

	cin>>n;
	
	int arr[2501];
	for (int i = 0; i < 2501; ++i)
	{
		arr[i] = 0;
	}

	int temp;
	for (int i = 0; i < 2 * n - 1; ++i)
	{
		for (int j = 0; j < n; ++j)
		{
			cin>>temp;
			arr[temp]++;		
		}
	}
	int count = 0;
	cout<<"Case #"<<k<<": ";
	for (int i = 1; i < 2501; ++i)
	{
		if(arr[i]%2){
			cout<<i<<" ";
			count++;
		}
	}
	cout<<endl;
	k++;
}

int main()
{
	int t;
	cin>>t;
	while(t--)
		solve();
	return 0;
}