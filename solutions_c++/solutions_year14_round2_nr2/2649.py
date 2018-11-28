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

int test_case;
int A, B, K;

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("outB.txt", "w", stdout);
	scanf("%d", &test_case);
	for(int caseId = 1; caseId <= test_case; caseId ++) {
		int ans = 0;
		cin >> A >> B >> K;
		for(int i = 0; i < A; i ++) {
			for(int j = 0; j < B; j ++ ) {
				int res = i & j;
				if(res < K ) ans ++;
			}
		}

		printf("Case #%d: %d\n", caseId, ans);
	}
	return 0;
}