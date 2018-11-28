#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <iomanip>
#include <queue>
#include <utility>
#include <stack>
#include <ctime>

#define pb push_back
#define mp make_pair
#define x first
#define y second
#define forn(i,n) for (i = 0; i < n; i++)

using namespace std;

typedef pair <int, int> pii;
typedef long double ld;
typedef long long ll;

const ld EPS = 1e-9;
const int INF = (int) 1e9;
const int N = (int) 1e3 + 5;
const ll M = (int) 1e9 + 7;



int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int k, c, s;
        cin >> k >> c >> s;
        cout << "Case #" << t + 1 << ": ";
        for (int i = 0; i < s; i++)
            cout << i + 1 << ' ';
        cout << endl;

    }
	return 0;
}
