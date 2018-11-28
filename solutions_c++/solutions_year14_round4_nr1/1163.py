#include<iostream>
#include<algorithm>
#include<string.h>
#include<vector>
#include<iomanip>
using namespace std;

#define MAXN 10005
int arr[MAXN];

int main()
{
	freopen("d:\\1.in", "r", stdin);
	freopen("d:\\1-ans.txt", "w", stdout);

	int T;
	cin>>T;
	for(int kase = 1; kase <= T; ++kase)
	{
		int n, k;
		cin>>n>>k;
		for(int i = 0; i < n; ++i)
			cin>>arr[i];
		sort(arr, arr+n);
		int first = 0, last = n-1;
		int ans = 0;
		while(first <= last)
		{
			ans++;
			if(first == last)
				break;
			if(arr[first] + arr[last] <= k)
			{
				first++;
				last--;
			}
			else
			{
				last--;
			}
		}
		cout<<"Case #"<<kase<<": "<<ans<<endl;
	}
	return 0;
}
