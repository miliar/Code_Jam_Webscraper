//============================================================================
// Name        : GoogleCodeJam.cpp
// Author      : Luis Eduardo Oliveira Lizardo
// Version     :
// Copyright   :
// Description : Problem C. Fair and Square
//============================================================================

#include <iostream>
#include <stdio.h>
using namespace std;

#define SIZE 4

int main() {

	int T;

	int p[] = {0, 1, 4, 9, 121, 484, 10201};
	int n = 7;
	int a, b;

	scanf("%d%*c", &T);

	for (int i = 1; i <= T; ++i) {
		scanf("%d %d%*c", &a, &b);
		int count =0;

		for (int j = 0; j < n; ++j) {
			if(a <= p[j] && b >= p[j]){
				count++;
			}
		}
		printf("Case #%d: %d\n", i, count);
	}

}

