#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <climits>
#include <cstring>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#define FOR(i,a,b) for(int i=int(a); i<int(b); ++i)
#define FORD(i,a,b) for(int i=int(a)-1; i>=int(b); --i)
#define FORE(i,q) for(typeof((q).begin()) i=(q).begin(); i!=(q).end(); ++i)
using namespace std;

typedef long long LG;
typedef long double LD;

struct board {
	int r, c;
	char t[6][6];
} B[51];

void preproc() {
	B[ 1   ] = (board){1, 1, { "c" }};
	B[ 2   ] = (board){1, 2, { "c." }};
	B[ 3   ] = (board){1, 3, { "c.." }};
	B[ 4   ] = (board){2, 2, { "c.", ".." }};
	B[ 4+25] = (board){1, 4, { "c..." }};
	B[ 5   ] = (board){1, 5, { "c...." }};
	B[ 6   ] = (board){2, 3, { "c..", "..." }};
	B[ 8   ] = (board){2, 4, { "c...", "...." }};
	B[ 8+25] = (board){3, 3, { "c..", "...", "..*" }};
	B[ 9   ] = (board){3, 3, { "c..", "...", "..." }};
	B[10   ] = (board){2, 5, { "c....", "....." }};
	B[10+25] = (board){3, 4, { "c...", "....", "..**" }};
	B[11   ] = (board){3, 4, { "c...", "....", "...*" }};
	B[12   ] = (board){3, 4, { "c...", "....", "...." }};
	B[13   ] = (board){3, 5, { "c....", ".....", "...**" }};
	B[13+25] = (board){4, 4, { "c...", "....", "...*", "..**" }};
	B[14   ] = (board){3, 5, { "c....", ".....", "....*" }};
	B[14+25] = (board){4, 4, { "c...", "....", "....", "..**" }};
	B[15   ] = (board){3, 5, { "c....", ".....", "....." }};
	B[15+25] = (board){4, 4, { "c...", "....", "....", "...*" }};
	B[16   ] = (board){4, 4, { "c...", "....", "....", "...." }};
	B[17   ] = (board){4, 5, { "c....", ".....", "....*", "...**" }};
	B[18   ] = (board){4, 5, { "c....", ".....", ".....", "...**" }};
	B[19   ] = (board){4, 5, { "c....", ".....", ".....", "....*" }};
	B[20   ] = (board){4, 5, { "c....", ".....", ".....", "....." }};
	B[21   ] = (board){5, 5, { "c....", ".....", ".....", "...**", "...**" }};
	B[22   ] = (board){5, 5, { "c....", ".....", ".....", "....*", "...**" }};
	B[23   ] = (board){5, 5, { "c....", ".....", ".....", ".....", "...**" }};
	B[24   ] = (board){5, 5, { "c....", ".....", ".....", ".....", "....*" }};
	B[25   ] = (board){5, 5, { "c....", ".....", ".....", ".....", "....." }};
}

void testcase(int zzz) {
	int r, c, m;
	bool change = false;
	scanf("%d%d%d", &r, &c, &m);
	if(r > c) {
		swap(r, c);
		change = true;
	}
	int a = r * c - m;
	if(r != 1 && (a == 2 || a == 3 || a == 5 || a == 7)) {
		printf("Case #%d:\nImpossible\n", zzz);
		return;
	}
	if(r == 2 && a == 9) {
		printf("Case #%d:\nImpossible\n", zzz);
		return;
	}
	printf("Case #%d:\n", zzz);
	if(r < B[a].r || c < B[a].c) a += 25;
	//printf("--------- r:%d c:%d\n", B[a].r, B[a].c);
	if(!change) {
		FOR(i,0,r) {
			FOR(j,0,c) {
				if(i < B[a].r && j < B[a].c)
					printf("%c", B[a].t[i][j]);
				else
					printf("*");
			}
			printf("\n");
		}
	} else {
		FOR(i,0,c) {
			FOR(j,0,r) {
				if(j < B[a].r && i < B[a].c)
					printf("%c", B[a].t[j][i]);
				else
					printf("*");
			}
			printf("\n");
		}
	}
}

int main() {
	preproc();
	int ZZZ; scanf("%d", &ZZZ);
	FOR(zzz,0,ZZZ) testcase(zzz + 1);
	return 0;
}
