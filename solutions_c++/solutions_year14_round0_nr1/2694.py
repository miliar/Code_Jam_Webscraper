#pragma warning(disable:4996)
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
#include<vector>
#include<cmath>
#include<cstdio>
using namespace std;



int mat1[4][4];
int mat2[4][4];
int ans1, ans2;
int main()
{
	freopen("A-small-attempt0.in.txt", "r", stdin);
	freopen("A-small-attempt0.out.txt", "w", stdout);
	int T; cin >> T; int ca = 0;
	while (T--){
		scanf("%d", &ans1);
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				scanf("%d", &mat1[i][j]);
			}
		}
		scanf("%d", &ans2);
		ans1--; ans2--;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				scanf("%d", &mat2[i][j]);
			}
		}
		int num = 0, res = -1;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				if (mat1[ans1][i] == mat2[ans2][j]){
					num++; res = mat1[ans1][i];
				}
			}
		}
		if (num == 1){
			printf("Case #%d: %d\n", ++ca, res);
		}
		else if (num == 0){
			printf("Case #%d: Volunteer cheated!\n", ++ca);
		}
		else{
			printf("Case #%d: Bad magician!\n", ++ca, res);
		}
	}
	return 0;
}