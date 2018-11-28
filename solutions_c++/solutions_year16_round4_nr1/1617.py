#include <stdio.h>
#include <iostream>

using namespace std;

int N, R, P, S;

// P R S
char winArrange[4096*3];
bool gotans;
char tmp[2][4096*3];

bool win_r(int tmpno, int n, int p, int r, int s)
{
	int newtmpno = 1 - tmpno;
	if (n == 1<<N) {
		// done
		if (p || r || s) {
			printf("ERR2 %d %d %d\n", p, r, s);
			exit(-1);
		}
		if (!gotans) {
change:
			for (int i=0; i<(1<<N); ++i)
				winArrange[i] = tmp[tmpno][i];
			winArrange[(1<<N)] = 0;
		} else {
			bool better = false;
			for (int i=0; i<(1<<N) && !better; ++i) {
				if (tmp[tmpno][i] < winArrange[i])
					better = true;
			}
			if (better)
				goto change;
		}
		gotans = true;
		return true;
	}
	for (int i=0; i<n; ++i) {
		switch (tmp[tmpno][i]){
		case 'P':
			if (r == 0) return false;
			break;
		case 'R':
			if (s == 0) return false;
			break;
		case 'S':
			if (p == 0) return false;
			break;
		default:
			printf("ERR\n");
			exit(-1);
		}
	}
	for (int i=0; i<n; ++i) {
		switch (tmp[tmpno][i]){
		case 'P':
			if (r == 0) return false;
			r--;
			tmp[newtmpno][i*2] = 'P';
			tmp[newtmpno][i*2 + 1] = 'R';
			win_r(newtmpno, n*2, p, r, s);
			tmp[newtmpno][i*2] = 'R';
			tmp[newtmpno][i*2 + 1] = 'P';
			win_r(newtmpno, n*2, p, r, s);
			r++;
			break;
		case 'R':
			if (s == 0) return false;
			s--;
			tmp[newtmpno][i*2] = 'R';
			tmp[newtmpno][i*2 + 1] = 'S';
			win_r(newtmpno, n*2, p, r, s);
			tmp[newtmpno][i*2] = 'S';
			tmp[newtmpno][i*2 + 1] = 'R';
			win_r(newtmpno, n*2, p, r, s);
			s++;
			break;
		case 'S':
			if (p == 0) return false;
			p--;
			tmp[newtmpno][i*2] = 'P';
			tmp[newtmpno][i*2 + 1] = 'S';
			win_r(newtmpno, n*2, p, r, s);
			tmp[newtmpno][i*2] = 'S';
			tmp[newtmpno][i*2 + 1] = 'P';
			win_r(newtmpno, n*2, p, r, s);
			p++;
			break;
		default:
			printf("ERR\n");
			exit(-1);
		}
	}
	return true;
}

void winR()
{
	if (R == 0) return;
	tmp[0][0] = 'R';
	win_r(0, 1, P, R-1, S);
}
void winP()
{
	if (P == 0) return;
	tmp[0][0] = 'P';
	win_r(0, 1, P-1, R, S);
}

void winS()
{
	if (S == 0) return;
	tmp[0][0] = 'S';
	win_r(0, 1, P, R, S-1);
}


char win[15][4096*3];
char get(char a, int b)
{
	if (a == b) return 0;
	switch (a) {
	case 'P':
		if (b == 'R') return a;
		return b;
	case 'R':
		if (b == 'S') return a;
		return b;
	case 'S':
		if (b == 'P') return a;
		return b;
	}
	return 0;
}

bool ok(int posn)
{
	int i = 0;
	while (posn) {
		int upn = posn / 2;
		if (posn % 2 == 0)
			return true;
		win[i+1][upn] = get(win[i][posn-1], win[i][posn]);
		if (win[i+1][upn] == 0)
			return false;
		posn = upn;
		i++;
	}
	return true;
}
bool gen(int n, int p, int r, int s)
{
	if (p < 0 || r < 0 || s < 0) return false;
	if (n == 1<<N) {
		return true;
	}
	if (p && r) {
		win[0][n] = 'P';
		win[0][n+1] = 'R';
		if (ok(n+1)) {
			if (gen(n+2, p-1, r-1, s))
				return true;
		}
	}
	if (p && s) {
		win[0][n] = 'P';
		win[0][n+1] = 'S';
		if (ok(n+1)) {
			if (gen(n+2, p-1, r, s-1))
				return true;
		}
	}
	if (r && s) {
		win[0][n] = 'R';
		win[0][n+1] = 'S';
		if (ok(n+1)) {
			if (gen(n+2, p, r-1, s-1))
				return true;
		}
	}
	return false;
}

void solve(int no)
{
	cin >> N >> R >> P >> S;
	/*
	gotans = false;
	winR();
	winP();
	winS();
	if (!gotans)
	*/
	if (gen(0, P, R, S)) {
		win[0][1<<N] = 0;
		printf("Case #%d: %s\n", no, win[0]);
	} else
		printf("Case #%d: IMPOSSIBLE\n", no);
}

int main()
{
	int T;
	cin >> T;
	for (int i=1; i<=T; ++i)
		solve(i);
	return 0;
}
