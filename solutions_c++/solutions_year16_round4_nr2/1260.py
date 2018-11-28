#define _USE_MATH_DEFINES

#include <iostream>
#include <sstream>
#include <cmath>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

typedef vector<int> vi;

typedef long long ll;

#define FOR(x, b, e) for (int x = b; x <= (e); ++x)
#define FORR(x, b, e) for (int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define REPR(x, n) for(int x = (n - 1); x >= 0; --x)

const int INF = 1000000001;
typedef vector<ll> vll;

stringstream out;

int norm(int n) { return n < INF ? n : INF; }
//---------------------------------------------------------------

float probs[1000];
float best = 0.0f;
vi combination;
int k, n;

float func(int na, float prob, int plus, int minus) {
	if (na == combination.size()) {
		if (plus == minus)
			return prob;

		return 0.0f;
	}
	float pr1 = prob * probs[combination[na]];
	float pr2 = prob * (1 - probs[combination[na]]);
	return func(na + 1, pr1, plus + 1, minus) + func(na + 1, pr2, plus, minus + 1);
}

void f(int offset, int ka) {
	if (ka == 0) {
		float prob = func(0, 1.0f, 0, 0);
		if (prob > best)
			best = prob;
		return;
	}
	FOR(i, offset, n - ka) {
		combination.push_back(i);
		f(i + 1, ka - 1);
		combination.pop_back();
	}
}

void function()
{
	cin >> n >> k;
	REP(i, n)
		cin >> probs[i];
	best = 0.0f;
	f(0, k);
	out << best << endl;
}

//---------------------------------------------------------------
int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	FOR(i, 1, t)
	{
		out << "Case #" << i << ": ";
		function();
		clog << i << endl;
	}
	cout << out.str();
	return 0;
}