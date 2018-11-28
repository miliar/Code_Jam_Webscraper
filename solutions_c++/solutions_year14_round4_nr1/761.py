#pragma comment(linker, "/STACK:256000000")

#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <ctime>
#include <math.h>
#include <vector>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <sstream>

using namespace std;

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

const double PI = acos(-1.0);
const int INF = 1000000000;
const int MOD = 1000000007;



int main() {
	
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

	int T; cin >> T;

	for (int test = 1; test <= T; ++test) {
		int n, x;
		cin >> n >> x;
		vector<int> s(n);
		for (int i = 0; i < n; ++i) cin >> s[i];

		int discs = 0;
		int left = 0, right = n - 1;
		sort(s.begin(), s.end());

		while (left < right) {
			if (s[left] + s[right] <= x) {
				++left;
				--right;
				++discs;
				continue;
			}

			--right;
			++discs;
		}

		if (left == right) ++discs;

		cout << "Case #" << test << ": " << discs << endl;
	}


	
    return 0;
}