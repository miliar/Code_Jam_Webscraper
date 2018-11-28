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

const int N = (int)(103);

int main() {
#ifdef FILE_IO
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	for(int qq = 0; qq < T; ++qq) {
		cout << "Case #" << qq+1 << ": ";

		lli c, d, v;
		cin >> c >> d >> v;
		vector<lli> a(d);
		for(int i = 0; i < d; ++i) cin >> a[i];

		int ans = 0;
		lli sum = 0;
		int p = 0;

		while(sum < v) {
			while(p < d && a[p] <= sum+1) {
				sum += a[p++];
			}
			if (sum < v) {
				ans++;
				sum += sum+1;
			}
		}

		cout << ans;

		cout << endl;
	}
    return 0;
}   