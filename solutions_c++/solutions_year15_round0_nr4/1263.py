#include <bits/stdc++.h>
#define ALL(x) x.begin(), x.end()
#define SIZE(x) (int)(x.size())
#define FOR(i, s, e) for (int i = int(s); i < int(e); ++i)
#define FORIT(i, c) for (__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef pair<long long, long long> PLL;
const int MOD = 1000000007;
const int INF = 0x3F3F3F3F;
const int MAX = 1010;

int T;
char str_template[] = "Case #%d: %s";
char str_answer[sizeof(str_template)];

bool answer;

bool brute_force(int x, int r, int c) {
	return (r >= x - 1) && (c >= x - 1);
}

int main() {
	freopen("output.txt", "w", stdout);
	cin >> T;
	for (int testcase = 1; testcase <= T; ++testcase) {
		int x, r, c;
		cin >> x >> r >> c;
		answer = ((r * c % x) == 0);
		answer &= brute_force(x, r, c);

		if (answer) {
			sprintf(str_answer, str_template, testcase, "GABRIEL");
		} else {
			sprintf(str_answer, str_template, testcase, "RICHARD");
		}
		cout << str_answer << endl;
	}
	return 0;
}
