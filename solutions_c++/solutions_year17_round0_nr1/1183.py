#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;

#define INF 1000000000 // 1 billion, safer than 2B for Floyd Warshall’s
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define REP(i, n) for(int i=0;i<(n);i++)
#define FOR(i, a, b) for(int i=(a);i<=(b);i++)
#define FORD(i, a, b) for(int i=(a);i>=(b);i--)

inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

bool panc[1001];

int main() {
    ios::sync_with_stdio(false);
    int T, K;
    string p;
    cin >> T;
    int cas = 1;
    while (T-- > 0) {
    	cin >> p;
    	cin >> K;
    	for(int i = 0; i < p.length(); ++i) {
    		panc[i] = (p[i] == '+');
    	}
    	int count = 0;
    	for(int i = 0; i < p.length() - K + 1; ++i) {
    	// 	for(int i = 0; i < p.length(); ++i) {
    	// cout << panc[i] << " ";
    	// }
    	// cout << endl;
    		if (!panc[i]) {
    			++count;
    			for(int j = i; j < i + K; ++j) {
    				panc[j] = !panc[j];
    			}
    		}
    	}
    	bool solvable = true;
    	for(int i = p.length() - K + 1; i < p.length(); ++i) {
    		if (!panc[i]) {
    			solvable = false;
    			break;
    		}
    	}
    	cout << "Case #" << cas++ <<": ";
    	if (solvable) {
    		cout << count;
    	} else {
    		cout << "IMPOSSIBLE";
    	}
    	cout << endl;

    }
    return 0;
}