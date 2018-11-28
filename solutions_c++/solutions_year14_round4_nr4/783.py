#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;


int T, N, M;
char s[9999], str[99][99];
int maxinum, answer;
int type0[9999];
int son0[999][99];

void check() {
	int aaa[99];
	memset(aaa, 0, sizeof(aaa));
	for (int i = 0; i < M; i++) aaa[type0[i]] = 1;
	for (int i = 0; i < N; i++) if (!aaa[i]) return;
	
	int sum = 0;
	for (int k = 0; k < N; k++) {
		sum += 1;
		memset(son0, 0, sizeof(son0));
		for (int i = 0; i < M; i++) {
			if (type0[i] != k) continue;
			int p = 0;
			int l = strlen(str[i]);
			for (int j = 0; j < l; j++)
				if (son0[p][str[i][j] - 'A'])
					p = son0[p][str[i][j] - 'A'];
				else {
					son0[p][str[i][j] - 'A'] = sum;
					p = sum;
					sum += 1;
				}
		}
	}
	if (sum > maxinum) {
		maxinum = sum;
		answer = 1;
	} else if (sum == maxinum) {
		answer ++;
	}
}
void work(int start) {
	if (start == M) {
		check();
		return ;
	}
	for (int i = 0; i < N; i++) {
		type0[start] = i;
		work(start + 1);
	}
}
int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	
	int testCaseNum;
	scanf("%d", &testCaseNum);
	for (int testCase = 1; testCase <= testCaseNum; testCase++) {
		scanf("%d%d", &M, &N);
		gets(s);
		for (int i = 0; i < M; i++) gets(str[i]);
		
		maxinum = -1;	answer = 0;
		work(0);
		printf("Case #%d: %d %d\n", testCase, maxinum, answer);
	}
	return 0;
}

