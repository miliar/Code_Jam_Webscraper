#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;

#define pb push_back
#define pp pop_back
#define f first
#define s second
#define mp make_pair
#define sz(a) int((a).size())
#define fname "."

const int N = (int)1e5 + 123;
const double eps = 1e-6;
const int inf = (int)1e9 + 123;

using namespace std;

int t;
int n;
string s;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> t;
	for (int test = 1; test <= t; test++) {
		cin >> n >> s;
		int ans = 0, cnt = 0;
		for (int i = 0; i <= n; i++) {
			if (cnt < i) {
				ans += i - cnt;
				cnt = i;
			}
			cnt += s[i] - '0';
		}
		cout << "Case #" << test << ": " << ans << endl;
	}
	return 0;
}
