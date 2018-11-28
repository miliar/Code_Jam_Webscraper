//============================================================================
// Name        : Csmall.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

bool chkStart(int num) {
	if (num < 10) {
		return true;
	} else if (num < 100) {
		if (num % 11 == 0) {
			return true;
		}
	} else {
		if (num % 10 == num / 100) {
			return true;
		}
	}
	return false;
}

int main() {
	int t;
	int i;
	int a, b;
	int start;
	int cnt;
	int num;
	scanf("%d", &t);
	for (i = 0; i < t; i++) {
		scanf("%d %d", &a, &b);
		cnt = 0;
		start = round(sqrt(a));
		while(!chkStart(start))	start++;
		num = pow(start, 2);
		while (num <= b) {
			if (num >= a && num <= b) {
				if (num < 10) {
					cnt++;
				} else if (num < 100) {
					if (num % 11 == 0) {
						cnt++;
					}
				} else {
					if (num % 10 == num / 100) {
						cnt++;
					}
				}
			}
			start++;
			while(!chkStart(start))	start++;
			num = pow(start, 2);
		}
		printf("Case #%d: %d\n", i + 1, cnt);
	}
	return 0;
}
