#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>
using namespace std;

bool is_palindrome(int n) {
	string s1 = to_string(n);
	string s2 = s1;
	reverse(s2.begin(), s2.end());
	return s1 == s2;		
}

bool is_perfect_square(int n) {
    if (n < 0)
        return false;
    int root(floor(sqrt(n)+0.5));
	return n == root * root && is_palindrome(root);
}

int main() {
	int N;
	cin >> N;
	for (int t = 0; t < N; ++t) {
		int A, B;
		cin >> A >> B;
		int cnt = 0;
		for (int i = A; i <= B; ++i) {
			if (is_perfect_square(i) && is_palindrome(i))
				++cnt;
		}
		cout << "Case #" << t+1 << ": " << cnt << endl;

	}
	return 0;
}