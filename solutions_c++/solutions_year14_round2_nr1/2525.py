#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 
#define FOR(i,a,b) for(__typeof(b) i=(a);i!=(b);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) a.begin(),a.end()
#define EACH(i,a) FOR(i,a.begin(),a.end())
#define PB push_back
#define iss istringstream
#define SZ(a) (int)a.size()
#define CLEAR(a) memset(a,0,sizeof(a))
#define ll long long

const int MAXN = 105;
int T;
int N;
string mem[MAXN];
vector<int> dp[MAXN];
vector<char> check;

inline void parse(string s, vector<int> &num, vector<char> &c) {
	char last = s[0];
	int ct = 1;
	for(int i = 1 ; i < (int)s.size() ; i++) {
		if (s[i] == last) {
			ct++;
		}	else {
			c.push_back(last);
			num.push_back(ct);
			ct = 1;
			last = s[i];
		}
	}
	c.push_back(last);
	num.push_back(ct);
}

int main() {
	cin >> T;
	for(int t = 1 ; t <= T ; t++) {
		cin >> N;
		bool good = true;
		int ans = 0;

		for(int i = 0 ; i < N ; i++) {
			cin >> mem[i];
			vector<int> a;
			vector<char> b;
			parse(mem[i], a, b);
			if (i == 0) {
				check = b;
			}	else {
				if (SZ(check) != SZ(b)) {
					good = false;
					break;
				}
				REP(j, SZ(b)) {
					if (b[j] != check[j]) {
						good = false;
						break;
					}
				}
			}
			dp[i] = a;
		}

		if (good) {
			int M = SZ(dp[0]);
			for(int i = 0 ; i < M ; i++) {
				vector<int> v;
				for(int j = 0 ; j < N ; j++) {
					v.push_back(dp[j][i]);
				}
				sort(ALL(v));
				for(int j = 0 ; j < N - 1 - j ; j++) {
					ans += (v[N - 1 - j] - v[0]);
				}
			}
			printf("Case #%d: %d\n", t, ans);
		}	else {
			printf("Case #%d: Fegla Won\n", t);
		}
	}
	return 0;
}
