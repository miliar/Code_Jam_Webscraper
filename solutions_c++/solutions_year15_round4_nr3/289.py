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
    
	char olol[20];
	gets(olol);
	//cin >> t;
	t = atoi(olol);

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

const int HASH = 997;

int gethash(const string & s) {
	int res = 0;
	for (int i = 0; i < s.size(); ++i) {
		res = res * HASH + int(s[i]);
	}
	return res;
}

void solve() {
	int n;
	//cin >> n;
	char olo[20];
	gets(olo);
	n = atoi(olo);

	vector <vector <int> > hashes(n);
	vector <int> allh;

	for (int i = 0; i < n; ++i) {
		string s;
		getline(cin, s);
		istringstream in(s);
		string tmp;
		while (in >> tmp) {
			int vv = gethash(tmp);
			hashes[i].push_back(vv);
			allh.push_back(vv);
		}
	}

	sort(allh.begin(), allh.end());
	allh.erase(unique(allh.begin(), allh.end()), allh.end());

	vector <vector <int> > a(n);

	for (int i = 0; i < hashes.size(); ++i) {
		for (int j = 0; j < hashes[i].size(); ++j) 
		{
			a[i].push_back(lower_bound(allh.begin(), allh.end(), hashes[i][j]) - allh.begin());		
		}
		sort(a[i].begin(), a[i].end());
		a[i].erase(unique(a[i].begin(), a[i].end()), a[i].end());
	}

	int ans = -1;

	for (int mask = 0; mask < (1 << n); ++mask) {
		if (mask & 1) {
			continue;
		}
		if (!(mask & 2)) {
			continue;
		}

		vector <int> ress(allh.size());

		for (int i = 0; i < n; ++i) {
			int add;
			if ((1 << i) & mask) {
				add = 1;
			}
			else {
				add = 2;
			}
			for (int j = 0; j < a[i].size(); ++j) {
				ress[a[i][j]] |= add;
			}
		}

		int cur = 0;
		for (int i = 0; i < ress.size(); ++i) {
			if (ress[i] == 3) {
				++cur;
			}
		}

		if (ans == -1 || cur < ans) {
			ans = cur;
		}
	}

	cout << ans << "\n";
}