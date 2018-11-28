#include <iostream>
#include <iomanip>
#include <string>

#define REP(i,n) for(int i = 0; i < (n); i++)
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)
#include <algorithm>
#include <map>
#include <vector>
#include <set>

using namespace std;

typedef pair<double, double> pdd;
const double eps = 1e-6;
#define R second
#define C first

const int MAX = 4005;

int vals[MAX];
int ind;
map<string, int> m;

void readLine(vector<int> &v) {
	cin.ignore();
	while (cin.peek() != '\n' && cin.peek() != '\r') {
		string s;
		cin >> s;
		if (m.find(s) == m.end()) {
			m[s] = ind++;
		}
		v.push_back(m[s]);
	}
}

void add(vector<int> &v, int val) {
	for (auto i : v) vals[i] |= val;
}

int solve() {
	int n;
	cin >> n;
	n -= 2;
	ind = 0;
	m.clear();
	vector<int> en, fr, vs[200];
	readLine(en);
	readLine(fr);
	int res = 1000000;
	REP(i, n) readLine(vs[i]);
	REP(ii, 1 << n) {
		REP(i, ind) vals[i] = 0;
		add(en, 1);
		add(fr, 2);
		REP(i, n) {
			add(vs[i], (ii & (1 << i)) == 0 ? 1 : 2);
		}
		int tmp = 0;
		REP(i, ind) {
			tmp += vals[i] == 3;
		}
		res = min(res, tmp);
	}
	return res;
}

int main() {
	int t;
	cin >> t;
	REP(i, t) {
		cout << "Case #" << i + 1 << ": ";
		auto s = solve();
		cout << s;
		cout << endl;
	}
}