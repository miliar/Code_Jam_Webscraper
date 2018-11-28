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

#define ULL unsigned long long

int inv(char s) {
	return (s == '+') ? '-' : '+';
}

int dp(char *sides, int s, char side) {
	if (s == -1) return 0;
	if (sides[s] == side) return dp(sides, s-1, side);
	for (int i=s-1; i>=0; --i) {
		if (sides[i] != sides[s]) return dp(sides, i, inv(side)) + 1;
	}
	return 1;
}

int main (int argc, char **argv)
{
	FILE *fin = fopen(argv[1], "r");
	if (fin==NULL) exit(1);
	int T;
	fscanf(fin, "%d", &T);
	char sides[110];

	for (int i=0; i<T; ++i) {
		fscanf(fin, "%s", sides);
		int s = strlen(sides);
		cout << "Case #" << i+1 << ": " << dp(sides, s-1, '+') << endl;
	}

	fclose(fin);
	return 0;
}






