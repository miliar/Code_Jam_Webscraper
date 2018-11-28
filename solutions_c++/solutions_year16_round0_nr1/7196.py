#include <cstdio>
#include <iostream>

using namespace std;

bool check[10];
int main() {
    int TC;

    cin >> TC;

    for (int tc = 1; tc <= TC; tc++) {
	long long n;
	cin >> n;
	for (int i = 0; i < 10; i++) check[i] = false;

	long long result = n;
	while (n != 0) {
	    long long tmp = result;
	    while (tmp != 0) {
		check[tmp%10] = true;
		tmp /= 10;
	    }

	    int cnt = 0;
	    for (int i = 0; i < 10; i++) {
		if (check[i]) cnt++;
	    }
	    if (cnt == 10) break;
	    result += n;
	}

	if (n == 0) {
	    printf("Case #%d: INSOMNIA\n", tc);
	} else {
	    printf("Case #%d: %lld\n", tc, result);
	}
	
    }
    return 0;
}
