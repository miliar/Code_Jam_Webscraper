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
	string line;
	cin >> line; 

	bool starts_with_plus = (line[0] == '+');
	int len = 1;
	for (int i = 1; i < line.length(); ++i) {
		if (line[i - 1] != line[i]) {
			len++;
		}
	}

	int res;
	if (starts_with_plus) {
		res = int(len / 2) * 2;
	}
	else {
		res = int((len - 1)/2) * 2 + 1;
	}

	cout << "Case #" << n << ": " << res  << "\n";
}

int main()
{
	int N;
	cin >> N;

	for (int i = 0; i < N; ++i) {
		solve(i+1);
	}
}