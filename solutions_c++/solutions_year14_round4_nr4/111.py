#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <utility>
//#include <set>
//#include <map>
//#include <queue>
#include <iomanip>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vint;
//typedef vector<string> vstr;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

vector<string> ss;
int n;
const ll mm = 1000000007;
ll cc[101][101] = {};
ll pp[101][101] = {};

void solve(int pl, int b, int e, int& node, ll& cnt) {
    node = 0;
    cnt = 1;
    int m = e - b;
    if (m <= n) {
        for (int i = b; i < e; i++) node += ss[i].length() - pl;
        return;
    }
    int newpl = pl;
    while (newpl < ss[b].length() && newpl < ss[e-1].length() && ss[b][newpl] == ss[e-1][newpl]) newpl++;
    if (newpl > pl) {
        node += (newpl - pl) * n;
        pl = newpl;
    }
    int i = b;
    vector<int> z;
    if (ss[b].length() == pl) {
        i++;
        z.push_back(1);
    }
    while (i < e) {
        int j = i + 1;
        while (j < e && ss[i][pl] == ss[j][pl]) j++;
        int node2;
        ll cnt2;
        solve(pl, i, j, node2, cnt2);
        node += node2;
        cnt = cnt * cnt2 % mm;
        z.push_back(j - i);
        i = j;
    }
    ll tmp = 1;
    bool has_full_n = false;
    for (i = 0; i < z.size(); i++) {
        if (!has_full_n && z[i] >= n) {
            has_full_n = true;
        } else {
            int k = min(n, z[i]);
            tmp = tmp * pp[n][k] % mm;
        }
    }
    if (!has_full_n) {
        vector<ll> x(n+1, 0);
        x[0] = 1;
        for (i = 0; i < z.size(); i++) {
            vector<ll> y(n+1, 0);
            for (int used = 0; used <= n; used++) if (x[used] != 0) {
                for (int k = 0; k <= z[i] && used+k<=n; k++) {
                    if (used < z[i]-k) continue;
                    y[used + k] = (x[used] * pp[used][z[i]-k] % mm * cc[z[i]][k] % mm + y[used + k]) % mm;
                }
            }
            swap(x, y);
        }
        tmp = x[n];
    }
    cnt = cnt * tmp % mm;
}

int main()
{
    for (int i = 0; i <= 100; i++) {
        pp[i][0] = 1;
        for (int j = 1; j <= i; j++)
            pp[i][j] = pp[i][j-1] * (i+1-j) % mm;
        cc[i][0] = cc[i][i] = 1;
        for (int j = 1; j < i; j++)
            cc[i][j] = (cc[i-1][j-1] + cc[i-1][j]) % mm;
    }
	int tcase = 0;
	ifstream fin("../D-large.in");
	ofstream fout("z.out");
	fin >> tcase;
	for (int tind = 1; tind <= tcase; tind++)
	{
        ss.clear();
		int i,j;
		int m;
		fin >> m >> n;
		for (i = 0; i < m; i++) {
            string s;
            fin >> s;
            ss.push_back(s);
		}
		sort(ss.begin(), ss.end());
		int ans = 0;
		ll cnt = 0;
		solve(0, 0, ss.size(), ans, cnt);
		ans += n;
		for (i = 1; i <= n; i++) cnt = cnt * i % mm;
		fout << "Case #" << tind << ": " << ans << " " << cnt << endl;
	}
	return 0;
}
