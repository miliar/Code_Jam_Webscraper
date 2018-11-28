#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define all(a) (a).begin(),(a).end()
#define UN(a) sort(all(a)),(a).resize(unique(all(a))-(a).begin())
#define sz(a) ((int) (a).size())
#define pb push_back
#define CL(a,b) memset ((a), (b), sizeof (a))
#define X first
#define Y second

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;

string problemName = "C";
string smallFileName = problemName + "-small-attempt2";
string largeFileName = problemName + "-large";

//string fileName(1, tolower(problemName[0]));
string fileName = smallFileName;
//string fileName = largeFileName;

string inputFileName = fileName + ".in";
string outputFileName = fileName + ".out";

vector<string> a, b;

int go(int y, int x, int n, int m) {
    b[y][x] = '.';
    int ans = 1;
    FOR (yy, y-1, y+2) {
	FOR (xx, x-1, x+2) {
	    if (yy == y && xx == x) continue;
	    if (yy < 0 || xx < 0 || yy >= n || xx >= m) continue;
	    if (b[yy][xx] == '*') return 1;
	}
    }
    FOR (yy, y-1, y+2) {
	FOR (xx, x-1, x+2) {
	    if (yy == y && xx == x) continue;
	    if (yy < 0 || xx < 0 || yy >= n || xx >= m) continue;
	    if (b[yy][xx] == '$') ans += go(yy, xx, n, m);
	}
    }
    return ans;
}

vector<string> solve(int n, int m, int k) {
    a.clear();
    a.resize(n);
    REP (i, n) a[i] = string(m, '$');
    REP (i, 1<<(n * m)) {
	int mines = __builtin_popcount(i);
	if (mines != k) continue;	
	REP (y, n) REP (x, m) {
	    if ((i >> (y*m+x)) & 1) continue;
	    b = a;
	    int j = i;
	    REP (q, n) {
		REP (w, m) {
		    if (j & 1) {
			b[q][w] = '*';
		    }
		    j /= 2;
		}
	    }
	    int u = go(y, x, n, m);
	    b[y][x] = 'c';
	    if (u == n*m - mines) {
		return b;
	    }
	}
    }
    return vector<string> ();
}

int main () {
    freopen(inputFileName.data(), "r", stdin);
    if (fileName == smallFileName || fileName == largeFileName)
    {
	freopen(outputFileName.data(), "w", stdout);
    }
    int T;
    cin >> T;
    REP (test, T) {
	int n, m, k;
	cin >> n >> m >> k;
	cout << "Case #" << (test + 1) << ":\n";
	vector<string> res = solve(n, m, k);
	if (!sz(res)) {
	    cout << "Impossible" << endl;
	    continue;
	}
	REP (i, sz (res))
	    cout << res[i] << endl;
    }
//     FOR (i, 1, 25) {
// 	vector<string> res = solve(5, 5, i);
// 	cout << i << ":\n";
// 	REP (j, sz (res))
// 	    cout << res[j] << endl;
//     }
    return 0;
}
