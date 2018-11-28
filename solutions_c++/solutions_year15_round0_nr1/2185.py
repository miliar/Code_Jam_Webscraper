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
const int MAX = 1000010;

string s;
int n, T;
char str_template[] = "Case #%d: %d";
char str_answer[sizeof(str_template)];

int main() {
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int testcase = 1; testcase <= T; ++testcase) {
		cin >> n >> s;
		int count = 0;
		int answer = 0;
		for (int i = 0; i < n + 1; ++i) {
			int x = s[i] - '0';
			if (i > count && x > 0) {
				int gap = i - count;
				answer += gap;
				count += gap;
			}
			count += x;
		}
		sprintf(str_answer, str_template, testcase, answer);
		cout << str_answer << endl;
	}
	return 0;
}
