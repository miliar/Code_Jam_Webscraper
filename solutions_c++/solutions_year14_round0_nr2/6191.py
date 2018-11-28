#include	<iostream>
#include	<algorithm>

#define	FOR(i, a, b) for (int i = (a), _b = (b); i < _b; i++)
#define	FOR_(i, a, b) for (int i = (a), _b = (b); i <= _b; i++)
#define	_FOR(i, a, b) for (int i = (a), _b = (b); i >= _b; i--)

#define PI 3.14159265358979323846
#define	LL long long
#define	NM 1000000

using namespace std;

double c, f, x, res, tim, num;

int	main() {

	ios::sync_with_stdio(0);
	int t;
	cin >>t;
	cout.setf(ios::fixed);
	cout.precision(7);
	FOR_(tt, 1, t) {
		cout <<"Case #" <<tt <<": ";
		cin >>c >>f >>x;
		tim = 0;
		res = x / 2;
		num = 2;
		while (1) {
			tim += c / num;
			num += f;
			if (tim + x / num > res) break;
			res = tim + x / num;
		}
		cout <<res;
		cout <<endl;
	}
	return 0;

}
