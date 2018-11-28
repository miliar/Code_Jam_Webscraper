#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <bitset>
#include <cstdio>
#include <queue>

using namespace std;

void precalc () {

}

int real(multiset<double> a, multiset<double> b) {
    int res = 0;
    while (!a.empty()) {
        double x = *a.begin();
        a.erase(a.begin());

        multiset<double>::const_iterator it = b.upper_bound(x);
        if (it == b.end()) {
            b.erase(b.begin());
            res++;
        } else {
            b.erase(it);
        }
    }
    return res;
}

int cheat(multiset<double> a, multiset<double> b) {
    int res = 0;
    while (!a.empty()) {
        double x = *a.begin();
        a.erase(a.begin());

        multiset<double>::const_iterator it = b.begin();
        if (x > *it) {
            b.erase(it);
            ++res;
        } else {
            b.erase(*b.rbegin());
        }
    }
    return res;
}

void solve () {
    int n;
    cin >> n;

    multiset<double> a, b;
    for (int i = 0; i < n; ++i) {
        double t;
        cin >> t;
        a.insert(t);
    }
    for (int i = 0; i < n; ++i) {
        double t;
        cin >> t;
        b.insert(t);
    }

    cout << cheat(a, b) << " " << real(a, b) << endl;
}

int main() {
	freopen("D-large.in","r",stdin);
	freopen("output.txt","w",stdout);

  precalc();

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		cout << "Case #" << test << ": ";
    
    solve();
	}
	return 0;
}
