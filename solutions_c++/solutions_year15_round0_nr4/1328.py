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
#define pi 3.14159265358979323846264338327950288
#define pb push_back
#define mp make_pair
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
#define mid (l + r) / 2
#define Left k * 2, l, mid
#define Right k * 2 + 1, mid + 1, r
#define N 1111111
using namespace std;
int T, cas;
int x, r, c;
int a[1111];
int ans;
char *answer[2] = {"RICHARD", "GABRIEL"};
bool check(int x, int r, int c) {
	if ((r * c) % x != 0) return false;
	if (x == 1) return true;
	if (x == 2) return !(r & c & 1);
	if (x == 3) return (r != 1) && (c != 1);
	if (r < 3 || c < 3) return false;
	return true;
}
int main () {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
	cin >> T;
	for ( cas  = 1; cas <= T; cas ++) {
		cin >> x >> r >> c;
		printf("Case #%d: %s\n", cas, answer[check(x, r, c)]);
	}
}
