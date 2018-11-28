#define Counting_Sheep_L

#ifdef Counting_Sheep_L
#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

int table[10][10] =
{
	{ 0,	0,	0,	0,	0,	0,	0,	0,	0,	0 },
	{ 1,	2,	3,	4,	5,	6,	7,	8,	9,	10 },
	{ 2,	4,	6,	8,	10,	12,	14,	16,	18,	20 },
	{ 3,	6,	9,	12,	15,	18,	21,	24,	27,	30 },
	{ 4,	8,	12,	16,	20,	24,	28,	32,	36,	40 },
	{ 5,	10,	15,	20,	25,	30,	35,	40,	45,	50 },
	{ 6,	12,	18,	24,	30,	36,	42,	48,	54,	60 },
	{ 7,	14,	21,	28,	35,	42,	49,	56,	63,	70 },
	{ 8,	16,	24,	32,	40,	48,	56,	64,	72,	80 },
	{ 9,	18,	27,	36,	45,	54,	63,	72,	81,	90 },
};

unsigned long long myCount(unsigned long long val, set <int>*mySet) {
	int R = 0;
	unsigned long long Q = val;

	while (true) {
		if (mySet->size() == 10) {
			return val;
		}

		R = Q % 10;
		mySet->insert(R);
		Q = (Q - R) / 10;
		if (Q == 0)
			return val;
	}
}

int main() {
	freopen("A-large.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int T;
	scanf("%d\n", &T);

	for (int i = 1; i <= T; i++) {
		unsigned long long N;
		scanf("%llu", &N);
		unsigned long long y = 0;

		set<int> digitSet;
		int **dict = new int*[10];

		if (N == 0)
			goto X;

		unsigned long long k = 1;
		while (true) {
			y = myCount((unsigned long long)k*(unsigned long long)N, &digitSet);
			if (digitSet.size() == 10)
				break;
			k++;
		}

	X:
		if (dict != NULL)
			delete(dict);
		if (y == 0)
			printf("Case #%d: INSOMNIA\n", i);
		else
			printf("Case #%d: %llu\n", i, y);
	}

	return 0;
}

#endif