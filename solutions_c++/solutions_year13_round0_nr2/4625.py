#include "std.h"
#include <string.h>

int mat[100][100];
char buf[1024];

int main() {
    int T;
    cin >> T; cin.getline(buf, sizeof buf);
    FOR(tt, T) {
	ZERO(mat);
	int full = 1;
	int Y, X;
	cin >> Y >> X; cin.getline(buf, sizeof buf);
	FOR(y, Y)
	{
	    FOR(x, X) cin >> mat[y][x];
	    cin.getline(buf, sizeof buf);
	}
	int hy[100], hx[100];
	FOR(y, Y) hy[y] = 1;
	FOR(x, X) hx[x] = 1;
	FOR(y, Y) FOR(x, X) hy[y] = max(hy[y], mat[y][x]), hx[x] = max(hx[x], mat[y][x]);
	int bad = 0;
	FOR(y, Y) FOR(x, X)
	{
	    int h = min(hy[y], hx[x]);
	    if (mat[y][x] < h) bad = 1;
	}
	cout << "Case #"<<(tt+1)<<": ";
	cout << (bad ? "NO" : "YES");
    end:
	cout << endl;
    }
    return 0;
}
