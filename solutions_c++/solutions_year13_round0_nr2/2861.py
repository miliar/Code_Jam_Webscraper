#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

using namespace std;

#define rep(i, n) for(int i = 0; i < (n); i++)
#define For(i, a, b) for(int i = (a); i < (b); i++)
#define foreach(it, c) for(__typeof (c).begin() it = (c).begin(); it != (c).end(); ++it)
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define sz(v) (int)(v).size()
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define sqr(x) ((x) * (x))
#define clr(m, c) memset((m), (c), sizeof (m))
#define DBG(x) cout << #x << " = " << x << endl
#define EPS 1e-9
#define PI 3.14159265358979323846264338327950

template<class T> T abs(T x) { return x > 0 ? x : -x; }

typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;
typedef vector<int> vi;

const ll INF = 1LL<<60;
const ll MOD = 1000000007;

int M[111][111];
int n, m;

bool can(int x, int y){
	bool res1 = true, res2 = true;
	for(int i = 0; i < n; i++) res1 &= (M[i][y] <= M[x][y]);
	for(int i = 0; i < m; i++) res2 &= (M[x][i] <= M[x][y]);
	return res1 or res2;
}

int main(){
	int tt; cin >> tt;
	for(int t = 1; t <= tt; t++){
		scanf("%d %d", &n, &m);
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				scanf("%d", &M[i][j]);
		bool res = true;
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				res &= can(i, j);
		printf("Case #%d: %s\n", t, (res ? "YES" : "NO"));
	}
	return 0;
}
