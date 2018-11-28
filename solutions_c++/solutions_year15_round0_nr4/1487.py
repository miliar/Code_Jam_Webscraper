#include <iostream>

using namespace std;

bool solve(int x, int r, int c)
{
	switch(x) {
	case 1:
		return true;
	case 2:
		return ((r * c) % x == 0) && ((r >= x) || (c >= x));
	case 3:
		return ((r * c) % x == 0) && ((r >= x) || (c >= x)) && (r > 1) && (c > 1);
	case 4:
		return ((r * c) % x == 0) && ((r >= x) || (c >= x)) && (r > 2) && (c > 2);
	}
	return true;
}

int main()
{
	int tests_num;
	cin >> tests_num;
	for(int t = 1; t <= tests_num; ++t) {
		int x, r ,c;
		cin >> x >> r >> c;
		cout << "Case #" << t << ": ";
		if(solve(x, r, c)) {
			cout << "GABRIEL" << endl;
		} else {
			cout << "RICHARD" << endl;
		}
	}
	return 0;
}
