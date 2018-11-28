#define _CRT_SECURE_NO_DEPRECATE

#include<stdio.h>
#include<iostream>

using namespace std;

int people[1005];
int biggest = 0;
int biggest_group;
int sum=0;

int main()
{
	int a, b, c;
	int t, n, p;
	int num;

	freopen("A-large.in", "r", stdin);
	freopen("A-large.txt", "w", stdout);

	scanf("%d", &t);
	for (num = 0; num < t; num++) {
		scanf("%d", &a);
		c = a; sum = 0;
		while (a--) {
			scanf("%d", &b);
			people[a] = b;
			sum = sum + b;
		}

		if (sum % 2 == 1) {
				a = c;
				biggest = 0;
				while (a--) {
					if (biggest < people[a]) {
						biggest = people[a];
						biggest_group = a;
					}
				}
				people[biggest_group] = people[biggest_group] - 1; printf("Case #%d: %c ", num + 1, 65-biggest_group+c-1);
		}
		else {
			printf("Case #%d: ", num + 1);
		}
		while (1) {
			a = c;
			biggest = 0;
			while (a--) {
				if (biggest < people[a]) {
					biggest = people[a];
					biggest_group = a;
				}
			}
			if (biggest == 0) break;
			people[biggest_group] = people[biggest_group] - 1; printf("%c", 65 - biggest_group + c - 1);

			a = c;
			biggest = 0;
			while (a--) {
				if (biggest < people[a]) {
					biggest = people[a];
					biggest_group = a;
				}
			}
			if (biggest == 0) break;
			people[biggest_group] = people[biggest_group] - 1; printf("%c ", 65 - biggest_group + c - 1);
		}
		printf("\n");
	}
	return 0;
}