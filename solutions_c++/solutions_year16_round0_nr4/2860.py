#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cstdint>
#include <cmath>
#include <utility>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <string.h>

using namespace std;

#define REP(i, p, n) for (int i=p; i<n; ++i)
#define FOR(i, c) for (__typeof ((c).begin()) i=(c).begin(); i!=(c).end(); ++i)

#define ll long long

ll pow(ll a, ll b) {
	if (b == 0) return 1;
	return pow(a, b-1) * a;
}

ll loc(ll k, ll c, ll l) {
	if (c == 1) return 1+l;
	ll base = pow(k, c-1) * l;
	return base+loc(k, c-1, l);
}

int main (int argc, char **argv)
{
	FILE *fin = fopen(argv[1], "r");
	if (fin==NULL) exit(1);
	int N;
	fscanf(fin, "%d", &N);

	for (int i=0; i<N; ++i) {
		ll k, c, s;
		fscanf(fin, "%lld %lld %lld", &k, &c, &s);
		cout << "Case #" << i+1 << ":";
		for (ll j=0; j<k; ++j) {
			cout << " " << loc(k, c, j);
		}
		cout << endl;
	}

	fclose(fin);
	return 0;
}






