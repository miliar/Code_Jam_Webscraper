#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz(a) (int)a.size()
#define sqr(x) ((x)*(x))
#define ms(a, x) memset(a, x, sizeof a)
#define all(a) a.begin(), a.end()
#define forit(it, s) for (__typeof(s.begin()) it = s.begin(); it != s.end(); it++)

typedef long long ll;
typedef vector<int> vi;
typedef pair<ll,int> pii;

const int N = 1<<17;
const int inf = 1<<30;

void solve(int test) {
	string s;
	cin >> s;
	string t = "";
	for (int i = 0; i < sz(s); i++)
		if (i == 0 || s[i] >= t[0])
			t = s[i] + t;
		else
			t += s[i];
	printf("Case #%d: ", test);
	cout << t << endl;
}

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int tests;
	scanf("%d", &tests);
	for (int t = 1; t <= tests; t++) {
		solve(t);
	}


	return 0;
}