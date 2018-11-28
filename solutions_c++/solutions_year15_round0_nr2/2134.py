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

string s;
int n, T;
char str_template[] = "Case #%d: %d";
char str_answer[sizeof(str_template)];

int p[MAX];
int answer;

int main() {
	freopen("output.txt", "w", stdout);
	cin >> T;
	for (int testcase = 1; testcase <= T; ++testcase) {
		memset(p, 0, sizeof(p));
		cin >> n;
		for (int i = 0; i < n; ++i) {
			cin >> p[i];
		}
		sort(p, p + n);
		answer = p[n - 1];
		int boundary = answer;
		int cost;

		for (int i = 1; i <= boundary; ++i) {
			cost = 0;
			for (int j = n - 1; p[j] > i; --j) {
				cost += p[j] / i;
				if (p[j] % i == 0) {
					--cost;
				}
			}
			answer = min(answer, cost + i);
		}
		sprintf(str_answer, str_template, testcase, answer);
		cout << str_answer << endl;
	}
	return 0;
}
