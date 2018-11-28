#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:128000000")
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

 
using namespace std; 
 
typedef long long ll; 
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
const long double PI = 3.14159265358979323846;  
const long double gammama = 0.57721566490153286060;
//const long double eps = 1e-5;
//const int INF = 50000;
//const int N = 1000 * 1000 * 1000 + 10;
bool par(const vector<vector<int> >& ed) {
    int n = ed.size();
    vector<int> g(n, 0);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (ed[i][j])
                g[i] = g[i] | (1 << j);
        }
    }
    int m = 1 << n;
    vector<int> shadow(m);
    for (int i = 0; i < m; ++i) {
        int sh = 0;
        for (int j = 0; j < n; ++j) {
            if (((i >> j) & 1) == 0)
                continue;
            sh = sh | g[j];
        }
        shadow[i] = __popcnt(sh);
    }
    vector<int> ok(m, 1);
    for (int i = 0; i < m; ++i) {
        if (__popcnt(i) > shadow[i]) {
            ok[i] = 0;
            for (int j = 0; j < m; ++j) {
                if (i | j == j)
                    ok[j] = 0;
            }
        }
    }
    return ok[m - 1];
}

bool par(const vector<vector<int> >& ed, int m1, int m2) {
    int sz1 = __popcnt(m1);
    int sz2 = __popcnt(m2);
    if (sz1 != sz2)
        return 0;
    vector<vector<int> > a(sz1, vector<int>(sz1, 0));
    vector<int> ind1, ind2;
    for (int i = 0; i < 4; ++i)
        if ((m1 >> i) & 1)
            ind1.push_back(i);

    for (int i = 0; i < 4; ++i)
        if ((m2 >> i) & 1)
            ind2.push_back(i);
    for (int i = 0; i < ind1.size(); ++i) {
        for (int j = 0; j < ind2.size(); ++j) {
            a[i][j] = ed[ind1[i]][ind2[j]];
        }
    }
    return par(a);
}

bool isGood(const vector<vector<int> >& ed) {
    int n = ed.size();
    int m = 1 << n;
    for (int m1 = 0; m1 < m; ++m1) {
        for (int m2 = 0; m2 < m; ++m2) {
            if (par(ed, m1, m2) != par(ed, m - m1 - 1, m - m2 - 1))
                return 0;
        }
    }
    return 1;
}

void solve() {
    int n;
    cin >> n;
    vector<string> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    vector < vector<int> > ed(n, vector<int>(n));
    vector<pii> b;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            ed[i][j] = a[i][j] - '0';
            if (ed[i][j] == 0)
                b.push_back(pii(i, j));
        }
    }
    int sz = b.size();
    int m = 1 << sz;
    int res = 1000;
    vector<vector<int> > newEd(n, vector<int>(n));
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j)
            for (int k = 0; k < n; ++k)
                newEd[j][k] = ed[j][k];
        for (int j = 0; j < sz; ++j) {
            if ((i >> j) & 1)
                newEd[b[j].first][b[j].second] = 1;
        }
        if (isGood(newEd))
            res = min(res, (int)__popcnt(i));
    }
    cout << res << endl;
}

int main() {
    //freopen("D-small.txt", "r", stdin);
    //freopen("D-large.txt", "r", stdin);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt;
	//scanf("%d\n", &tt);
	cin >> tt;
	for (int i = 0; i < tt; ++i) {
        cout << "Case #" << i + 1 << ": ";
        solve();
		std::cerr << i << endl;
	}
	return 0;
}