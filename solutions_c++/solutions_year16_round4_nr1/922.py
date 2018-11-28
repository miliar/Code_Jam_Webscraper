#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

#define MAX_LEVEL 12

struct Comb
{
	int R, P, S;
	Comb(int r=0, int p=0, int s=0, string a="") { R=r; P=p; S=s; ans=a; }
	string ans;
};

Comb comb[3][MAX_LEVEL + 1];

int N, R, P, S;

Comb build(Comb& win, Comb& lose)
{
	Comb result = Comb(win.R + lose.R, win.P + lose.P, win.S + lose.S);
	if (win.ans < lose.ans) {
		result.ans = win.ans + lose.ans;
	} else {
		result.ans = lose.ans + win.ans;
	}
	return result;
}

void gen()
{
	comb[0][0] = Comb(1, 0, 0, "R");
	comb[1][0] = Comb(0, 1, 0, "P");
	comb[2][0] = Comb(0, 0, 1, "S");

	for (int i=1;i<=MAX_LEVEL;++i) {
		for (int w=0;w<3;++w) {
			comb[0][i] = build(comb[0][i-1], comb[2][i-1]);
			comb[1][i] = build(comb[1][i-1], comb[0][i-1]);
			comb[2][i] = build(comb[2][i-1], comb[1][i-1]);
		}
	}
}

void solv()
{
	for (int w=0;w<3;++w) {
		if (comb[w][N].R == R && 
			comb[w][N].P == P && 
			comb[w][N].S == S) {
			
			printf("%s\n", comb[w][N].ans.c_str());
			return;
		}
	}
	printf("IMPOSSIBLE\n");
}

int main()
{
	gen();
	
	int T;
	cin >> T;
	for (int nCase = 1; nCase <= T; ++nCase) {
		cin >> N >> R >> P >> S;
		printf("Case #%d: ", nCase);
		solv();
	}
	return 0;
}