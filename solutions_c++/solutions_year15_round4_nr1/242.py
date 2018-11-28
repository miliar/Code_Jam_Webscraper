#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:256000000")
#define _USE_MATH_DEFINES
#include<iostream>
#include<vector>
#include<string>
#include<stack>
#include<algorithm>
#include<cmath>
#include<set>
#include<queue>
#include<sstream>
#include<utility>
#include<map>
#include<ctime>
#include<cstdio>
#include<cassert>
#include<functional>




using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
typedef pair<char, char> pcc;
typedef pair<double, double> pdd;

#define show(x) cerr << x
#define debug(x) show(#x << ": " << (x) << endl)

const long double PI = 3.14159265358979323846;
const long double gammama = 0.57721566490153286060;
const long double eps = 1e-5;
const int INF = 100;
const ll LINF = (ll)1000 * 1000 * 1000 * 1000 * 1000 * 1000;
const ll mod = 1000 * 1000 * 1000 + 7;
const ll N = 1001;
//const int M = 10000000;




ll solve() {
    int r, c;
    cin >> r >> c;
    vector<string> a(r);
    for (int i = 0; i < r; ++i)
        cin >> a[i];
    vector<vector<vector<int> > > ok(r, vector<vector<int> >(c, vector<int>(4, 1)));
    for (int i = 0; i < c; ++i) {
        int j = 0;
        while ((j < r) && (a[j][i] == '.'))
            ++j;
        if (j == r)
            continue;
        ok[j][i][0] = 0;
    }
    for (int i = 0; i < c; ++i) {
        int j = r - 1;
        while ((j >= 0) && (a[j][i] == '.'))
            --j;
        if (j == -1)
            continue;
        ok[j][i][2] = 0;
    }
    for (int i = 0; i < r; ++i) {
        int j = 0;
        while ((j < c) && (a[i][j] == '.'))
            ++j;
        if (j == c)
            continue;
        ok[i][j][3] = 0;
    }
    for (int i = 0; i < r; ++i) {
        int j = c - 1;
        while ((j >= 0) && (a[i][j] == '.'))
            --j;
        if (j == -1)
            continue;
        ok[i][j][1] = 0;
    }
    int res = 0;
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            if (a[i][j] == '.')
                continue;
            if (a[i][j] == '^') {
                if (ok[i][j][0])
                    continue;
            }
            if (a[i][j] == '>') {
                if (ok[i][j][1])
                    continue;
            }
            if (a[i][j] == 'v') {
                if (ok[i][j][2])
                    continue;
            }
            if (a[i][j] == '<') {
                if (ok[i][j][3])
                    continue;
            }
            if (ok[i][j][0] || ok[i][j][1] || ok[i][j][2] || ok[i][j][3])
                ++res;
            else
                return -1;
        }
    }
    return res;

}

void solveAns() {
    ll res = solve();
    if (res < 0)
        cout << "IMPOSSIBLE" << endl;
    else
        cout << res << endl;
}




int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt;
	
	cin >> tt;
	for (int i = 0; i < tt; ++i) {
        cout << "Case #" << i + 1 << ": ";
        solveAns();
        std::cerr << i << endl;
	}
	return 0;
}
