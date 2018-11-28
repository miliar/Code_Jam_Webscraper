#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
using namespace std;

int mat1[4][4], mat2[4][4];
int row1, row2;
int main()
{
	freopen("A--small-attempt0.in", "r", stdin);
	freopen("A--small-attempt0.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		scanf("%d", &row1);
		row1--;
		for (int i=0; i<4; i++) {
			for (int j=0; j<4; j++) {
				scanf("%d", &mat1[i][j]);
			}
		}
		scanf("%d", &row2);
		row2--;
		for (int i=0; i<4; i++) {
			for (int j=0; j<4; j++) {
				scanf("%d", &mat2[i][j]);
			}
		}
		vector<int> v;
		for (int i=0; i<4; i++) {
			for (int j=0; j<4; j++) {
				if (mat1[row1][i] == mat2[row2][j]) {
					v.push_back(mat1[row1][i]);
				}
			}
		}
		printf("Case #%d: ", t);
		if (v.size() == 0) {
			printf("Volunteer cheated!\n");
		} else if (v.size() == 1) {
			printf("%d\n", v[0]);
		} else {
			printf("Bad magician!\n");
		}
	}
	return 0;
}