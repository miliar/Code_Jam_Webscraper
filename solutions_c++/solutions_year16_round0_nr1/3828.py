// very useful, common imports
#include <iostream>
#include <string>
#include <stdlib.h>
#include <memory>
#include <cassert>
#include <climits>
#include <cctype>
#include <vector>
#include <map>
#include <list>
#include <deque>
#include <algorithm>
#include <cmath>
#include <set>

// bost library for printing out complex data structs. useful for debugging
// can be found http://louisdx.github.io/cxx-prettyprint/
#include "../common/prettyprint.h"

#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define mp make_pair
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()

using namespace std;

using pii = pair<int, int>;
using vpii = vector<pii>;
using vi = vector<int>;
using vd = vector<double>;
using vii = vector<vector<int> >;


void solve(int n)
{
	int num;
	cin >> num;

	if (!num) {
		cout << "Case #" << n << ": INSOMNIA\n";
		return;
	}

	vector<bool> seen(10, false);

	int mult = 0;
	int nn = num;

	while (any_of(all(seen), [](bool b){return !b;})) {

		mult++;
		nn = num * mult;

		string numstr = to_string(nn);
		for (int i = 0; i < numstr.length(); ++i) {
			seen[numstr[i]-'0'] = true;
		}


	}

	cout << "Case #" << n << ": "  <<  nn    << "\n";
}

int main()
{
	int N;
	cin >> N;

	for (int i = 0; i < N; ++i) {
		solve(i+1);
	}
}