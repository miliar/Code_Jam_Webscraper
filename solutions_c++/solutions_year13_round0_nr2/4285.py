
#include <map>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <iostream>
#include <sstream>
#include <assert.h>
#include <cstring>

using namespace std;

#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define REPD(i,n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset(x,0,sizeof x);
#define CLEARA(x) memset(&x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define FILLA(x,v) memset(&x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())

#define INPUT_FILE_NAME "B-large"
#define OUTPUT_FILE_NAME "a"

//lawn[i][j] > min(max(lawn.col[i]), max(lawn.row[j]))

int lawn[105][105];
int maxRow[105];
int maxCol[105];

void solveCase(){
	int width, height;
	scanf("%d", &height);
	scanf("%d", &width);
	REP(i, height) {
		REP(j, width) {
			scanf("%d", &(lawn[i][j]));
		}
	}

	CLEAR(maxRow);
	CLEAR(maxCol);

	REP(i, height) {
		REP(j, width) {
			maxRow[i] = max(maxRow[i], lawn[i][j]);
			maxCol[j] = max(maxCol[j], lawn[i][j]);
		}
	}

	REP(i, height) {
		REP(j, width) {
			if(lawn[i][j] < maxRow[i] && lawn[i][j] < maxCol[j]) {
				printf("%s", "NO");
				return;
			}
		}
	}
	printf("%s", "YES");

}

int main() {
	freopen(INPUT_FILE_NAME ".in","r",stdin);
	freopen(OUTPUT_FILE_NAME ".out","w",stdout);
	int caseAmount;
	scanf("%d", &caseAmount);
	for (int caseNumber = 1; caseNumber <= caseAmount; ++caseNumber) {
		printf("Case #%d: ", caseNumber);

		solveCase();

		printf("\n");
	}
	return 0;
}
