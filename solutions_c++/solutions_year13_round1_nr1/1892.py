#include<iostream>
#include<cmath>

using namespace std;

int main() {
	int testcases;
	long long r, t;
	long long left, right, mid;
	long long tmp;
	scanf("%d", &testcases);
	for (int i = 0; i < testcases; i++) {
		scanf("%lld %lld", &r, &t);
		left = 0l, right = t/(2 * r - 1);
		tmp = sqrt(t/2);
		if (tmp < right)
			right = tmp;
		while (right >= left) {
			mid = (left + right) / 2;
			tmp = (mid * 2 + 2 * r - 1) * mid;
			//printf("mid = %lld, tmp = %lld, t = %lld \n", mid, tmp, t);
			if (tmp < t)
				left = mid + 1;
			else if (tmp > t)
				right = mid - 1;
			else {
				right = mid;
				break;
			}
		}
		printf("Case #%d: %lld\n", i + 1, right);
	}
	return 0;
}