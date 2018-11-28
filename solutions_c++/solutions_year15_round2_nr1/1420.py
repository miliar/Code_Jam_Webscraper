#include <cstdio>
#include <cstring>
#include <algorithm>
#define LL long long
#define MAX 1000005
using namespace std;

int arr[MAX];

int rev(int x) {
	int r = 0;
	while(x) {
		r = 10 * r + x % 10;
		x /= 10;
	}
	return r;
}

void precompute() {
	arr[1] = 1;
	for(int i = 2; i < MAX; i++) {
		int r = rev(i);
		if(r < i && rev(r) == i) {
			arr[i] = min(arr[i - 1] + 1, 1 + arr[r]);
		} else {
			arr[i] = arr[i - 1] + 1;
		}
	//	printf("arr[%d] = %d\n", i, arr[i]);
	}
}

int main(int argc, char const *argv[]) {
	int cases;

/*	LL table[32][2] = {
						{1, 19},
						{91, 109},
						{901, 1009},
						{9001, 10009},
						};*/
	precompute();
	scanf("%d", &cases);
	LL N;
	for(int i = 1; i <= cases; i++) {
		scanf("%lld", &N);
		printf("Case #%d: %d\n", i, arr[N]);
	}

	return 0;
}