#pragma comment (linker, "/STACK:128000000")
#include <iostream> 
#include <cstdio> 
#include <fstream>
#include <functional>
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

using namespace std;

#define mp make_pair
#define pb push_back

typedef long long li;
typedef long long i64;
typedef pair <int, int> pi;
typedef vector <int> vi;
typedef double ld;
typedef vector<int> vi;
typedef pair <int, int> pi;

void solve();

//int timer = 0;
#define FILENAME ""

int main() {
    string s = FILENAME;
#ifdef YA
    //assert(!s.empty());
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //cerr<<FILENAME<<endl;
    //assert (s != "change me please");
    clock_t start = clock();
#else
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    //freopen(FILENAME ".in", "r", stdin);
    //freopen(FILENAME ".out", "w", stdout); 
    cin.tie(0);
#endif
    cout.sync_with_stdio(0);
    cout.precision(10);
    cout << fixed;
    int t = 1;
    
	cin >> t;
    for (int i = 1; i <= t; ++i) {
        //++timer;
		cout << "Case #" << i << ": ";
        solve();
    }
#ifdef YA
    cerr << "\n\n\n" << (clock() - start) / 1.0 / CLOCKS_PER_SEC << "\n\n\n";
#endif
    return 0;
}


map <int, int> used;

int r, c, w;

bool corr(const vector <int>& t) {
	bool f = false;
	for (int i = 0; i < t.size(); ++i) {
		if (t[i] == 2) {
			f = true;
		}
	}

	if (!f) {
		for (int i = 0; i < t.size(); ) {
			if (t[i] == 1) {
				++i;
				continue;
			}
			int j = i;
			while (j < t.size() && t[j] == 0) {
				++j;
			}
			if (j - i >= w) {
				return true;
			}
			i = j;
		}
		return false;
	}

	int left = 0;
	int right;
	for (left = 0; t[left] != 2; ++left);
	for (right = t.size() - 1; t[right] != 2; --right);

	for (int j = left; j <= right; ++j) {
		if (t[j] == 1) {
			return false;
		}
	}


	while (left >= 0 && t[left] != 1) {
		--left;
	}
	++left;

	int sum = 0;
	while (left < t.size() && t[left] != 1) {
		++sum;
		++left;
	}
	return sum >= w;
}

int proc(vector <int> state) {
	int x = 0;
	for (int i = 0; i < state.size(); ++i) {
		x = x * 3 + state[i];
	}
	if (used.find(x) != used.end()) {
		return used[x];
	}

	int& res = used[x];
	
	int sum = 0;
	for (int i = 0; i < state.size(); ++i) {
		if (state[i] == 2) {
			++sum;
		}
	}
	if (sum == w) {
		return res = 0;
	}

	res = -1;
	for (int i = 0; i < state.size(); ++i) {
		if (state[i] == 0) {
			int tmp[2];
			tmp[0] = tmp[1] = -1;

			for (int j = 1; j <= 2; ++j) {
				state[i] = j;
				if (corr(state)) {
					tmp[j - 1] = proc(state) + 1;
				}
			}

			if (tmp[0] != -1 || tmp[1] != -1) {
				int x = max(tmp[0], tmp[1]);
				if (res == -1 || res > x) {
					res = x;
				}
			}
			state[i] = 0;
		}
	}

	return res;
}

void solve() {
	used.clear();

	cin >> r >> c >> w;
	vector <int> cur;
	vector <int> start(c, 0);

	cout << proc(start) << "\n";
}