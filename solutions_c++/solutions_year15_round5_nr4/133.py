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

vector <pair <int, int> > gen(vector <int> a) {
	vector <int> b;
	for (int mask = 0; mask < (1 << a.size()); ++mask) {
		int sum = 0;
		for (int j = 0; j < a.size(); ++j) {
			if ((1 << j) & mask) {
				sum += a[j];
			}
		}
		b.push_back(sum);
	}
	sort(b.begin(), b.end());

	vector <pair <int, int> > res;

	for (int i = 0; i < b.size(); ) {
		int j = i;
		while (j < b.size() && b[j] == b[i]) {
			++j;
		}
		res.push_back(mp(j - i, b[i]));
		i = j;
	}

	return res;
}

void solve() {
	int P;
	cin >> P;
	vector <int> a(P), b(P);

	for (int i = 0; i < P; ++i) {
		cin >> a[i];
	}
	
	int summ = 0;

	for (int i = 0; i < P; ++i) {
		
		cin >> b[i];
		summ += b[i];
	}

	vector <int> ans;

	while ((1 << ans.size()) != summ ) {
		auto tmp = gen(ans);
		for (int j = 0; j < a.size(); ++j) {
			if (j >= tmp.size() || tmp[j].second > a[j] ||  tmp[j].first < b[j]) {
				ans.push_back(a[j]);
				break;
			}
		}
	}

	for (int i = 0; i < ans.size(); ++i) {
		cout << ans[i] << " ";
	}
	cout << endl;
}