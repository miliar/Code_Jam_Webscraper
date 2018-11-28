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
const int MAXN = 1100;
const int MOD = 1000000007;
const double eps = 1e-8;
double nao[MAXN], ken[MAXN];
int n;
int gao(double* a, double* b)
{
	int p1 = 0, p2 = 0;
	int ret = 0;
	while(p2 < n) {
		while(p2 < n && b[p2] < a[p1]) p2++;
		if(p2 < n){ 
			ret++;
			p1++; p2++;
		}
	}
	return ret;
}

int main()
{
	ios_base::sync_with_stdio(false);
	int T;
	//freopen("d-small.in", "r", stdin);
	//freopen("d-small.out", "w", stdout);
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	cin >> T;
	FOR(_, 1, T+1) {
		cin >> n;
		double tmp;
		REP(i, n)  cin >> nao[i]; 
		REP(i, n)  cin >> ken[i];
		sort(nao, nao+n);
		sort(ken, ken+n);
		int p1 = 0, p2 = 0;
		int a1 = gao(ken, nao), a2 = gao(nao, ken);

		cout << "Case #" << _ << ": ";
		cout << a1 << " " << n-a2 << endl;
		//cout << t << endl;
	}
	return 0;
}

