#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <climits>
#include <vector>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>

#define FORT for(int t=1;t<=T;t++)
#define REP(x,s,n) for(int x=s; x<n; x++)
#define EPSILON (1E-6)
#define CODEJAM 0
#define MAXN 131073
#define sz(s) (s).size()
#define pb(s) push_back((s))
#define all(s) (s).begin(),(s).end()

using namespace std;

typedef long int LI;
typedef long long LL;
typedef long double LD;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef map<int,int> mii;

bool CompareDouble(const LD &, const LD &);

int main() {
    freopen("qualA-large.in", "r+", stdin);
    freopen("outputA-large.txt", "w+", stdout);
    int T;
    cin >> T;
    FORT {
		long int N;
		int res[10] = {0};
		cin >> N;
		if (N > 0) {
			for (int i = 1; ;i++) {
				long int n = N*i;
				while (n > 0) {
					res[n%10] = 1;
					n /= 10;
				}
				int sum = 0;
				for (int j = 0; j < 10; j++) sum += res[j];
				if (sum == 10) {
					N *= i;
					break;
				}
			}
		}
		if (N > 0)
			printf("Case #%d: %d\n", t, N);
		else
			printf("Case #%d: INSOMNIA\n", t);
    }
    return 0;
}

bool CompareDouble(const LD &a, const LD &b) {
    return fabs(a - b) < EPSILON;
}
