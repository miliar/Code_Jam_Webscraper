/*
 * Qa.cpp
 *
 *  Created on: Apr 10, 2016
 *      Author: suparsh14
 */

#include<bits/stdc++.h>
#include<stdio.h>
using namespace std;

typedef long long int ll;

ll N, ans, cnt;
bool arr[10];

void digit_check(ll num) {

	while (num != 0) {
		if (!arr[num % 10]) {
			arr[num % 10] = true;
			cnt++;
		}
		num /= 10;
	}

}

int main() {

	int tc;
	scanf("%d", &tc);

	for (int i = 1; i <= tc; i++) {
		scanf("%lld", &N);
		if (N == 0) {
			printf("Case #%d: INSOMNIA\n", i);
		} else {

			memset(arr, false, sizeof(arr));
			cnt=0;

			for (ans = N;; ans += N) {
				digit_check(ans);
				if (cnt == 10)
					break;
			}
			printf("Case #%d: %lld\n", i, ans);
		}

	}

	return 0;
}

