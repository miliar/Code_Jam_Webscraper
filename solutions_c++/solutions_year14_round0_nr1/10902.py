/*
ID: mbahran1
PROG: checker
LANG: C++
*/

#include <iostream>
#include <algorithm>
#include <fstream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <iomanip>
#include <cassert>
#include <set>
#include <map>

#define show(x) cerr << "# " << #x << " = " << (x) << endl

#define FOR(i, a, b) for(__typeof(a) i = a; i != b; i++)
#define FR(i, a) FOR(i, 0, a)
#define FOREACH(i, t) FOR(i, t.begin(), t.end())
#define ALL(x) (x).begin(), (x).end()
#define SZ(a) int(a.size())
#define PB push_back
#define MP make_pair
#define F first
#define S second

using namespace std;

inline bool ascending (int i, int j) { return (i < j); }
inline bool descending (int i, int j) { return (i > j); }

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

const int MAXN = 5;

int a[MAXN][MAXN], b[MAXN][MAXN];
int t, x, y, tmp;
set<int> ans;

int main()
{
	// Case Handling
	cin >> t;
	FR(q, t){
		ans.erase(ans.begin(), ans.end());
		
		// INPUT
		cin >> x; x--;
		FR(i, 4) FR(j, 4) cin >> a[i][j];
		cin >> y; y--;
		FR(i, 4) FR(j, 4) cin >> b[i][j];
		
		// Computations
		FR(i, 4) FR(j, 4){
			if(a[x][i] == b[y][j]) ans.insert(a[x][i]), tmp = a[x][i];
		}
		
		// Output
		cout << "Case #" << q + 1 << ": ";
		if(ans.size() == 1) cout << tmp;
		else if (ans.size() > 1) cout << "Bad magician!";
		else cout << "Volunteer cheated!";
		cout << endl;
	}
	
	return 0;
}
