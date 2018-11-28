#include <cstring>
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

double c, f, x;
double n, v, tt, t, s;

void deal()
{
	cin >> c >> f >> x;
	s = 0.0;
	n = 0.0;
	v = 2.0;
	t = x / v;
	do {
		double g = c / v;
		tt = g + x / (v + f);
		if (t > tt) {
			s += g;
			v += f;
			t = x / v;
		} 
		else {
			break;
		}
	} while (t > 0);
	cout << setprecision(7) << setiosflags(ios::fixed);
	cout << s+t << endl;
}

int main()
{
	int cases;

	ios::sync_with_stdio(false);

	cin >> cases;
	for (int t = 1; t <= cases; ++t) {
		cout << "Case #" << t << ": ";
		deal();
	}

	return 0;
}