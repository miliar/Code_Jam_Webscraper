#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iostream>
#include <map>
#include <memory>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int N, X;
int S[11111];

bool Chk[11111];

int main(void)
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int TC;
	scanf("%d", &TC);
	for (int tt = 1; tt <= TC; tt++) {
		scanf("%d%d", &N, &X);
		for (int i = 1; i <= N; i++) scanf("%d", &S[i]);
		stable_sort(S + 1, S + N + 1);
		memset(Chk, false, sizeof (Chk));
		int Ans = 0;
		for (int i = 1; i <= N; i++) {
			if (Chk[i]) continue;
			Ans++;
			Chk[i] = true;
			for (int j = N; j > i; j--) {
				if (Chk[j]) continue;
				if (S[i] + S[j] <= X) {
					Chk[j] = true;
					break;
				}
			}
		}
		printf("Case #%d: %d\n", tt, Ans);
	}

	return 0;
}
