#include <cstdio>
#include <cstring>


int R, C, M;
char map[55][55];
bool vis[55][55];
int rem;
int dx[] = {-1, -1, -1, 0, 0, 1,1,1};
int dy[] = {-1, 0, 1, -1, 1, -1,0,1};

bool cango(int r, int c) {
	return r >= 0 & r < R && c >=0 && c < C;
}

void pmap(int x, int click)
{
	for (int i = 0; i < R*C; i++) {
		if (x & (1<<i)) putchar('*');
		else if (i == click) putchar('c');
		else putchar('.');
		if (i % C == C-1) putchar('\n');
	}
	return;
}
bool zero(int r, int c) {
	//printf ("zeroing %d %d\n", r,c);
	int a = 0, b=0;
	for (int k = 0; k < 8; k++) {
		if (cango(r+dx[k],c+dy[k])) {
			a++;
			//printf ("a++ at %d %d\n",r+dx[k],c+dy[k]);
		}
		if (cango(r+dx[k],c+dy[k]) && map[r+dx[k]][c+dy[k]] == '.') {
			b++;
			//printf ("b++ at %d %d\n",r+dx[k],c+dy[k]);
		}
	}
	if (a == b) return true;
	return false;
}


void dfs(int r, int c) {
	vis[r][c] = 1;
	rem--;
	bool ret = zero(r,c);
	//printf ("zero r = %d c = %d is %d\n",r,c,ret);
	if (ret) {
		for (int k = 0; k < 8; k++) {
			if (cango(r+dx[k],c+dy[k]) && !vis[r+dx[k]][c+dy[k]]) {
				dfs(r+dx[k],c+dy[k]);
			}
		}
	}
}

int can(int x) {
	for (int i = 0; i < R*C; i++) {
		if (x & (1<<i)) map[i/C][i%C] = '*';
		else map[i/C][i%C] ='.';
	}

	for (int r = 0; r < R; r++)
		for (int c = 0; c < C; c++)
			if (map[r][c] =='.') {
				memset(vis, 0, sizeof(vis));
				//printf ("try r = %d c = %d\n", r,c);
				//pmap(x, -1);
				rem = R*C-M;
				dfs(r,c);
				//printf ("rem = %d\n", rem);
				if (rem == 0) return r*C+c;
			}
	return -1;
}

int count(int x) {
	int ret = 0;
	while (x) {
		if (x & 1) ret++;
		x/=2;
	}
	return ret;
}


int main()
{
	int T; scanf ("%d", &T);
	for (int cc=1; cc<=T; cc++) {
		scanf ("%d %d %d", &R, &C, &M);
		int N = R*C, ret = -1, click = -1;
		for (int i = 0; i < (1<<N); i++) {
			if (count(i) == M) {
				//printf ("i = %d\n", i);
				click = can(i);
				if (click != -1) {
					ret = i; 
					break;
				}
			}
		}
		printf ("Case #%d:\n", cc);
		if (ret != -1) {
			pmap(ret,click);
		} else {
			printf ("Impossible\n");	
		}
	}
	return 0;
}
