#include <iostream>
#define s(n) scanf("%d", &n)
#include <cstring>
#define fill(a, v) memset(a, v, sizeof a)
typedef long long ll;
const int mxn = 128;
using namespace std;


int nxt[mxn];
string s;
int dp[mxn][2];
int cs;
int n;

int solve(int pos, int up) {
	if (pos >= n) return 0;

	int &d = dp[pos][up];
	if(~d) return d;

	if(s[pos] == '+')
		return d = solve(nxt[pos], 1);
	return d = 1 + up + solve(nxt[pos], 1);
}

int main() {
	int cases, N;
	s(cases);
	while(cases-- > 0) {
		fill(nxt, -1);
		fill(dp, -1);
		cin >> s;
		n = s.size();
		int last = -1;
		for(int i=n-1; i >= 0; i--) {
			nxt[i] = max(last != -1 ? last : n - 1, 0);
			if(s[i]=='-') {
				nxt[i]++;
				continue;
			}
			else {
				if (i == nxt[i])
					nxt[i]++;
			}
			last = max(i-1, 0);
		}
		// for(int i=0;i<n;i++) cout << nxt[i] << " "; cout << endl;
		int ans = solve(0, 0);
		printf("Case #%d: %d\n", ++cs, ans);
	}
	return 0;
}
