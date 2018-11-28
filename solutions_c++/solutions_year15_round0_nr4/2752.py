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
#define f first
#define s second
using namespace std;

int main()
{
	freopen("D-small-attempt1.in", "rt", stdin);
	freopen("Out1.out", "wt", stdout);
	int tc, x, r, c;
	cin >> tc;
	string ans;
	for (int t = 1; t <= tc; t++) {
		cin >> x >> r >> c;
		cout << "Case #" << t << ": ";
		if (x >= 7) {
			cout << "RICHARD\n";
			continue;
		}
		else {
			if ((x == 1 || x == 2) && r *c % x == 0) {
				cout << "GABRIEL\n";
				continue;
			}
			else if ( (x == 3) && r >=2 && c >=2 && (r * c )/ x >= 2 && (r * c)%x == 0)
			{
				cout << "GABRIEL\n";
				continue;
			}
			else if (x == 4 && r >=3 && c >=3 && (r * c) % 4 == 0) {
				cout << "GABRIEL\n";
				continue;
			}
			else if (x == 5 && r >=3 && c >= 3 && (r * c)/x >= 3 && (r * c) %x == 0) {
				cout << "GABRIEL\n";
				continue;
			}
			else if (x == 6 && r >=4 && c >=4 && (r * c)/x >= 4 && (r * c) %x == 0) {
				cout << "GABRIEL\n";
				continue;
			}
			else {
				cout << "RICHARD\n";
				continue;
			}
		}
	}
	return 0;	
}