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

string problemName = "D";
string smallFileName = problemName + "-small-attempt1";
string largeFileName = problemName + "-large";

//string fileName(1, tolower(problemName[0]));
//string fileName = smallFileName;
string fileName = largeFileName;

string inputFileName = fileName + ".in";
string outputFileName = fileName + ".out";

const int mod = 1000000007;

int d[110000];
long long ways[110000];

int cnk[128][128];
int n;
bool node[110000];
int child[110000][26];
long long yo[128];

int main () {
    freopen(inputFileName.data(), "r", stdin);
    if (fileName == smallFileName || fileName == largeFileName)
    {
	freopen(outputFileName.data(), "w", stdout);
    }
    REP (i, 128) {
	cnk[i][0] = cnk[i][i] = 1;
	FOR (j, 1, i) {
	    cnk[i][j] = (cnk[i-1][j-1] + cnk[i-1][j]) % mod;
	}
    }
    int T;
    cin >> T;
    REP (test, T) {
	memset(child, -1, sizeof(child));
	memset(node, 0, sizeof(node));
	memset(d, 0, sizeof(d));
	memset(ways, 0, sizeof(ways));
	int q, m;
	cin >> q >> m;
	n = 1;
	REP (i, q) {
	    string s;
	    cin >> s;
	    int x = 0;
	    REP (j, sz (s)) {
		if (child[x][s[j]-'A'] == -1) {
		    child[x][s[j]-'A'] = n;
		    ++n;
		}
		x = child[x][s[j]-'A'];
	    }
	    node[x] = true;
	}
	long long res = 0;
	for (int i = n-1; i >= 0; --i) {
	    vector<int> v;
	    long long mult = 1;
	    REP (k, 26) if (child[i][k] != -1) {
		int j = child[i][k];
		v.pb(d[j]);
		mult *= ways[j];
		mult %= mod;
	    }
	    if (node[i])
		v.pb(1);
	    // REP (j, sz(v))
	    // 	cout << v[j] << ' ';
	    // cout << endl;
	    int sum = 0;
	    int ma = 0;
	    REP (j, sz (v)) {
		sum += v[j];
		ma = max(ma, v[j]);
	    }
	    sum = min(sum, m);
	    
	    FOR(j, ma, sum+1) {
		yo[j] = 1;
		REP (k, sz (v)) {
		    yo[j] *= cnk[j][v[k]];
		    yo[j] %= mod;
		}
		FOR (k, ma, j) {
		    yo[j] -= yo[k] * cnk[j][k];
		    yo[j] %= mod;
		    yo[j] += mod;
		    yo[j] %= mod;
		}
	    }
	    long long r = yo[sum];
	    r *= mult;
	    r %= mod;
	    ways[i] = r;
	    d[i] = sum;
	    res += sum;
	    //	    cout << i << ' ' << ways[i] << ' ' << d[i] << endl;
	}
	cout << "Case #" << (test + 1) << ": ";
	cout << res << ' ' << ways[0] << endl;
    }
    return 0;
}
