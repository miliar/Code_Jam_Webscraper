#include <iostream>

using namespace std;

#define	For(i, a, b)	for(int i = (a) ; i < (b) ; ++i)
#define	rep(i, n)		For(i, 0, (n))

bool solve()
{
	int		N, M;
	int		field[110][110];

	cin >> N >> M;
	rep(i, N)
		rep(j, M)
			cin >> field[i][j];

	rep(i, N) {
		rep(j, M) {
			rep(k, N)
				if(field[i][j] < field[k][j])
					goto Next;
			continue;
Next:
			rep(k, M)
				if(field[i][j] < field[i][k])
					return false;
		}
	}
	return true;
}

int main()
{
	int		T;
	cin >> T;
	rep(i, T)
		cout << "Case #" << (i + 1) << ": " << (solve() ? "YES" : "NO") << endl;
}

