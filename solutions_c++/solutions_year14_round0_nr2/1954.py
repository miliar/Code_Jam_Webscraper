#include<cstdio>
#include<cstring>
#include<cmath>
#include<cctype>
#include<cstdlib>
#include<iostream>
#include<map>
#include<string>
#include<set>
#include<bitset>
#include<vector>
#include<queue>
#include<list>
#include<stack>
#include<algorithm>
using namespace std;

#define PB push_back
#define MP make_pair
#define SIZE(X) (int)(X).size()

#define REP(i, n) for(int i = 0; i < (n); i++)
#define FOR(i, l, h) for(int i = (l); i < (h); i++)
#define RREP(i, n) for(int i = (int)(n-1); i >= 0; i--)
#define FORD(i, l, h) for(int i = (int)(h-1); i >= (l); i--)

typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<string>VS;
typedef pair<int, int> PII;
typedef vector<PII> VII;
typedef long long ll;

const ll oo = (1LL)<<40;
const int MAXN = 110;
const int MOD = 1000000007;
const double eps = 1e-8;
int n;
int main()
{
	//ios_base::sync_with_stdio(false);
	int T;
	//freopen("b-small.in", "r", stdin);
	//freopen("b-small.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin >> T;
	FOR(_, 1, T+1) {
		double C, F, X;
		double v = 2, t = 0;
		cin >> C >> F >> X;
		double cur = 0;
		if(C < X) {
			t += C/v; //first time can have a farm
			while(cur+eps < X) {
				if(X*v < (v+F)*(X-C)) {
					t += C/(v+F);
					v += F;
				}else{
					t += (X-C)/v;
					break;
				}
			}
		} else{
			t = X/2;
		}
		cout << "Case #" << _ << ": ";
		printf("%.7lf\n", t);
		//cout << t << endl;
	}
	return 0;
}

