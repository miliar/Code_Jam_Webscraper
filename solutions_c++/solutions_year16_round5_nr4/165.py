#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include <queue>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

#define INF 1000000000
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define FORC(cont, it) for(typeof((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;

#define maxN 100

string good[maxN], bad;

int main() {
	int T, caso=1, N, L;
	cin >> T;
	while (T--) {
		cin >> N >> L;
		FOR(i, 0, N) {
			cin >> good[i];
		}
		cin >> bad;
		bool imp = false;
		FOR(i, 0, N) if (good[i] == bad) imp = true;
		cout << "Case #" << caso++ << ": ";
		string a1 = "10?", a2 = "";
		FOR(i, 1, L) {
			a1 += "01";
			a2 += '?';
		}
		if (L == 1) {
			if(bad[0]=='0') a2 = "1";
			else a2 = "0";
		}
		if (a1.length() + a2.length() >= 200) {
			imp = imp;
		}
		if (imp) cout << "IMPOSSIBLE" << endl;
		else cout <<a1<<" "<<a2<< endl;
	}
	return 0;
}
