#include	<iostream>
#include	<algorithm>
#include	<cstring>
#include    <fstream>

#define	FOR(i, a, b) for (int i = (a), _b = (b); i < _b; i++)
#define	FOR_(i, a, b) for (int i = (a), _b = (b); i <= _b; i++)
#define	_FOR(i, a, b) for (int i = (a), _b = (b); i >= _b; i--)

#define PI 3.14159265358979323846
#define	LL long long
#define	NM 101

using namespace std;

int t, a, b, k, res;

int	main() {

	ios::sync_with_stdio(0);
	ifstream cin ("test.inp");
	ofstream cout ("test.out");
	cin >>t;
	FOR_(tt, 1, t) {
		cout <<"Case #" <<tt <<": ";
		cin >>a >>b >>k;
		res = 0;
		FOR(i, 0, a)
			FOR(j, 0, b)
				if ((i & j) < k) res++;
		cout <<res  <<endl;
	}
	return 0;

}
