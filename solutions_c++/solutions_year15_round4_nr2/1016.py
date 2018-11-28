#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <sstream>
#include <ctime>
#include <functional>
#include <iomanip>
#define pi 3.14159265358979323846264338327950288
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define LL long long
#define LD long double
#define INF 1000000000
#define INFll 1000000000000000000ll
#define Vi vector<int>
#define VI Vi::iterator
#define Mi map<int, int>
#define MI Mi::iterator
#define Si set<int>
#define SI Si::iterator
#define FOR(i,s,e) for (int i=(s); i<(e); i++)
#define FOE(i,s,e) for (int i=(s); i<=(e); i++)
#define FOD(i,s,e) for (int i=(s)-1; i>=(e); i--)
#define CLR(a,x) memset(a, x, sizeof(a))
#define SZ(x) ((int)x.size())
#define mid (l + r) / 2
#define Left k * 2, l, mid
#define Right k * 2 + 1, mid + 1, r
#define N 1111111
#define eps 1e-10
using namespace std;

struct node {
    LD r, c;
}a[N];
bool cmp(node a, node b) {
    return a.c < b.c;
}
int cmpd(LD a) {
    if (fabs(a) < eps) return 0;
    if (a > eps) return 1;
    if (a < eps) return -1;
}
LD  v, x;
int n;
int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cout << fixed << showpoint;
	int T, cas;
	scanf("%d", &T);
	for (cas = 1; cas <= T; cas++) {
		printf("Case #%d: ", cas);
		LD sumr = 0, sums = 0;
		cin >> n >> v >> x;
		for (int i = 0; i < n; i++){
			cin >> a[i].r >> a[i].c;
			sumr += a[i].r;
			sums += (a[i].c - x) * a[i].r;
		}
		sort(a, a + n, cmp);
		if (cmpd(sums) == 0) {
			cout << setprecision(10) << v / sumr << endl;
			continue;
		}
		if (cmpd(sums) < 0) {
			for (int i = 0; i < n; i++) {
				LD temp = (a[i].c - x) * a[i].r;
				if (cmpd(sums - temp) < 0) {
					sumr -= a[i].r;
					sums -= temp;
				}
				else {
					sumr -= sums / (a[i].c - x);
					sums = 0;
					break;
				}
			}
			if (cmpd(sumr) <= 0)
				cout << "IMPOSSIBLE" << endl;
			else
				cout << setprecision(10) << v / sumr << endl;
		}
		else {
			for (int i = n - 1; i >= 0; i--) {
				LD temp = (a[i].c - x) * a[i].r;
				if (cmpd(sums - temp) > 0) {
					sumr -= a[i].r;
					sums -= temp;
				}
				else {
					sumr -= sums / (a[i].c - x);
					sums = 0;
					break;
				}
			}
			if (cmpd(sumr) <= 0)
				cout << "IMPOSSIBLE" << endl;
			else
				cout << setprecision(10) << v / sumr << endl;
		}

	}
}
