#include <bits/stdc++.h>

using namespace std;

void solve(int testnum)
{
    int n;
    cin >> n;
    string s;
    cin >> s;

    int ans = 0;
    int predsum = 0;
    for (int i = 0; i <= n; i++) {
	if (predsum < i) {
	    ans = max(ans, i - predsum);
	}
	predsum += s[i] - '0';
    }

    cout << "Case #" << testnum + 1 << ": " << ans << "\n";
}

int main()
{
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for (int q = 0; q < t; q++) {
	solve(q);
    }
}
