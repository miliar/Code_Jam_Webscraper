#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <functional>
using namespace std;

#define mp make_pair
#define lli long long int

const int N = (int)(60);


int main() {
#ifdef FILE_IO
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	for(int qq = 0; qq < T; ++qq) {
		cout << "Case #" << qq+1 << ": ";

		int r, c, w;
		cin >> r >> c >> w;
		int rowAns = (r-1) * (c/w);
		int ans = 0;

		if (c % w == 0) {
			ans = (c/w - 1);
		} else {
			int to = w-1;
			while(to < c) {
				++ans;
				int rest = (c - to);
				if (rest < w) break;
				to += w;
			}
		}

		cout << ans + rowAns + w;
		cout << endl;
	}
    return 0;
}   