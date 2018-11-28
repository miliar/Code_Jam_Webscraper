#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pi;

#define MP make_pair
#define PB push_back
#define F first
#define S second
#define MOD 1000000007
#define INF (1 << 30)

int main()
{
    ios :: sync_with_stdio(false);
    cin.tie(0);
    freopen("large2.in", "r", stdin);
	freopen("large2out.txt", "w", stdout);
	int t, i, j, n, cases = 0;
	string s;
	cin >> t;
	while(t--)
	{
		cases++;
		cin >> s;
		n = s.length();
		int ans = 0;
		for(i = n - 1; i >= 0; i--)
		{
			if(s[i] == '-')
			{
				while(i - 1 >= 0 && s[i - 1] == '-')
					i--;
				if(i > 0)
					ans += 2;
				else
					ans++;
			}
		}
		cout << "Case #" << cases << ": " << ans << endl;
	}
    return 0;
}

