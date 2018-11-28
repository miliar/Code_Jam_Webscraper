#include<stdio.h>
#include<string.h>
#include<vector>
#include<iostream>
#include<string>
#include<vector>
#include<set>

using namespace std;
typedef long long LL;
int main() {
	int caseNum;
	char dummy; //read the '\n' after the caseNum
	scanf("%d%c", &caseNum, &dummy);
	for (int caseCount = 1; caseCount <= caseNum; caseCount++) {
		int firstRow, secondRow;
		set<int> s;
		scanf("%d", &firstRow);
		int i, j, dummy;
		for (i = 1; i <= 4; i++) {
			if (i != firstRow) {
				scanf("%d%d%d%d", &dummy, &dummy, &dummy, &dummy);
				continue;
			}
			for (j = 0; j < 4; j++) {
				int t;
				scanf("%d", &t);
				s.insert(t);
			}
		}

		vector<int> answer;
		scanf("%d", &secondRow);
		for (i = 1; i <= 4; i++) {
			if (i != secondRow) {
				scanf("%d%d%d%d", &dummy, &dummy, &dummy, &dummy);
				continue;
			}
			for (j = 0; j < 4; j++) {
				int t;
				scanf("%d", &t);
				if (s.find(t)!=s.end()) {
					answer.push_back(t);
				}
			}
		}

		printf("Case #%d: ", caseCount);
		if (answer.size() == 1) {
			printf("%d\n", answer[0]);
		} else if (answer.size() == 0) {
			printf("Volunteer cheated!\n");
		} else {
			printf("Bad magician!\n");
		}
	}
	return 0;
}
