#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstring>
#include<string>
#include<queue>
#include<set>
#include<map>
#include<cmath>
using namespace std;

#define MAX 5

int test_case;
int numCount[ MAX * MAX ];
int A1, A2;
int firstGrid[ MAX ][ MAX ], secondGrid[ MAX ][ MAX ];

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("outputA.txt", "w", stdout);
	int i, j;
	scanf("%d", &test_case);
	for(int caseId = 1; caseId <= test_case; caseId ++) {
		scanf("%d", &A1);
		for(i = 0 ; i < 4; i ++) for(j = 0; j < 4; j ++) scanf("%d", &firstGrid[ i ][ j ]);
		scanf("%d", &A2);
		for(i = 0 ; i < 4; i ++) for(j = 0; j < 4; j ++) scanf("%d", &secondGrid[ i ][ j ]);

		memset(numCount, 0, sizeof(numCount));

		int curRow = A1 - 1;
		for(i = 0; i < 4; i ++) {
			numCount[ firstGrid[ curRow ][ i ] ] ++;
		}

		curRow = A2 - 1;
		int total = 0;
		int ans ;
		for(i = 0; i < 4; i ++) {
			numCount[ secondGrid[ curRow ][ i ] ] ++;
			if(numCount[ secondGrid[ curRow ][ i ] ] == 2){
				total ++;
				ans = secondGrid[ curRow ][ i ];
			}
		}


		if(total == 0) {
			printf("Case #%d: Volunteer cheated!\n", caseId);
		} 

		else if(total == 1) {
			printf("Case #%d: %d\n", caseId, ans);
		}

		else printf("Case #%d: Bad magician!\n", caseId);
	}
	return 0;
}