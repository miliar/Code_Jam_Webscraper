#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <ctime>
using namespace std;
typedef long long LL; 
typedef pair<int, int> PII;
typedef vector<int> VI;
#define PB push_back
#define MP make_pair
#define FOR(i, n) for(int i = 0; i < (n); i++)
#define REP(i, a, b) for(int i = (a); i <= (b); i++)
#define CLR(x, a) memset(x, a, sizeof(x))
//#define L(x) ((x) << 1)
#define R(x) (((x) << 1) + 1)
#define LB(x) ((x)&(-(x)))
#define SL(x) (1 << (x))
#define X first
#define Y second
const int MAXN = 1000 + 20;

double A[MAXN];
double B[MAXN];

int main(){

	int T; cin >> T;
	FOR(cas, T){
		printf("Case #%d: ", cas + 1);
		int n; cin >> n;
		FOR(i, n) {
			cin >> A[i];
		}
		FOR(i, n) {
			cin >> B[i];
		}
		sort(A, A + n);
		sort(B, B + n);
		int res1 = 0, res2 = 0;
		for (int i = 0, l = 0, r = n - 1; i < n; i++) {			
			if (A[i] > B[l]) { 
				res1++;
				l++;
			} else r--;
		}
		for (int i = n - 1; i >= 0; i--) {
			FOR(j, n) {
				if (B[j] > A[i]) {
					B[j] = -1;
					res2++;
					break;
				}
			}
		}
		cout << res1 << " " << n - res2 << endl;
	}
}