#include <iostream>
#include <cstring>
#include <cmath>
#include <string>
using namespace std;

const double EPS = 1e-9;

bool IsPolindrome(int num)
{
	string str, rev;
	while (num > 0)
	{
		str += (num % 10);
		rev += (num % 10);
		num /= 10;
	}
	reverse (rev.begin(), rev.end());
	return str == rev;
}

int GetSqrt(int num)
{
	int kor = (int)(sqrt((double)num) + EPS);
	if (kor * kor == num)
		return kor;
	else
		return 0;
}

int main()
{
	freopen ("test.in", "a+", stdin);
	freopen ("test.out", "w", stdout);

	int tests, a, b, ans;
	cin >> tests;
	for (int t = 0; t < tests; ++t)
	{
		ans = 0;

		cin >> a >> b;
		for (int num = a; num <= b; ++num)
		{
			if (IsPolindrome(num))
			{
				int kor = GetSqrt(num);
				if (kor > 0 && IsPolindrome(kor))
					++ans;
			}
		}
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}
	return 0;
}