#include <stdio.h>
#include <vector>

using namespace std;


bool checkCol(vector < vector <int> > grass, vector < vector <bool> > *isLawned, int col, int N) {
	bool flag = true;
	int curr;

	int j = 1;
	curr = grass[0][col];
	while (j < N && flag) {
		if (curr != grass[j][col]) {
			flag = false;
			break;
                }
		curr = grass[j][col];
		j++;
	}
	
	if (!flag) {
		flag = true;
                for (int j = 0; j < N ; j++) {
			if (!((*isLawned)[j][col]) && grass[j][col] == 1)
				flag = false;
		}
        }

	return flag;
}

void checkRow(vector < vector <int> > grass, vector < vector <bool> > *isLawned, int row, int M) {

	int curr;
	bool flag = true;
	
	curr = grass[row][0];
	int j = 1;
	while (j < M && flag) {
		if (curr != grass[row][j]) {
			flag = false;
		}
		curr = grass[row][j];
		j++;
	}

	if (flag) {
		for (int j = 0; j < M; j++)
			(*isLawned)[row][j] = true;
	}
}

int main() 
{
	int tests, N, M;
	bool flag;

	scanf("%d\n", &tests);	


	for (int i = 1; i <= tests; i++) {
		flag = true;
		scanf("%d %d\n", &N, &M);
		vector< vector<int> > grass(N, vector<int> (M));
		vector< vector<bool> > isLawned(N, vector<bool> (M));
		for (int j = 0; j < N; j++) {
		    for (int k = 0; k < M; k++) 
			scanf("%d", &grass[j][k]);
		}
		int j = 0;
		while (j < N) {
			checkRow(grass, &isLawned, j, M);
			j++;	
		}
		j = 0;
		while (j < M && flag) {
			flag = checkCol(grass, &isLawned, j, N);
			j++;
		}
		
		printf("Case #%d: %s\n", i, flag ? "YES" : "NO");
	}
	return 0;
}
