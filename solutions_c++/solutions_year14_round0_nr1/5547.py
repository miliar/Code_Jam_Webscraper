#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

const int N = 4;

int m1[N][N], m2[N][N];
int cnt[N * N + 1];

int main () {
	int test;
	scanf ("%d", &test);
	for (int tests = 0; tests < test; tests++) {
		printf ("Case #%d: ", tests + 1);
		int r1, r2;
		scanf ("%d", &r1);
		r1--;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				scanf ("%d", &m1[i][j]);
		scanf ("%d", &r2);
		r2--;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				scanf ("%d", &m2[i][j]);
		for (int j = 0; j < N; j++) {
			cnt[m1[r1][j]]++;
			cnt[m2[r2][j]]++;
		}
		int nTwo = 0;
		int two = -1;
		for (int i = 1; i <= N * N; i++)
			if (cnt[i] == 2) {
				nTwo++;
				two = i;
			}
		if (nTwo == 0)
			printf ("Volunteer cheated!\n");
		else
			if (nTwo > 1)
				printf ("Bad magician!\n");
			else
				printf ("%d\n", two);
		for (int i = 1; i <= N * N; i++)
			cnt[i] = 0;
	}
}

