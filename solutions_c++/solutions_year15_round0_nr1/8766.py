#include <iostream>
#include <cstdio>

using namespace std;


void execute(int tc) {
	int n;
	char data[1002];
	scanf("%d %s\n", &n, data);
	// printf("%d %s\n",n, data);
	int standing = 0;
	int helper = 0;
	for (int i=0; i<n+1; i++) {
		if (standing >= i) {
			// cout << "a:";
			standing += (data[i] - '0');
		} else {
			// cout << "b:";
			if (data[i]-'0' > 0) {
				int _helper = i - standing;
				helper += _helper;
				standing += _helper + (data[i] - '0');
			}
		}
		// printf("i: %d; helper: %d; standing: %d\n", i, helper, standing);
	}
	printf("Case #%d: %d\n", tc, helper);
}


int main() {
	int T;
	scanf("%d", &T);
	for (int i=1; i<=T; i++) {
		execute(i);
	}
	return 0;
}
