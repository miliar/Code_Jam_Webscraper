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

void find(long n, unordered_set<int>& d) {
	while (n != 0) {
		d.insert(n%10);
		n /= 10;
	}
}

int main (int argc, char **argv)
{
	FILE *fin = fopen(argv[1], "r");
	if (fin==NULL) exit(1);
	int T;
	fscanf(fin, "%d", &T);

	for (int i=0; i<T; ++i) {
		long N;
		fscanf(fin, "%ld", &N);
		if (N == 0) {
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
			continue;
		}
		unordered_set<int> ds;
		int j = 1;
		while (ds.size() != 10) {
			find(N*j, ds);
			j++;
		}
		cout << "Case #" << i+1 << ": " << N*(j-1) << endl;
	}

	fclose(fin);
	return 0;
}






