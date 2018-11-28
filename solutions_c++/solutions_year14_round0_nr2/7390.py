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

#define eps 1e-8
#define Inf (1 << 28)

int test_case;
double C, F, X;
double ans;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("outputB_Large.txt", "w", stdout);
	scanf("%d", &test_case);
	for(int caseId = 1; caseId <= test_case; caseId ++) {
		scanf("%lf %lf %lf", &C, &F, &X);
		ans = X / 2.0;
		double curTime = 0;
		double cookie = 2.0;
		for(int i = 1; i <= 100000; i ++) {
			curTime += (C / cookie);
			cookie += F;
			if(curTime + (X / cookie) + eps < ans) ans = curTime + (X / cookie) + eps;
		}

		printf("Case #%d: %.7lf\n", caseId, ans);
	}
	return 0;
}