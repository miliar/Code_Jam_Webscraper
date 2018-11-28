#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef pair<long, long> ii;

const long MOD = 1000002013;

long N;
long M;
long COST_EXP;
long COST_REAL;

vector<ii> O_POINTS;
vector<ii> E_POINTS;

inline long cost(long o, long e)
{
	long long d = (e-o);
	return (long)(d*(N+1) - d*(d+1)/2) % MOD;
}

inline long cost(long o, long e, long p)
{
	long long c = cost(o, e);
	return (long)(c*p % MOD);
}

void read_input()
{
	cin >> N >> M;

	COST_EXP = 0;
	long o, e, p;
	O_POINTS.clear();
	E_POINTS.clear();
	O_POINTS.reserve(M);
	E_POINTS.reserve(M);
	for (long t = 0; t < M; ++t) {
		cin >> o >> e >> p;
		O_POINTS.push_back(make_pair(o, p));
		E_POINTS.push_back(make_pair(e, p));
		COST_EXP = (COST_EXP + cost(o, e, p)) % MOD;
	}
}

void solve()
{
	sort(O_POINTS.begin(), O_POINTS.end());
	sort(E_POINTS.begin(), E_POINTS.end());

	int ko = 0;
	int ke = 0;

	COST_REAL = 0;
	for (int ko = M-1; ko >= 0; --ko) {
		int ke = 0;
		while (O_POINTS[ko].first > E_POINTS[ke].first) ++ke;
		while (O_POINTS[ko].second > 0) {
			long matched = min(O_POINTS[ko].second, E_POINTS[ke].second);
			O_POINTS[ko].second-= matched;
			E_POINTS[ke].second-= matched;
			COST_REAL = (COST_REAL + cost(O_POINTS[ko].first, E_POINTS[ke].first, matched)) % MOD;
			++ke;
		}
	}
}

int main()
{
	int numOfTests;
	cin >> numOfTests;

	for (int t = 1; t <= numOfTests; ++t) {
		read_input();
		solve();
		cout << "Case #" << t << ": " << (COST_EXP - COST_REAL) << endl;
	}	
}