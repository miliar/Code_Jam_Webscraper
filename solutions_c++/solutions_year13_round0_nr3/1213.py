#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string>
#include <cmath>
using namespace std;

#define CY 1010
#define CY2 3340
typedef long long LL;
typedef LL typec;

int ar[CY], rec[CY], rec2[CY2], tb[CY], tb2[CY2];
typec A, B;

int get_num(int value) {
	int sum = 0, p = 1, tmp = value;
	while (value > 0) {
		sum = 10 * sum + value % 10;
		value /= 10;
		p *= 10;
	}
	return tmp * p + sum;
}

int get_num2(int value) {
	int sum = 0, p = 1, tmp = value;
	while (value > 0) {
		sum = 10 * sum + value % 10;
		value /= 10;
		p *= 10;
	}
	tmp /= 10;
	return tmp * p + sum;
}

bool Is(typec value) {
	int k = 0;
	while (value > 0) {
		ar[k++] = value % 10;
		value /= 10;
	}
	for (int i = 0, j = k - 1; i < j; ++i, --j) {
		if (ar[i] != ar[j]) return false;
	}
	return true;
}

void init() {
	int sum = 0;
	rec[0] = 0;
	for (int i = 1; i < CY; ++i) {
		typec tmp = get_num(i);
		tb[i] = tmp;
		if (Is(tmp * tmp)) rec[i] = rec[i - 1] + 1;
		else rec[i] = rec[i - 1];
	}
	rec2[0] = 1;
	for (int i = 1; i < CY2; ++i) {
		typec tmp = get_num2(i);
		tb2[i] = tmp;
		if (Is(tmp * tmp)) rec2[i] = rec2[i - 1] + 1;
		else rec2[i] = rec2[i - 1];
	}
}


int cal(typec value) {
	int lt = 0, rt = CY - 1, mid;
	typec tmp;
	while (lt <= rt) {
		mid = (lt + rt) >> 1;
		tmp = (typec)tb[mid] * tb[mid];
		if (tmp > value) rt = ~-mid;
		else lt = -~mid;
	}
	int sum = rec[rt];
	lt = 0, rt = CY2 - 1, mid;
	while (lt <= rt) {
		mid = (lt + rt) >> 1;
		tmp = (typec)tb2[mid] * tb2[mid];
		if (tmp > value) rt = ~-mid;
		else lt = -~mid;
	}
	sum += rec2[rt];
	return sum;
}

int main(void) {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("me.out", "w", stdout);
	init();
	int cas;
	scanf("%d", &cas);
	for (int T = 1; T <= cas; ++T) {
		scanf("%lld%lld", &A, &B);
		printf("Case #%d: ", T);
		printf("%d\n", cal(B) - cal(A - 1));
	}
	return 0;
}