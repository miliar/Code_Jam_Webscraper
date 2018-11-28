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
FILE* out;

double getPr(const vector<double>& a) {
    int n = a.size();
    vector<vector<double> > d(n + 1, vector<double>(n + 1, 0));
    d[0][0] = 1;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j <= n; ++j) {
            d[i + 1][j] = d[i][j] * (1 - a[i]);
            if (j > 0)
                d[i + 1][j] += d[i][j - 1] * a[i];
        }
    }
    return d[n][n / 2];
}

void solve() {
    int n, k;
    cin >> n >> k;
    vector<double> p(n);
    for (int i = 0; i < n; ++i) {
        cin >> p[i];
    }
    sort(p.begin(), p.end());
    double res = 0;
    for (int st = 0; st < n; ++st) {
        vector<double> pp;
        int ind = st;
        for (int j = 0; j < k; ++j, ++ind) {
            if (ind == n)
                ind = 0;
            pp.push_back(p[ind]);
        }
        double cur = getPr(pp);
        res = max(res, cur);
    }
    fprintf(out, "%0.18f\n", res);
    cout << res << endl;
}

int main() {
    out = fopen("output.txt", "w");
    //freopen("B-small.txt", "r", stdin);
    freopen("B-large.in", "r", stdin);
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int tt;
	//scanf("%d\n", &tt);
	cin >> tt;
	for (int i = 0; i < tt; ++i) {
        fprintf(out, "Case #%d: ", i + 1);
        solve();
		std::cerr << i << endl;
	}
	return 0;
}