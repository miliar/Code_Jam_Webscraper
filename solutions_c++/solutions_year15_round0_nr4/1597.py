#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

string str[2] = {"GABRIEL", "RICHARD"};
int main()
{
	freopen("D-small-attempt4.in", "r", stdin);
	freopen("D.out", "w", stdout);
	int cas = 1;
	cin >> cas;
	for (int t = 1; t <= cas; t++) {
		int x, r, c;
		cin >> x >> r >> c;

		bool flag = 0;
		if (x == 1) {
				flag = 0;
		}
		else if (x == 2) {
			if (r * c <= 1 || r * c % 2 != 0)
				flag = 1;
			else
				flag = 0;
		}
		else if (x == 3) {
			if (r * c <= 3 || r * c % 3 != 0)
				flag = 1;
			else
				flag = 0;
		}
		else {
			if (r * c <= 4 || r * c % 4 != 0 || r * c == 8)
				flag = 1;
			else
				flag = 0;
		}
		printf("Case #%d: ", t);
		cout << str[flag] << endl;

	}
	return 0;
}