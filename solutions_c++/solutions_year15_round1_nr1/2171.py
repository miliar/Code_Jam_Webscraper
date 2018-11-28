#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int arr[11111];
int main() {

    int TC;

    cin >> TC;

    for (int tc = 1; tc <= TC; tc++) {
	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
	    cin >> arr[i];
	}

	long long int ans1 = 0;
	for (int i = 1; i < n;  i++) {
	    if (arr[i] < arr[i-1]) {
		ans1 += (long long int)(arr[i-1]  -  arr[i]);
	    }
	}

	long long int ans2 = 0;
	int rate = 0;
	for (int i = 1; i < n; i++) {
	    if (arr[i] < arr[i-1]) {
		rate = max(rate, arr[i-1] - arr[i]);
	    }
	}
	for (int i = 0; i < n-1; i++) {
	    if (arr[i] >= rate) ans2 += (long long int)rate;
	    else ans2 += (long long int)arr[i];
	}

	printf("Case #%d: %lld %lld\n", tc, ans1, ans2);
    }

    return 0;

}
