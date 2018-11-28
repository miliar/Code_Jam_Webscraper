#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <stdlib.h>
using namespace std;

#define N 1000000

int ar[N+1];

int inv(int a) {
	int ans = 0;
	while(a > 0) {
		int d = a%10;
		ans = ans*10 + d;
		a/=10;
	}
	return ans;
}

int main() {
	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	fill(ar, ar+N+1, 1000000);
	ar[0] = 0;

	for(int i = 1; i <= N; i++) {
		ar[i] = min(ar[i], ar[i-1] + 1);
		int j = inv(i);
		if (j <= i) continue;
		ar[j] = ar[i] + 1;
	}

	//for(int i = 1; i <= 100; i++) {
	//	cout << i << " " << ar[i] << endl;
	//}



	int T; cin >> T;
	for(int t = 1; t <= T; t++) {
		int n; cin >> n;
		int ans = ar[n];
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}