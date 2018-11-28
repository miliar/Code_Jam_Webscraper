#include <iostream> 
#include <cstdio> 
#include <set> 
#include <map> 
#include <vector> 
#include <queue> 
#include <stack> 
#include <cmath> 
#include <algorithm> 
#include <cstring> 
#include <bitset> 
#include <ctime> 
#include <sstream>
#include <stack> 
#include <cassert> 
#include <list> 
#include <deque>
//#include <unordered_set> 
using namespace std;
typedef long long li;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pi;

#define mp make_pair 
#define pb push_back 
#define all(s) s.begin(), s.end() 
void solve();

#define NAME "changemeplease"
int main() {
#ifdef YA 
	//cerr << NAME << endl;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout); 
	clock_t start = clock();
#else 
	//freopen("input.txt", "r", stdin); 
	//freopen("output.txt", "w", stdout); 
#endif 
	ios_base::sync_with_stdio(false);
	cout << fixed;
	cout.precision(10);
	int t = 1;
	cin >> t;	 
	for (int i = 1; i <= t; ++i) {
		cerr << i << endl;
		cout << "Case #" << i << ": ";
		solve();
	}
#ifdef YA 
	//cout << "\n\n\nTime:" << ((clock() - start) / 1.0 / CLOCKS_PER_SEC);
#endif 
	return 0;
}

int m, n;
vector <string> a;
vector <vector <int> > b;

int mx = 0;
int k = 0;

struct vert {
	char go[27];
	vert() {
		memset(go, 255, sizeof(go));
	}
};

vector <vert> tr;

int build(int pos) {
	tr.clear();
	tr.resize(1);
	for (int i = 0; i < b[pos].size(); ++i) {
		int cur = 0;
		for (int j = 0; j < a[b[pos][i]].size(); ++j) {
			char c = a[b[pos][i]][j];
			if (tr[cur].go[c - 'A'] == -1) {
				tr[cur].go[c - 'A'] = tr.size();
				tr.push_back(vert());
			}
			cur = tr[cur].go[c - 'A'];
		}
	}
	return tr.size();
}

void per(int pos) {
	if (pos == a.size()) {
		for (int i = 0; i < b.size(); ++i) {
			if (b[i].empty())
				return;
		}
		int sum = 0;
		for (int i = 0; i < b.size(); ++i) {
			sum += build(i);
		}
		if (sum > mx) {
			mx = sum;
			k = 0;
		}
		if (sum == mx) {
			++k;
		}
		return;
	}
	for (int i = 0; i < b.size(); ++i) {
		b[i].push_back(pos);
		per(pos + 1);
		b[i].pop_back();
	}
}

void solve() {
	mx = 0;
	k = 0;
	cin >> m >> n;
	a.resize(m);
	b.resize(n);
	for (int i = 0; i < m; ++i) {
		cin >> a[i];
	}
	per(0);
	cout << mx << " " << k << endl;
}