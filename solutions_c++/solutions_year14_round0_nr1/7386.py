#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<cmath>
#include<list>
#include<string>
#include<set>
#include<map>
#include<iomanip>
#include<sstream>
#include<string.h>
#include<math.h>
#include<functional>
#include<deque>
#include<fstream>
#define eps 1e-9
using namespace std;

int main(){
	freopen("test.txt", "r", stdin);
	freopen("problem1Sol.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int k = 1; k <= t; ++k){
		int ans1, ans2, mat1[4][4], mat2[4][4];
		scanf("%d", &ans1);
		for (int i = 0; i < 4; ++i){
			for (int j = 0; j < 4; ++j){
				scanf("%d", &mat1[i][j]);
			}
		}
		scanf("%d", &ans2);
		for (int i = 0; i < 4; ++i){
			for (int j = 0; j < 4; ++j){
				scanf("%d", &mat2[i][j]);
			}
		}
		vector<int> res;
		for (int i = 0; i < 4; ++i){
			for (int j = 0; j < 4; ++j){
				if (mat1[ans1 - 1][i] == mat2[ans2 - 1][j]) {
					res.push_back(mat1[ans1 - 1][i]);
				}
			}
		}
		if (res.size() == 1) printf("Case #%d: %d\n", k, res[0]);
		else if (res.size() == 0) printf("Case #%d: Volunteer cheated!\n", k);
		else printf("Case #%d: Bad magician!\n", k);
	}
	return 0;
}