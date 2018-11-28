#include <bits/stdc++.h>

using namespace std;

bool check(bool *arr)
{
	for (int i = 0; i < 10; ++i)
	{
		if(arr[i] != 1)
			return false;
	}
	return true;
}
int k = 1;
void solve()
{
	int n;
	cin>>n;

	if(n == 0)
	{
		cout<<"Case #"<<k<<": "<<"INSOMNIA\n";
		k++;
	}
	else
	{
		bool arr[10];
		memset(arr, 0, sizeof(bool) * 10);
		int i;
		for (i =1;; ++i)
		{
			if(check(arr))
			{
				break;
			}
			
			string s = to_string(n * i);
			for (int j = 0; j < s.length(); ++j)
			{
				arr[s[j] - '0'] = 1;
			}
			/*
			cout<<n * i<<endl;
			for (int j = 0; j < 10; ++j)
			{
				cout<<arr[j]<<" ";
			}
			cout<<endl;
			*/
		}
		cout<<"Case #"<<k<<": "<<n * (i-1)<<endl;
		k++;
	}
}

int main()
{
	int t;
	cin>>t;
	while(t--)
		solve();
	return 0;
}