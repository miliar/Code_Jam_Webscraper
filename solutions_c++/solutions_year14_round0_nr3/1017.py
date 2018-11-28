#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

int dr[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dc[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

struct Board {
	int b[32], nbr[32];
	int nr, nc;
	Board() {}
	Board(int r, int c):nr(r), nc(c) {
		memset(b, 0, sizeof(b));
	}
	inline int id(int r, int c) { return r*nc+c; }
	inline char get(int r, int c) {
		return (0<=r && r<nr && 0<=c && c<nc) ? b[id(r,c)] : 0;
	}
	int getNbrMines(int r, int c) {
		return nbr[id(r,c)];
	}
	void buildNbr() {
		memset(nbr, 0, sizeof(nbr));
		for(int r = 0; r < nr; ++r) for(int c = 0; c < nc; ++c)
			for(int i = 0; i < 8; ++i)
				nbr[id(r,c)] += get(r+dr[i], c+dc[i]);
		for(int r = 0; r < nr; ++r) for(int c = 0; c < nc; ++c)
			if(get(r,c) == 1) nbr[id(r,c)] = -1;
	}
	int bfs(int r, int c) {
		int qr[32] = {r}, qc[32] = {c}, qh = 0, qt = 1;
		int vst[32] = {0}, cnt = 1;
		vst[id(r,c)] = 1;
		for(; qh < qt; ++qh) {
			r = qr[qh], c = qc[qh];
			for(int i = 0; i < 8; ++i) {
				int xr = r+dr[i], xc = c+dc[i];
				if(xr<0 || xr>=nr || xc<0 || xc>=nc) continue;
				if(get(xr,xc)==1 || vst[id(xr,xc)]) continue;
				++cnt;
				vst[id(xr,xc)] = 1;
				if(getNbrMines(xr,xc) == 0) {
					qr[qt] = xr, qc[qt] = xc;
					++qt;
				}
			}
		}
		return cnt;
	}
	void output(int cr, int cc) {
		for(int r = 0; r < nr; ++r) {
			for(int c = 0; c < nc; ++c)
				if(r == cr && c == cc) putchar('c');
				else putchar(get(r,c)?'*':'.');
			putchar('\n');
		}
	}
};

int oneclick(Board &brd, int M) {
	brd.buildNbr();
	int n1 = 0, res = -1, nspace = brd.nr*brd.nc - M;
	for(int r = 0; r < brd.nr; ++r) for(int c = 0; c < brd.nc; ++c) {
		int nbr = brd.getNbrMines(r, c);
		if(nbr > 0) ++n1, res = r*brd.nc+c;
		else if(nbr == 0)
			return (brd.bfs(r,c) == nspace) ? r*brd.nc+c : -1;
	}
	return (n1==1) ? res : -1;
}

void gen(int R, int C, int M) {
	int n = R*C;
	Board brd(R, C);
	for(int i = n-M; i < n; ++i) brd.b[i] = 1;
	int res = -1;
	do {
		res = oneclick(brd, M);
	} while(res == -1 && next_permutation(brd.b, brd.b+n));
	if(res != -1) brd.output(res/C, res%C);
	else puts("Impossible");
}

int main() {
	int TT;
	scanf("%d", &TT);
	for(int T = 1;  T <= TT; ++T) {
		int r, c, m;
		scanf("%d %d %d", &r, &c, &m);
		printf("Case #%d:\n", T);
		gen(r, c, m);
	}
}

