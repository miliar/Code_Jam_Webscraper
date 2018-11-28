#include <iostream>
#include <sstream>
#include <algorithm>

using namespace std;

#define	For(i, a, b)	for(int i = (a) ; i < (b) ; ++i)
#define	rep(i, n)		For(i, 0, (n))

int		digit[100];

bool check(long long nn)
{
	stringstream ss;
	string s;

	ss << nn;
	s = ss.str();
	return equal(s.begin(), s.end(), s.rbegin());
}

long long recv(int index, int depth, long long n)
{
	long long	res = 0;

	if(!depth) {
		long long	number = 0;
		rep(i, index) {
			number *= 10;
			number += digit[i];
		}
		For(i, 1, index) {
			number *= 10;
			number += digit[index - i - 1];
		}
		number *= number;
		if(number <= n)
			if(check(number))
				++res;
		number = 0;
		rep(i, index) {
			number *= 10;
			number += digit[i];
		}
		rep(i, index) {
			number *= 10;
			number += digit[index - i - 1];
		}
		number *= number;
		if(number <= n)
			if(check(number))
				++res;
		return res;
	}
	rep(i, 10) {
		digit[index] = i;
		res += recv(index + 1, depth - 1, n);
	}
	return res;
}

long long answer(long long n)
{
	long long	res = 0;
	rep(i, 4) {
		For(j, 1, 10) {
			digit[0] = j;
			res += recv(1, i, n);
		}
	}
	return res;
}

long long solve()
{
	long long	A, B;

	cin >> A >> B;

	return answer(B) - answer(A - 1);
}

int main()
{
	int		T;
	cin >> T;
	rep(i, T)
		cout << "Case #" << (i + 1) << ": " << solve() << endl;
}

