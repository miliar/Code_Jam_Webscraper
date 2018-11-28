#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <climits>
#include <cmath>
using namespace std;

int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("A-largesol.out", "wt", stdout);
	int tc, n, total = 0, add = 0;
	cin >> tc;
	for (int t = 1; t <= tc; t++) {
		cin >> n;
		string s;
		total = add = 0;
		cin >> s;
		for (int i=0; i <= n; i++) {
			if (i > total) {
				add += i - total;
				total = i;
			}
			total += s[i] - '0';
		}
		cout << "Case #" << t << ": " << add << endl;
	}
}