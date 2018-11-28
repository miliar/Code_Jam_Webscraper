#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>
using namespace std;

typedef long long LL;
typedef vector<int> VI;

#define REP(i,n) for(int i=0, i##_len=(n); i<i##_len; ++i)
#define EACH(i,c) for(__typeof((c).begin()) i=(c).begin(),i##_end=(c).end();i!=i##_end;++i)
#define eprintf(s...) fprintf(stderr, s)

template<class T> inline void amin(T &a, const T &b) { if (b<a) a=b; }
template<class T> inline void amax(T &a, const T &b) { if (a<b) a=b; }
const int dy[] = { 0, 1, 0, -1 };
const int dx[] = {  1, 0, -1 , 0};

int R, C;
char F[111][111];


void set_dir(char c, int &dy, int &dx) {
    dy = dx = 0;
    if (c == '^') dy = -1;
    if (c == '>') dx = 1;
    if (c == '<') dx = -1;
    if (c == 'v') dy = 1;
}


bool in(int y, int x) {
    return 0 <= y && y < R && 0 <= x && x < C;
}
int main() {
    int T;
    scanf("%d", &T);

    for (int tc=1; tc<=T; tc++) {
	scanf("%d%d", &R, &C);
	REP (i, R) scanf("%s", F[i]);
	
	int ans = 0;
	bool bad = false;
	REP (i, R) REP (j, C) {
	    if (F[i][j] != '.') {
		int ddy, ddx;
		bool b = false;
		set_dir(F[i][j], ddy, ddx);
		for (int k=1; ; k++) {
		    int y = i + k*ddy, x = j + k*ddx;
		    if (!in(y, x)) {
			b = true;
			break;
		    }
		    if (F[y][x] != '.') break;
		}

		if (b) {
		    REP (d, 4) {
			for (int k=1; ; k++) {
			    int y = i + k*dy[d], x = j + k*dx[d];
			    if (!in(y, x)) {
				break;
			    }
			    if (F[y][x] != '.') {
				b = false;
				break;
			    }
			}
		    }
		    if (b) bad = true;
		    else ans++;
		}
	    }
	}
	    
	printf("Case #%d: ", tc);
	if (bad) puts("IMPOSSIBLE");
	else printf("%d\n", ans);
    }
    return 0;
}
