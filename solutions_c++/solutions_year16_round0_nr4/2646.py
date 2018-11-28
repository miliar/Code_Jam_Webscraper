#include <bits/stdc++.h>
using namespace std;
#define max(a,b) ((a) > (b) ? (a) : (b))
#define min(a,b) ((a) < (b) ? (a) : (b))
#define abs(x) ((x) < 0 ? -(x) : (x))


int t;
int k,c,s;
int main()
{
	cin.sync_with_stdio(0);
	cin.tie(0);
	cin >> t;
	for (int tcs=1;tcs<=t;++tcs) {
		cin >> k >> c >> s;
		cout << "Case #" << tcs << ":";
		for (int i=1;i<=k;++i) cout << ' ' << i;
		cout << '\n';
	}
	return 0;
}

