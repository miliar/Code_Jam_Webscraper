#include <iostream>
#include <cmath>
using namespace std;

int T;
int A, B;
int low, high;
bool check(int x) {
	int num = x;
	int rev = 0;
	int dig;
	while (num > 0) {
      dig = num % 10;
      rev = rev * 10 + dig;
      num = num / 10;
	}
	return (x == rev);
}

int main() {
	cin >> T;
	for(int t = 0; t < T; ++t) {
		int ans = 0;
		cin >> A >> B;
		low = sqrt(A);
		high = sqrt(B);
		while(low * low < A) {
			low++;
		} while(B < high * high) {
			high--;
		}
		cout << "Case #" << t + 1 << ": ";
		for(int i = low; i <= high; ++i) {
			if(check(i) && check(i*i)) {
				ans++;
			}
		}
		cout << ans << endl;
	}
	return 0;
}