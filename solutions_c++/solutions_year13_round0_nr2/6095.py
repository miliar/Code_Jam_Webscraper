#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>
#include <set>

#pragma comment (linker, "/stack:200000000")

#define forn(i, a, b) for (int i = (a); i < (b); i++)
#define ford(i, a, b) for (int i = (b) - 1; i >= (a); i--)
#define mp make_pair
#define min(a, b) ((a < b) ? (a) : (b))
#define max(a, b) ((a > b) ? (a) : (b))
#define abs(a) ((a < 0) ? (-(a)) : (a))
#define pb push_back
#define fs first
#define sc second
#define rn(a) int a; scanf("%d", &(a));
#define rn2(a, b) int a, b; scanf("%d %d", &(a), &(b));
#define rn3(a, b, c) int a, b, c; scanf("%d %d %d", &(a), &(b), &(c));
#define rd(a) scanf("%d", &(a));
#define rd2(a, b) scanf("%d %d", &(a), &(b));
#define rd3(a, b, c) scanf("%d", &(a), &(b), &(c));
#define sz size

using namespace std;

const int mod = 1000000007;
const int maxn = 300010;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pii> vii;
const int inf = 2e9;
const double eps = 1e-7;
inline int gcd(int a, int b) {
    if(a < b) swap(a, b);
    if(a % b == 0) return b;
    return gcd(b, a % b);
}
int mul(int a, int b) {
	return ((ll)a * (ll)b) % mod;
}

int mx[101][2];
int a[101][101];

int main() {	
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	int p;
	cin >> p;
	
	forn(c, 1, p + 1) {
		forn(i, 0, 101)
			mx[i][0] = mx[i][1] = 0;
		rn2(n, m);
		forn(i, 0, n) 
			forn(j, 0, m) {
				rd(a[i][j]);
				mx[i][0] = max(mx[i][0], a[i][j]);
				mx[j][1] = max(mx[j][1], a[i][j]);
			}
		bool tmp = 1;
		forn(i, 0, n)
			forn(j, 0, m)
				if (a[i][j] != min(mx[i][0], mx[j][1]))
					tmp = 0;
		cout << "Case #" << c;
		if (tmp)
			cout << ": YES";
		else
			cout << ": NO";
		cout << endl;
	}
}
