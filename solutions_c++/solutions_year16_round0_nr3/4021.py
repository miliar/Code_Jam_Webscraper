#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <map>
using namespace std;

#define NN 16
typedef long long lld;

int N, J;

void input() {
	scanf("%d%d", &N, &J);
}

lld convert(int a[], int n, int k) {
	lld r = 0;
	lld t = 1;
	for (int i = 0; i < n; i++) {
		r += t * a[i];
		t *= k;
	}
	return r;
}

int divisor(lld x) {
	for (lld i = 2; i*i <= x; i++) {
		if (x % i == 0) return i;
	}
	return -1;
}

void solve(int icase) {
	printf("Case #%d:\n", icase);
	int nans = 0;
	for (lld i = (1 << (NN - 1)) + 1; i < (1 << NN); i+=2) {
		int a[NN]; // small -> big, reverse output
		for (int j = 0; j < NN; j++) {
			a[j] = (i >> j) & 0x1;
		}
		bool ok = true;
		lld save[NN];
		for (int k = 2; k <= 10; k++) {
			lld x = convert(a, NN, k);
			lld d = divisor(x);
			if (d == -1) {
				ok = false;
				break;
			}
			else {
				save[k] = d;
			}
		}
		if (ok) {
			nans++;
			for (int j = NN - 1; j >= 0; j--) {
				printf("%d", (i >> j) & 0x1);
			}
			for (int k = 2; k <= 10; k++) {
				printf(" %lld", save[k]);
			}
			printf("\n");

			if (nans >= J) break;
		}
	}
}


int main()
{
	//freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		input();
		solve(i);
	}
	//system("pause");
	return 0;
}