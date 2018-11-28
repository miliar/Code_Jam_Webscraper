#include <algorithm>
#include <climits>
#include <cmath>
#include <cstring>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;


int main(void)
{
	FILE* fin = fopen("B-large.in", "r");
	FILE* fout = fopen("B-large.out", "w");

	int numTests;
	fscanf(fin, "%d\n", &numTests);

	for(int testIndex=0;testIndex<numTests;testIndex++)
	{
		int numRows, numCols;
		fscanf(fin, "%d %d", &numRows, &numCols);

		int lawn[101][101];
		for(int r=0;r<numRows;r++)
			for(int c=0;c<numCols;c++)
				fscanf(fin, "%d\n", &lawn[r][c]);

		bool ok = true;
		for(int r=0;r<numRows && ok;r++) {
			for(int c=0;c<numCols && ok;c++) {

				int hBlocked = 0;
				int vBlocked = 0;

				for(int nr=r;nr>=0;nr--)
					if(lawn[nr][c] > lawn[r][c]) {
						vBlocked++;
						break;
					}

				for(int nr=r;nr<numRows;nr++)
					if(lawn[nr][c] > lawn[r][c]) {
						vBlocked++;
						break;
					}

				for(int nc=c;nc>=0;nc--)
					if(lawn[r][nc] > lawn[r][c]) {
						hBlocked++;
						break;
					}

				for(int nc=c;nc<numCols;nc++)
					if(lawn[r][nc] > lawn[r][c]) {
						hBlocked++;
						break;
					}

				if(hBlocked != 0 && vBlocked != 0)
					ok = false;
			}
		}

		fprintf(fout, "Case #%d: ", testIndex+1);
		if(ok == false)
			fprintf(fout, "NO");
		else
			fprintf(fout, "YES");
		fprintf(fout, "\n");
	}

	fclose(fin);
	fclose(fout);
}
