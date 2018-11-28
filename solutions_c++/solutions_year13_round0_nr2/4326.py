
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int lawn[102][102];
int maxR[102];
int maxC[102];

int main() {

	int cases;
	scanf("%d\n", &cases);
	for (int caseNo=0; caseNo < cases; caseNo++) {

		for(int i=0; i<102; i++) {
			memset(lawn+i, 0, sizeof(int)*102);
		}
		memset(maxR, 0, sizeof(int)*102);
		memset(maxC, 0, sizeof(int)*102);

		int x,y;
		scanf("%d %d\n", &x, &y);

		for (int i=0; i<x; i++) {
			for (int j=0; j<y; j++) {
				scanf("%d ", lawn[i]+j);

				if (lawn[i][j] > maxR[i]) {maxR[i] = lawn[i][j];}
				if (lawn[i][j] > maxC[j]) {maxC[j] = lawn[i][j];}
			}
		}

		bool possible = true;
		for (int i=0; i<x; i++) {
			for (int j=0; j<y; j++) {
				
				if (lawn[i][j] != maxR[i] && lawn[i][j] != maxC[j]) {
					possible = false;
					break;
				}
			}
			if (!possible) {break;}
		}

		printf("Case #%d: %s\n", caseNo+1, (possible ? "YES" : "NO"));
	}

	return 0;
}
