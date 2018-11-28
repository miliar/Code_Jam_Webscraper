#include <bits/stdc++.h> 

using namespace std;

typedef long long ll; 
typedef pair<int, int> pii;

#define REP(i,n) for(int(i)=0;(i)<(int)(n);(i)++)

int r,c;
int mate[110];
int tmate[110];
int board[110][110];

void read() {
	scanf("%d %d", &r, &c);
	REP(i, r+c) {
		int pa, pb;
		scanf("%d %d", &pa, &pb);
		pa--;
		pb--;
		mate[pa]=pb;
		mate[pb]=pa;
	}
}

bool inside(int rr, int cc) {
	return 0 <= rr && rr < r && 0 <= cc && cc < c;
}

int convert(int rr, int cc) {
	//printf("converting %d %d\n", rr,cc);
	if (rr == -1) {
		return cc;
	}
	if (cc == c) {
		return c + rr;
	}
	if (rr == r) {
		return r + c + (c-cc-1); 
	}
	if (cc == -1) {
		return r + c + c + (r-rr-1);
	}
}

// 1 == /
int dfs(int y, int x, int dy, int dx) {
	//printf("dfs %d %d %d %d\n", y,x,dy,dx);
	if (!inside(y,x)) return convert(y,x);

	if (dy == 1) {
		dy = 0;
		if (board[y][x] == 1) dx = -1;
		else dx = 1;
	}
	else if (dy == -1) {
		dy = 0;
		if (board[y][x] == 1) dx = 1;
		else dx = -1;
	}

	else if (dx == 1) {
		dx = 0;
		if (board[y][x] == 1) dy = -1;
		else dy = 1;
	}
	else if (dx == -1) {
		dx = 0;
		if (board[y][x] == 1) dy = 1;
		else dy = -1;
	}

	return dfs(y+dy, x+dx, dy, dx);
}


void solve() {
	printf("\n");

	int boardsize = r*c;

	bool found = false;
	for (int bm = 0; bm < (1<<boardsize); bm++) {
		int idx = 0;
		REP(i,r) REP(j,c) {
			board[i][j] = !!(bm & (1<<idx));
			idx++;
		}


		bool good = true;
		for (int i = 0; i < 2*(r+c); i++) {
			int ti = i;

			if (ti < c) {
				tmate[i] = dfs(0,ti,1,0);
			}
			else {
				ti -= c;
				if (ti < r) {
					tmate[i] = dfs(ti,c-1,0,-1);
				}
				else {
					ti -= r;
					if (ti < c) {
						tmate[i] = dfs(r-1,c-1-ti,-1,0);
					}
					else {
						ti -= c;
						tmate[i] = dfs(r-1-ti,0,0,1);
					}
				}
			}

			//printf("tmate[%d]= %d\n", i, tmate[i]);

			if (mate[i] != tmate[i]) good = false;
		}

		if (good) {
			found = true;

			REP(i,r) {
				REP(j,c) {
					if (board[i][j] == 0) printf("\\");
					else printf("/");
				}
				printf("\n");
			}

			break;
		}
	}

	if (!found) printf("IMPOSSIBLE\n");
}


























int myMod = 0;
int howMany = 1;

int main(int argc, char** argv) {
	if (argc > 1) {
		stringstream ss; ss << argv[1]; ss >> myMod;
		ss.str(""); ss.clear();
		ss << argv[2]; ss >> howMany;
	}

	int cases;
	scanf("%d", &cases);
	for (int i = 0; i < cases; i++) {
		read();
		if (i % howMany == myMod) {
			printf("Case #%d: ", i+1);
			solve();
		}
	}
}