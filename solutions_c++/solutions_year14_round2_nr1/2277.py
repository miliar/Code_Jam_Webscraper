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

int t, n, cnt[NM][NM], m, res, sleft[NM], sright[NM];
char s[NM], key[NM], newkey[NM];

int	main() {

	ios::sync_with_stdio(0);
	ifstream cin ("test.inp");
	ofstream cout ("test.out");
	cin >>t;
	FOR_(tt, 1, t) {
		cout <<"Case #" <<tt <<": ";
		cin >>n;
		FOR(i, 0, n) {
			cin >>s;
			m = 1;
			newkey[0] = s[0];
			cnt[0][i] = 1;
			FOR(j, 1, strlen(s)) {
				if (s[j] == s[j - 1]) cnt[m - 1][i]++;
				else {
					newkey[m] = s[j];
					cnt[m++][i] = 1;
				}
			}
			newkey[m] = 0;
			if (i == 0) strcpy(key, newkey);
			if (strcmp(key, newkey) != 0) break;
		}
		if (strcmp(key, newkey) != 0) {
			cout <<"Fegla Won" <<endl;
			continue;
		}
		res = 0;
		FOR(i, 0, m) {
			sort(cnt[i], cnt[i] + n);
			int x = 1, move;
			sleft[0] = 0;
			FOR(j, 1, n) sleft[j] = sleft[j - 1] + (cnt[i][j] - cnt[i][j - 1]) * (x++);
			x = 1;
			move = sleft[n - 1];
			sright[n - 1] = 0;
			_FOR(j, n - 2, 0) {
				sright[j] = sright[j + 1] + (cnt[i][j + 1] - cnt[i][j]) * (x++);
				move = min(move, sleft[j] + sright[j]);
			}
			res += move;
		}
		cout <<res <<endl;
	}
	return 0;

}
