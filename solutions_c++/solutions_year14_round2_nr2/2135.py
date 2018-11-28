#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

// 000
// 001
// 010
// 011

int main() {
  int T;
  cin >> T;
  for (int t=1;t<=T;t++) {
		int A, B, K;
		cin >> A >> B >> K;

		int ans = 0;
		for (int a=0;a<A;a++) for (int b=0;b<B;b++) {
			if ((a&b) < K) ans ++;
		}

		printf("Case #%d: ", t);
		printf("%d\n", ans);
	}

  return 0;
}
