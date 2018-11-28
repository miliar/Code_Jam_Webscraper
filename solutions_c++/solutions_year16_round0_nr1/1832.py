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

void calc_nums(int n, vector <int> &v) {
    while (n) {
        v[n % 10] = 1;
        n /= 10;
    }
}

bool all_numbers(vector <int> &v) {
    for (int i = 0; i < 10; i++)
        if (!v[i])
            return 0;
    return 1;
}

int solve(int n) {
    int n2 = n;
    vector <int> v(10, 0);
    calc_nums(n, v);
    while (!all_numbers(v)) {
        n += n2;
        calc_nums(n, v);
    }
    return n;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int n;
        cin >> n;
        cout << "Case #" << t + 1 << ": ";
        if (n)
            cout << solve(n) << endl;
        else
            cout << "INSOMNIA\n";
    }
	return 0;
}
