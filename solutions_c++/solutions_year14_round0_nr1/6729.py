/*
 * problem1.cpp
 *
 *  Created on: 12-Apr-2014
 *      Author: cfilt
 */
#include <stdio.h>
#include <vector>
#include <algorithm>
int row1[4], row2[4];
int mat[4][4];
int main() {
	int cases;
	scanf("%d", &cases);
	for (int c = 1; c <= cases; ++c) {
		int guess;
		scanf("%d", &guess);
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				scanf("%d", &mat[i][j]);
			}
		}
		for (int i = 0; i < 4; i++)
			row1[i] = mat[guess - 1][i];
		scanf("%d", &guess);
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				scanf("%d", &mat[i][j]);
			}
		}
		for (int i = 0; i < 4; i++)
			row2[i] = mat[guess - 1][i];

		std::vector<int> v(8);
		std::vector<int>::iterator it;
		std::sort(row1, row1 + 4);
		std::sort(row2, row2 + 4);
		it = std::set_intersection(row1, row1 + 4, row2, row2 + 4, v.begin());
		v.resize(it - v.begin());
		if (v.size() == 1) {
			printf("Case #%d: %d\n", c, v[0]);
		} else if (v.size() == 0) {
			printf("Case #%d: %s\n", c, "Volunteer cheated!");
		} else {
			printf("Case #%d: %s\n", c, "Bad magician!");
		}
	}
}

