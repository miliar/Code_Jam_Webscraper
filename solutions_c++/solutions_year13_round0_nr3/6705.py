// Pooja Ahuja
// Google CodeJam

#include <iostream>
#include <cmath>
using namespace std;

bool palindrome(unsigned long long n)
{
	unsigned long long c = n;
	unsigned long long r = 0;
	
	while (c) {
		r = r * 10 + (c % 10);
		c /= 10;
	}
	
	if (r == n)
		return true;
	else
		return false;
}

unsigned long long square(unsigned long long n)
{
	unsigned long long r = sqrt(n);
	if (r * r == n)
		return r;
	else
		return 0;
}

int main()
{
	unsigned long long T;
	unsigned long long a, b, count;
	cin >> T;
	
	for (unsigned long long testcase = 1; testcase <= T; ++testcase) {
		cin >> a >> b;
		count = 0;

		for (unsigned long long i = a; i <= b; ++i) {
			if (palindrome(i)) {
				unsigned long long r = square(i);
				if (r && palindrome(r))
					++count;
			}
		}
		
		cout << "Case #" << testcase << ": " << count << endl;
	}
}
