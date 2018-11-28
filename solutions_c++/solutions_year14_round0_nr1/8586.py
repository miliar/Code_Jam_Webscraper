#include <algorithm>
#include <bitset>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <ctime>

using namespace std;

#define rep(a, b, e) for(int a = (int) b; a < (int) e; ++a)
#define clr(a, val) memset(a, val, sizeof(a))
#define debug(a) cerr << #a << ": " << a << endl;
#define debugv(b, t) cerr << #b << ":\n"; rep(countvec, 0, t) { cerr << b[countvec] << '\t'; } cerr << endl;
#define debugm(c, t, u) cerr << #c << ":\n"; rep(countmat, 0, t) { rep(countbb, 0, u) { cerr << c[countmat][countbb] << '\t'; } cerr << endl; }
string tos(int a) { ostringstream os(""); os << a; return os.str(); }
#define SIZE(x) int((x).size())


int T;

void solve(int tc) {
	int N[16] = {}, M[4][4], op;
	cin >> op; --op;
	rep(i, 0, 4) rep(j, 0, 4) cin >> M[i][j];
	rep(i, 0, 4) ++N[ M[op][i] - 1 ];
	cin >> op; --op;
	rep(i, 0, 4) rep(j, 0, 4) cin >> M[i][j];
	rep(i, 0, 4) ++N[ M[op][i] - 1 ];
	vector<int> ans;
	rep(i, 0, 16) if(N[i] == 2) ans.push_back(i + 1);
	cout << "Case #" << tc << ": ";
	if(ans.empty()) cout << "Volunteer cheated!";
	else if(SIZE(ans) > 1) cout << "Bad magician!";
	else cout << ans[0];
	cout << endl;
}

int main() {
	#ifndef ONLINE_JUDGE
		freopen("D:/in.txt","r",stdin);
		freopen("D:/out.txt","w",stdout);
		clock_t start = clock();
	#endif
	
	cin >> T;
	rep(tc, 1, T + 1)
		solve(tc);
	
	#ifndef ONLINE_JUDGE
		fprintf(stderr, "\ntime=%.3lfsec\n", 0.001 * (clock() - start));
	#endif 
	return 0;
}
