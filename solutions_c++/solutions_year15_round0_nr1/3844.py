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
	freopen("output.txt", "w", stdout);
	freopen("A-large.in", "r", stdin);
	int t, x, i, temp;
	int cases = 0;
	int ans, countify;
	cin >> t;
	while(t--)
	{
		cases++;
		string s;
		cin >> x >> s;
		int n = s.length();
		countify = (s[0] - '0');
		ans = 0;
		for(i = 1; i < n; i++)
		{
			if(countify < i)
			{
				temp = i - countify;
				ans += temp;
				countify += temp;
			}
			countify += (s[i] - '0');
		}
		cout << "Case #" << cases << ": " << ans << endl;
	}
	return 0;
}

