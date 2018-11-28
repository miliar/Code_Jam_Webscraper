#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
using namespace std;

int isP[1010];

void init() {
	int num,k,tmp;
	for (k = 1; k <= 1000; k++) {
		num=k;
		tmp=0;
		while (num != 0) {
			tmp=tmp*10+num%10;
			num /= 10;
		}
		if (tmp == k)
			isP[k] = 1;
	}
}
int main() {
	int T = 0;
	int i;
	int A, B;
	int n, a, b, ans;
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);

	memset(isP, 0, sizeof(isP));
	init();
	cin >> T;
	for (i = 1; i <= T; i++) {
		cin >> A >> B;
		//printf("i%d A%d B%d\n",i,A,B);
		ans = 0;
		a = ceil(sqrt(A));

		b = sqrt(B);
		//printf("i%d a%d b%d\n",i,a,b);

		for (n = a; n <= b; n++) {
			if (isP[n] == 1 && isP[n * n] == 1)
				ans++;
		}
		printf("Case #%d: %d\n", i, ans);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
