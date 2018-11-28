#include	<iostream>
#include	<algorithm>
#include    <fstream>

#define	FOR(i, a, b) for (int i = (a), _b = (b); i < _b; i++)
#define	FOR_(i, a, b) for (int i = (a), _b = (b); i <= _b; i++)
#define	_FOR(i, a, b) for (int i = (a), _b = (b); i >= _b; i--)

#define PI 3.14159265358979323846
#define	LL long long
#define	NM 1000000

#define FI "A-small-attempt2.in"
#define FO "A-small-attempt2.ou"

using namespace std;
int t, x1, x2, a1[4][4], a2[4][4], c, res;

int	main() {

	ios::sync_with_stdio(0);
	ifstream in (FI);
    ofstream out (FO);
	in >>t;
	FOR_(tt, 1, t) {
		in >>x1; x1--;
		c = 0;
		FOR(i, 0, 4)
			FOR(j, 0, 4) in >>a1[i][j];
		in >>x2; x2--;
		FOR(i, 0, 4)
			FOR(j, 0, 4) in >>a2[i][j];
		FOR(i, 0, 4)
			FOR(j, 0, 4)
				if (a1[x1][i] == a2[x2][j]) {
					res = a1[x1][i];
					c++;
				}
		out <<"Case #" <<tt <<": ";
		if (c == 1) out <<res;
		else if (c == 0) out <<"Volunteer cheated!";
		else out <<"Bad magician!";
		out <<endl;
	}
	in.close();
	out.close();
	return 0;

}
