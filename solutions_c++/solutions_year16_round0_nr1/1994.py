#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <cassert>
#include <cstdlib>
#include <string>
#include <cstdio>
#include <vector>
#include <ctime>
#include <queue>
#include <set>
#include <map>
using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define fore(i, b, e) for (int i = (int)(b); i <= (int)(e); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define all(x) (x).begin(), (x).end()
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long i64;
typedef unsigned long long u64;

int main() {
#ifdef HOME
//     freopen("a.in", "r", stdin);
#endif

    int t;
    cin >> t;
    fore(tn, 1, t) {
        int n;
        cin >> n;
        int b[10] = {0};
        bool done = false;
        forn(i, 1000) {
            int x = n * i;
            while (x) {
                b[x%10] = 1;
                x /= 10;
            }
            if (count(b, b+10, 1) == 10) {
                cout << "Case #" << tn << ": " << n*i << endl;
                done = true;
                break;
            }
        }
        if (!done) {
            cout << "Case #" << tn << ": INSOMNIA" << endl;
        }
    }


#ifdef HOME
    cerr << "Time elapsed: " << clock() / 1000 << " ms" << endl;
#endif
    return 0;
}
