#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <algorithm>
#include <iomanip>
#include <complex>
#include <valarray>
#include <unordered_map>
#include <unordered_set>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
#define rep(i,s,e) for (int i=(s);i<(e);++i)
#define pb push_back
#define mk make_pair
#define fst first
#define snd second
#define all(x) (x).begin(),(x).end()
#define clr(x,y) memset(x,y,sizeof x)
#define contains(x,y) (x).find(y)!=(x).end()
#define endl "\n"

int dx[]={0,0,1,-1,1,-1,1,-1}, dy[]={-1,1,0,0,1,-1,-1,1};
const int mod = 1e9+7;

int main() {
	ios::sync_with_stdio(0);
	cout << fixed << setprecision(16);

	int t;
	cin >> t;
	for (int ti = 1; ti <= t; ti++) {
		cout << "Case #" << ti << ": ";
		int n;
		cin >> n;
		vector<string> s(n);
		vector<string::iterator> it(n);
		vector<int> count(n);
		rep (i,0,n) {
			cin >> s[i];
			it[i] = s[i].begin();
			count[i] = 0;
		}
		int res = 0;
		while (it[0] != s[0].end()) {
			char c = *it[0];
			int sum = 0;
			rep (i,0,n) {
				count[i] = 0;
				while (it[i] != s[i].end() && *it[i] == c) it[i]++, count[i]++;
				if (!count[i]) goto nope;
				sum += count[i];
			}
			int opt = int(round(sum / (float)n));
			//cout << opt << endl;
			rep(i,0,n) res += abs(opt - count[i]);
		}
		rep(i,0,n)
			if (it[i] != s[i].end()) {
				goto nope;
			}
		cout << res << endl;
		continue;
nope: cout << "Fegla Won" << endl;
	}
}
