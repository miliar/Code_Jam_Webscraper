#include <set>
#include <map>
#include <ctime>
#include <queue>
#include <string>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;
int Test, N, M, P[10010], Q[10010], A[2000000];
bool B[2000000];
vector<int> ANS;

int main(int argc, char **argv)
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	scanf("%d", &Test);
	for (int Case = 1; Case <= Test; Case ++) {
		scanf("%d", &N);
		for (int i = 0; i < N; i ++) {
			scanf("%d", &P[i]);
		}
		M = 0;
		for (int i = 0; i < N; i ++) {
			scanf("%d", &Q[i]);
			for (int j = 0; j < Q[i]; j ++) {
				A[M ++] = P[i];
			}
		}
		sort(A, A + M);
		ANS.clear();
		while (M > 1) {
			memset(B, true, sizeof(B));
			int d = A[1] - A[0];
			ANS.push_back(d);
			for (int i = 0, j = 1; i < M; i ++)
			if (B[i]) {
				if (j <= i) j = i + 1;
				for (; A[i] + d != A[j]; j ++);
				B[j ++] = false;
			}
			N = 0;
			for (int i = 0; i < M; i ++)
			if (B[i]) {
				A[N ++] = A[i];
			}
			M = N;
		}
		printf("Case #%d:", Case);
		sort(ANS.begin(), ANS.end());
		for (int i = 0; i < ANS.size(); i ++) {
			printf(" %d", ANS[i]);
		}
		printf("\n");
	}
	return 0;
}