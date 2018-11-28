#include <cstdio>
#include <algorithm>
using namespace std;
int T, N;
char C[5][5];

bool pic4[10][5][5] =
{{{1, 1, 1, 1}, 
  {1, 1, 1, 1}, 
  {1, 1, 1, 1},
  {1, 1, 1, 1}}, 
 {{1, 1, 1, 0}, 
  {1, 1, 1, 0}, 
  {1, 1, 1, 0},
  {0, 0, 0, 1}}, 
 {{1, 1, 0, 0}, 
  {1, 1, 0, 0}, 
  {0, 0, 1, 1},
  {0, 0, 1, 1}}, 
 {{1, 1, 0, 0}, 
  {1, 1, 0, 0}, 
  {0, 0, 1, 0},
  {0, 0, 0, 1}}, 
 {{1, 0, 0, 0}, 
  {0, 1, 0, 0}, 
  {0, 0, 1, 0},
  {0, 0, 0, 1}}};

bool pic3[10][5][5] =
{{{1, 1, 1}, 
  {1, 1, 1}, 
  {1, 1, 1}}, 
 {{1, 1, 0}, 
  {1, 1, 0}, 
  {0, 0, 1}},  
 {{1, 0, 0}, 
  {0, 1, 0}, 
  {0, 0, 1}}};
  
int row3[6][5] = {{0, 1, 2}, {0, 2, 1}, {1, 0, 2}, {1, 2, 0}, {2, 0, 1}, {2, 1, 0}};
int row4[24][5] = {{0, 1, 2, 3}, {0, 1, 3, 2}, {0, 2, 1, 3}, {0, 2, 3, 1}, {0, 3, 1, 2}, {0, 3, 2, 1}, {1, 0, 2, 3}, {1, 0, 3, 2}, {1, 2, 0, 3}, {1, 2, 3, 0}, {1, 3, 0, 2}, {1, 3, 2, 0}, 
                   {2, 0, 1, 3}, {2, 0, 3, 1}, {2, 1, 0, 3}, {2, 1, 3, 0}, {2, 3, 0, 1}, {2, 3, 1, 0}, {3, 0, 1, 2}, {3, 0, 2, 1}, {3, 1, 0, 2}, {3, 1, 2, 0}, {3, 2, 0, 1}, {3, 2, 1, 0}};

void check3 (char C[][5], int x, int y, int &low){
	for (int i = 0; i < 3; i++){
		int cnt = 0;
		for (int j = 0; j < 3; j++){
			for (int k = 0; k < 3; k++){
				if (C[j][k] == '0' && pic3[i][row3[x][j]][row3[y][k]] == 1){
					cnt++;
				} else if (C[j][k] == '1' && pic3[i][row3[x][j]][row3[y][k]] == 0){
					cnt = 9;
				}
			}
		}
		if (cnt < low){
			low = cnt;
		}
	}
}

void check4 (char C[][5], int x, int y, int &low){
	for (int i = 0; i < 5; i++){
		int cnt = 0;
		for (int j = 0; j < 4; j++){
			for (int k = 0; k < 4; k++){
				if (C[j][k] == '0' && pic4[i][row4[x][j]][row4[y][k]] == 1){
					cnt++;
				} else if (C[j][k] == '1' && pic4[i][row4[x][j]][row4[y][k]] == 0){
					cnt = 16;
				}
			}
		}
		if (cnt < low){
			low = cnt;
		}
	}
}

int main (){
	freopen ("D-small-attempt1.in", "r", stdin);
	freopen ("D-small-attempt1.out", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; i++){
		scanf("%d\n", &N);
		int cnt = 0;
		for (int j = 0; j < N; j++){
			for (int k = 0; k < N; k++){
				scanf("%c", &C[j][k]);
				cnt += C[j][k] - '0';
			}
			scanf("\n");
		}
		if (N == 1){
			printf ("Case #%d: %d\n", i, 1 - (C[0][0] - '0'));
		} else if (N == 2){
			if (cnt == 0){
				printf("Case #%d: 2\n", i);
			} else if (cnt == 1 || cnt == 3){
				printf("Case #%d: 1\n", i);
			} else if (cnt == 2){
				if (C[0][0] == '1' && C[1][1] == '1')
					printf("Case #%d: 0\n", i);
				else if (C[0][1] == '1' && C[1][0] == '1')
					printf("Case #%d: 0\n", i);
				else 
					printf("Case #%d: 2\n", i);
			} else if (cnt == 4){
				printf("Case #%d: 0\n", i);
			}
		} else if (N == 3){
			int low = 9;
			for (int x = 0; x < 6; x++){
				for (int y = 0; y < 6; y++){
					check3 (C, x, y, low);
				}
			}
			printf("Case #%d: %d\n", i, low);
		} else if (N == 4){
			int low = 16;
			for (int x = 0; x < 24; x++){
				for (int y = 0; y < 24; y++){
					check4 (C, x, y, low);
				}
			}
			printf("Case #%d: %d\n", i, low);
		}
	}
	fclose (stdin);
	fclose (stdout);
	return 0;
}
