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

vector<pii > arr;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	string s;
	cin >> tc;
	for (int t = 1; t <= tc; t++) {
		cin >> s;
		cout << "Case #" << t << ": ";
		arr.clear();
		int ans = 0;
		
		pii temp;
		for (int i = 0; i < s.size(); i++) {
			if (s[i] == '-') {
				temp.f = i;
				while (s[i] == '-' && i < s.size()) {
					i++;
				}
				temp.s = i - 1;
				arr.pb(temp);
			}
		}
		
		for (int i = 0; i < arr.size(); i++) {
			ans += 2;
			if (arr[i].f == 0)
				ans--;
		}
		cout << ans << endl;
	}

	return 0;
}