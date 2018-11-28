#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int A, B;

bool isPalindrome(int n) {
	vector<int> d;
	while (n > 0) {
		d.push_back(n % 10);
		n /= 10;
	}
	int l = d.size();
	for (int i = 0; i < l - 1 - i; ++i)
		if (d[i] != d[l - 1 - i])
			return false;
	return true;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; Ti++)
	{
		scanf("%d %d", &A, &B);
		int count = 0;
		int n = (int)(sqrt(A));
		while (true) {
			int s = n*n;
			if (s > B) break;
			if (s >= A && isPalindrome(n) && isPalindrome(s)) {
				count++;
				//printf("%d\n", n);
			}
			n++;
		}

		printf("Case #%d: %d\n", Ti, count);
	}
	return 0;
}
