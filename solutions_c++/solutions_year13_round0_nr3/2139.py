#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <sstream>
using namespace std;

typedef long long lld;
int T;
lld L, R;

bool isPalindrome(lld x)
{
	ostringstream os;
	os << x;
	const string &s = os.str();
	for (int i = 0, j = s.length() - 1; i < j; ++i, --j)
		if (s[i] != s[j]) return false;
	return true;
}

void work()
{
	static int ttt = 0;
	printf("Case #%d: ", ++ttt);
	cin >> L >> R;
	lld res = 0;
	for (lld base = 1; base * base <= R; ++base) {
		if (!isPalindrome(base)) continue;
		lld square = base * base;
		if (square < L || !isPalindrome(square)) continue;
		++res;
		//cout << base << endl;
	}
	cout << res << endl;
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%d\n", &T);
	while (T--) work();
}