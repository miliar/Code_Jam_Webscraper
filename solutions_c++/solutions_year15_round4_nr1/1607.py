#include <algorithm>
#include <iostream>
#include <cstdio>
#include <map>
#include <numeric>
#include <cmath>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <complex>
#include <string.h>
#include <unordered_set>
#include <unordered_map>
#include <iomanip>
using namespace std;

#define endl '\n'
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define uniq(v) (v).erase(unique((v).begin(), (v).end()), (v).end())

typedef long long ll;
typedef pair<int, int> P;
typedef unsigned int uint;
typedef unsigned long long ull;
struct pairhash {
public:
    template<typename T, typename U>
    size_t operator()(const pair<T, U> &x) const {
	size_t seed = hash<T>()(x.first);
	return hash<U>()(x.second) + 0x9e3779b9 + (seed<<6) + (seed>>2);
    }
};

const int inf = 1000000009;
const double eps = 1e-8;
const string yes = "YES", no = "NO";
int r, c;
bool out(vector<string>& s, int i, int j) {
    for (int k = j + 1; k < c; k++)
	if (s[i][k] != '.') return true;

    for (int k = j - 1; k >= 0; k--)
	if (s[i][k] != '.') return true;

    for (int k = i-1; k >= 0; k--)
	if (s[k][j] != '.') return true;

    for (int k = i + 1; k < r; k++)
	if (s[k][j] != '.') return true;
    
    return false;
}

inline int check(vector<string>& s, int i, int j) {
    if (s[i][j] == '.') return 0;
    if (r == 1 && c == 1) return -1;
    if (!out(s, i, j))
	return -1;

    
    
    if (s[i][j] == '>') {
	for (int k = j + 1; k < c; k++)
	    if (s[i][k] != '.') return 0;
	return 1;
    }
    if (s[i][j] == '<') {
	for (int k = j - 1; k >= 0; k--)
	    if (s[i][k] != '.') return 0;
	return 1;
    }
    if (s[i][j] == '^') {
	for (int k = i-1; k >= 0; k--)
	    if (s[k][j] != '.') return 0;
	return 1;
    }
    if (s[i][j] == 'v') {
	for (int k = i + 1; k < r; k++)
	    if (s[k][j] != '.') return 0;
	return 1;
    }
}

string solve() {
    cin >> r >> c;
    vector<string> s(r);
    for (int i = 0; i < r; i++)
	cin >> s[i];
    int res = 0;
    for (int i = 0; i < r; i++) {
	for (int j = 0; j < c; j++) {
	    int t = check(s, i, j);
	    if (t < 0) return "IMPOSSIBLE";
	    res += t;
	}
    }
    /*
    if (s[0][0] == '<' || s[0][0] == '^') res++;
    if (c>1&&(s[0][c-1] == '^' || s[0][c-1] == '>')) res++;
    if (r>1&&(s[r-1][0] == '<' || s[r-1][0] == 'v')) res++;
    if (c>1&&r>1&&(s[r-1][c-1] == '>' || s[r-1][c-1] == 'v')) res++;

    for (int i = 1; i < c-1; i++) if (s[0][i] == '^') res++;
    for (int i = 1; i < c-1; i++) if (s[r-1][i] == 'v') res++;
    for (int i = 1; i < r-1; i++) if (s[i][0] == '<') res++;
    for (int i = 1; i < r-1; i++) if (s[i][c-1] == '>') res++;
    */
    stringstream ss;
    ss << res;
    return ss.str();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout << fixed << setprecision(15);

    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
	cout << "Case #" << i << ": " << solve() << endl;
    }
}
