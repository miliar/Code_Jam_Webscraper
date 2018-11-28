#define Rank_and_File

#ifdef Rank_and_File
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <vector>

using namespace std;

int main() {
	//freopen("in.txt", "rt", stdin);
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int T;
	scanf("%d\n", &T);

	for (int i = 1; i <= T; i++) {
		int N;
		scanf("%d\n", &N);
		int list[99][50];

		for (int j = 0; j < 2 * N - 1; j++) {
			for (int k = 0; k < N; k++) {
				scanf("%d", &list[j][k]);
			}
		}

		vector <vector <int *>> group;
		int count[99] = { 0 };
		for (int j = 0; j < N; j++) {
			int min = -1;
			int idx1 = -1;
			int idx2 = -1;
			for (int k = 0; k < 2 * N - 1; k++) {
				if (count[k] == 1)
					continue;
				else {
					if (min == -1) {
						min = list[k][j];
						idx1 = k;
						continue;
					}

					if (list[k][j] < min) {
						min = list[k][j];
						idx1 = k;
						idx2 = -1;
					}
					else if ((list[k][j] == min)) {
						idx2 = k;
					}
				}
			}

			vector <int*> member;
			count[idx1] = 1;
			member.push_back(list[idx1]);
			if (idx2 != -1) {
				count[idx2] = 1;
				member.push_back(list[idx2]);
			}
			group.push_back(member);
		}

		int ruleOut[50];
		int idx = -1;
		for (int j = 0; j < N; j++) {
			if (group[j].size() == 1) {
				//ans[j] = group[j][0][j];
				memcpy(ruleOut,group[j][0],50);
				idx = j;
				//for (int k = 0; k < N; k++) {

				//}
			}
		}

		int ans[50];
		/*
		for (int j = 0; j < N; j++) {
			if (group[j].size() == 1) {
				ans[j] = group[j][0][j];
			}
			else {
				if (group[j][0][j] != ruleOut[j])
					ans[j] = group[j][0][j];
				else
					ans[j] = group[j][1][j];

			}
		}
		*/

		for (int j = 0; j < group.size(); j++) {
			if (group[j].size() == 1) {
				ans[j] = group[j][0][j];
				continue;
			}
			//printf("\ngroup %d:", j);
			//for (int k = 0; k < group[j].size(); k++) {
				if (group[j][0][idx] != ruleOut[j])
					ans[j] = group[j][0][idx];
				else
					ans[j] = group[j][1][idx];
				//printf("%d ", group[j][k][0]);
				//printf("%d ", group[j][k][1]);
				//printf("%d ", group[j][k][2]);
			//}
		}

		
		printf("Case #%d: ", i);
		for (int j = 0; j < N; j++) {
			printf("%d", ans[j]);
			if (j != N - 1)
				printf(" ");
		}
		printf("\n");
		
	}

	return 0;
}

#endif