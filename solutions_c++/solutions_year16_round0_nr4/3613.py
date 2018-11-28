#include <bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define pii pair<int, int>
#define pll pair<ll, ll>
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define pi 3.14159265
#define si(x) scanf("%d", &x)
#define sl(x) scanf("%lld", &x)
#define MEM(x, y) memset(x, y, sizeof(x))
using namespace std;

int main() {
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tc;
	cin >> tc;
	for (int t = 1; t <= tc; t++) {
		cout << "Case #" << t << ": ";
		ll k, c, s, temp = 1;
		cin >> k >> c >> s;
		
		temp = 1;
		for (int i = 0; i < c; i++)
			temp = temp * k;
		
		ll div = temp / k, ans = 1;
		for (int i = 0; i < s; i++) {
			cout << ans << " ";
			ans += div;
		}
		cout << endl;
	}
	return 0;
}