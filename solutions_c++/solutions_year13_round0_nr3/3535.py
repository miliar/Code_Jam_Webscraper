#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <string.h>

using namespace std;

string i_to_s(int x)
{
	string s = "";
	while (x)
	{
		s = char(x % 10 + '0') + s;
		x /= 10;
	}
	return s;
}

void get_ans(int x, int res)
{
	string s = "Case #" + i_to_s(x) + ": ";
	cout << s << res << endl;
}

bool palindrome(int x)
{
	int y = 0;
	int _x = x;
	while (_x)
	{
		y = y * 10  + _x % 10;
		_x /= 10;
	}
	return (x == y);
}


int T, A, B;

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int k = 1; k <= T; ++k)
	{
		scanf("%d %d", &A, &B);
		int cnt = 0;
		for (int i = A; i <= B; ++i)
			if (palindrome(i) && (int)sqrt((double)i) * (int)sqrt((double)i) == i && palindrome((int)sqrt((double)i)))
				++cnt;
		get_ans(k, cnt);
	}
}