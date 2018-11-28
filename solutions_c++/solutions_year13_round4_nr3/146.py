#include <algorithm>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define SIZE(v) ((int)(v).size())

#define BEGIN(v) ((v).begin())
#define END(v) ((v).end())
#define ALL(v) BEGIN(v),END(v)
#define SORT(v) sort(ALL(v))
#define UNIQUE(v) SORT(v);(v).erase(unique(ALL(v)),END(v))

#define FOR(i,l,r) for(int i=(l);i<(r);i++)
#define FOREACH(i,v) for(typeof((v).begin()) i=(v).begin();i!=(v).end();i++)

const int MAXN = 2048;

int N, A[MAXN], B[MAXN], answer[MAXN];
pair<int, int> order[MAXN];

int a[MAXN], b[MAXN];

void verify() {
	FOR(i, 0, N) {
		a[i] = 1;
		FOR(j, 0, i) if (answer[j] < answer[i]) {
			a[i] = max(a[i], a[j] + 1);
		}
	}
	for (int i = N - 1; i >= 0; i--) {
		b[i] = 1;
		FOR(j, i + 1, N) if (answer[i] > answer[j]) {
			b[i] = max(b[i], b[j] + 1);
		}
	}
	bool flag = true;
	FOR(i, 0, N) {
		if (a[i] != A[i]) {
			puts("A ooooooops");
			flag = false;
			break;
		} else if (b[i] != B[i]) {
			puts("B ooooooops");
			flag = false;
			break;
		}
	}
	if (!flag) {
		printf("  ="); FOR(i, 0, N) printf("%3d", answer[i]); putchar('\n');
		printf("a ="); FOR(i, 0, N) printf("%3d", a[i]); putchar('\n');
		printf("b ="); FOR(i, 0, N) printf("%3d", b[i]); putchar('\n');
		printf("B ="); FOR(i, 0, N) printf("%3d", B[i]); putchar('\n');
	}
}

bool found;

void dfs(int depth) {
	if (depth == N) {
		found = true;
		return ;
	}
	int tmp;
	tmp = 1;
	FOR(i, 0, N) {
		if (answer[i] == -1) a[i] = tmp;
		else {
			a[i] = -1;
			tmp = max(tmp, A[i] + 1);
		}
	}
	tmp = 1;
	for (int i = N - 1; i >= 0; i--) {
		if (answer[i] == -1) b[i] = tmp;
		else {
			b[i] = -1;
			tmp = max(tmp, B[i] + 1);
		}
	}
	vector<int> candidate;
	FOR(i, 0, N) if (answer[i] == -1 && a[i] == A[i] && b[i] == B[i]) {
		candidate.push_back(i);
	}
	FOREACH(it, candidate) {
		answer[*it] = depth;
		dfs(depth + 1);
		if (found) break;
		answer[*it] = -1;
	}
}

int main() {
	int taskNumber; scanf("%d", &taskNumber);
	for (int taskIdx = 1; taskIdx <= taskNumber; taskIdx++) {
		scanf("%d", &N);
		FOR(i, 0, N) scanf("%d", &A[i]);
		FOR(i, 0, N) scanf("%d", &B[i]);
		memset(answer, 0xFF, sizeof(answer));
		found = false;
		dfs(0);
		if (!found) puts("NOT FOUND");
		verify();
		printf("Case #%d:", taskIdx); FOR(i, 0, N) printf(" %d", answer[i] + 1); putchar('\n');
	}
	return 0;
}
