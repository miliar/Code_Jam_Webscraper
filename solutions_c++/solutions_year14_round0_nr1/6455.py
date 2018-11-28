#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
using namespace std;

typedef double DB;
typedef unsigned int UI;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<char> VC;
typedef vector<double> VD;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef vector<PII> VPII;

#define PB push_back
#define MP make_pair
#define ALL(x) (x).begin(), (x).end()
#define CLR(a, x) memset(a, x, sizeof(a))

template <class T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template <class T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

inline void RD(int & a) {
    a = 0;
    char c = getchar();
    while (c < '0' || c > '9') c = getchar();
    while (c >= '0' && c <= '9') { a = a * 10 + c - '0'; c = getchar(); }
}
inline void RD(int & a, int & b) { RD(a); RD(b); }
inline void RD(int & a, int & b, int &c) { RD(a); RD(b); RD(c); }
inline void RD(int & a, int & b, int & c, int & d) { RD(a); RD(b); RD(c); RD(d); }

const int MOD = 1000000007;
LL inv(LL a) { return a == 1 ? 1 : (MOD - MOD / a) * inv(MOD % a) % MOD; }
LL mPow(LL x, int n) { LL ret = 1; while (n) { if (n & 1) ret = ret * x % MOD; x = x * x % MOD; n >>= 1; } return ret; }
LL mC(int n, int m) { LL ret = 1; for(int i = 1; i <= m; i++, n--) { ret = ret * n % MOD * inv(i) % MOD; } return ret; }

int g1, g2, a[4][4], b[4][4];

int main() {
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int cas; cin >> cas;
    for (int t = 1; t <= cas; t++) {
    	cin >> g1; g1--;
    	for (int i = 0; i < 4; i++) {
    		for (int j = 0; j < 4; j++) {
    			cin >> a[i][j];
    		}
    	}

    	cin >> g2; g2--;
    	for (int i = 0; i < 4; i++) {
    		for (int j = 0; j < 4; j++) {
    			cin >> b[i][j];
    		}
    	}

    	int k, cnt = 0;
    	for (int i = 0; i < 4; i++) {
    		int x = a[g1][i];
    		for (int j = 0; j < 4; j++) if (b[g2][j] == x) {
    			cnt++;
    			k = x;
    			break;
    		}
    	}

    	printf("Case #%d: ", t);

    	if (cnt == 0) {
    		printf("Volunteer cheated!\n");
    	} else if (cnt == 1) {
    		printf("%d\n", k);
    	} else {
    		printf("Bad magician!\n");
    	}
    }
    return 0; 
}