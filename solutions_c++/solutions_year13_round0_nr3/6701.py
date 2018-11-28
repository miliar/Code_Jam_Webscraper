#include <iostream>
#include <cmath>
using namespace std;

bool isPalindrome(int n)
{
	int c = n;
	int r = 0;
	
	while (c) {
		r = r * 10 + (c % 10);
		c /= 10;
	}
	
	if (r == n)
		return true;
	else
		return false;
}

int isSquare(int n)
{
	int r = sqrt(n);
	if (r * r == n)
		return r;
	else
		return 0;
}

int main()
{
	int T;
	int a, b, total;
	cin >> T;
	
	for (int testcase = 1; testcase <= T; ++testcase) {
		cin >> a >> b;
		total = 0;

		for (int i = a; i <= b; ++i) {
			if (isPalindrome(i)) {
				int r = isSquare(i);
				if (r && isPalindrome(r))
					++total;
			}
		}
		
		cout << "Case #" << testcase << ": " << total << endl;
	}
}
