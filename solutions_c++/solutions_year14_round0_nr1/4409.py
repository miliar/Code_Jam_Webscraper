/*
 * 1000.cpp
 *
 *  Created on: 2013-12-14
 *      Author: lenovo
 */
#include<iostream>
#include<cstdio>
int card[10][10];
using namespace std;
int main() {
	int T, Case = 0;
	scanf("%d", &T);
	int a, b, c, d, num, ans;
	int row, i, j;
	while (T--) {
		Case++;
		scanf("%d", &row);
		for (i = 1; i <= 4; i++) {
			for (j = 1; j <= 4; j++) {
				scanf("%d", &card[i][j]);
			}
		}
		a = card[row][1];
		b = card[row][2];
		c = card[row][3];
		d = card[row][4];
		scanf("%d", &row);
		for (i = 1; i <= 4; i++) {
			for (j = 1; j <= 4; j++) {
				scanf("%d", &card[i][j]);
			}
		}
		num = 0;
		for (i = 1; i <= 4; i++)
			if (card[row][i] == a) {
				num++;
				ans = a;
			}
		for (i = 1; i <= 4; i++)
			if (card[row][i] == b) {
				num++;
				ans = b;
			}
		for (i = 1; i <= 4; i++)
			if (card[row][i] == c) {
				num++;
				ans = c;
			}
		for (i = 1; i <= 4; i++)
			if (card[row][i] == d) {
				num++;
				ans = d;
			}
		printf("Case #%d: ", Case);
		if (num == 1)
			printf("%d\n", ans);
		else if (num == 0)
			printf("Volunteer cheated!\n");
		else
			printf("Bad magician!\n");
	}
	return 0;
}
