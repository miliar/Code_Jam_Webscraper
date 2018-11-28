#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pi;

#define MP make_pair
#define PB push_back
#define F first
#define S second
#define MOD 1000000007

int main()
{
	ios::sync_with_stdio(false);
	freopen("output3.txt", "w", stdout);
	freopen("B-large.in", "r", stdin);
	int t, n, i, j, maxi;
	int cases = 0;
	cin >> t;
	while(t--)
	{
		cases++;
		cin >> n;
		int a[n];
		maxi = 0;
		for(i = 0; i < n; i++)
		{
			cin >> a[i];
			maxi = max(maxi, a[i]);
		}
		int mini = 1e9;
		for(i = 1; i <= maxi; i++)
		{
			int steps = 0;
			for(j = 0; j < n; j++)
			{
				if(a[j] > i)
				{
					int temp = a[j] - i;
					steps += (temp/i);
					steps += (temp%i)?1:0;
				}
			}
			steps += i;
			mini = min(mini, steps);
		}
		cout << "Case #" << cases << ": " << mini << endl;
	}
	return 0;
}

