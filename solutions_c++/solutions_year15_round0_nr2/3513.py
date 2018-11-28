#include<bits/stdc++.h>

using namespace std;

#define pb push_back
#define mem(a, b) memset(a, b, sizeof(a))
#define mp make_pair

const int oo = (int)1e9;
const double PI = 2 * acos(0.0);
const double eps = 1e-9;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t;
	cin >> t;
	for(int c=1;c<=t;c++)
	{
		int n,arr[1005],maxi=0,ans = (1<<30);
		cin >> n;
		for(int i=0;i<n;i++)
		{
			cin >> arr[i];
			maxi = max(maxi,arr[i]);
		}
		for(int i=1;i<=maxi;i++)
		{
			int res = 0;
			for(int j=0;j<n;j++)
			{
				if(arr[j] > i)
				{
					res += (arr[j]-1)/i;
				}
			}
			ans = min(res+i,ans);
		}
		cout << "Case #" << c << ": " << min(ans,maxi) << endl;
	}
	return 0;
}
