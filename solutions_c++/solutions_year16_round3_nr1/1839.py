#include <iostream>
#include <cstdio>

using namespace std;

int check(int[]);
void max1(int[]);
void max2(int[]);
int main()
{
	int T;

	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		int N, P[30] = { 0 };

		scanf("%d", &N);
		for (int i = 0; i < N; i++)
			scanf("%d", P + i);

		printf("Case #%d: ", t);
		while (1) {
			max1(P);
			if (check(P)) break;
			max2(P);
			if (check(P)) break;
			printf(" ");
		}
		printf("\n");
	}

	return 0;
}
int check(int P[])
{
	for (int i = 0; i < 26; i++) {
		if (P[i]) return 0;
	}

	return 1;
}
void max2(int P[])
{
	int cnt = 0;
	int CNT = 0;

	for (int i = 0; i < 26; i++) {
		if (P[i] == 1) cnt++;
		else if (P[i] != 0) CNT++;
	}

	if (cnt == 2 && CNT == 0) return;

	int max_index = 0;

	for (int i = 0; i < 26; i++) {
		if (P[i] > P[max_index]) max_index = i;
	}

	printf("%c", max_index + 'A');
	P[max_index]--;
}
void max1(int P[])
{
	int max_index = 0;

	for (int i = 0; i < 26; i++) {
		if (P[i] > P[max_index]) max_index = i;
	}

	printf("%c", max_index + 'A');
	P[max_index]--;
}