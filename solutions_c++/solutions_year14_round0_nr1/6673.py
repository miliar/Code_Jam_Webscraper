#include <sstream>
#include <string>
#include <cstdio>
using namespace std;

void readCase(int grid[4], int line, int row) {

	char work[20];
	int rLine;

	scanf("%d", &rLine);
	for( int i = 1; i <= line; ++i) {
		if (rLine == i ) {
			scanf("%d %d %d %d", &grid[0], &grid[1], 
							  &grid[2], &grid[3]);
		} else {
			scanf("%s", work);
			scanf("%s", work);
			scanf("%s", work);
			scanf("%s", work);
		}	
	}
	return;
}

string itoStr(int in)
{
	stringstream wk;
	
	wk << in;
	return wk.str();
}

string check(int grid[2][4])
{
	int matchCount = 0;
	int tmp;

	for(int i = 0; i < 4; ++i) {
		for(int j = 0; j < 4; ++j) {
			if(grid[0][i] == grid[1][j]) {
				matchCount++;
				tmp = i;
			}
		}
	}

	switch( matchCount ) {
	case 0:
		return "Volunteer cheated!";

	case 1:
		return itoStr(grid[0][tmp]);

	default:
		return "Bad magician!";
	}
		
}

void body(int counter) {

	int grid[2][4];
	printf("Case #%d: ", counter);

	readCase(&grid[0][0], 4, 0);
	readCase(&grid[1][0], 4, 1);

	printf("%s\n", check(grid).c_str());
	return;
}

int main() {
	int counter = 0;
	int loop; scanf("%d",&loop);
	while(loop--) {
		body(++counter);
	}
	return 0;
}
