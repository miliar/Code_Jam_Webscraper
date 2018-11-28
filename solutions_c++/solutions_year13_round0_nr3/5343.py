#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

bool IsPalindrome(char* str)
{
	bool ret = true;
	int len = strlen(str);
	if (len > 1)
	{
		for (int j = 0; j < len/2; j++)
		{
			if (str[j] != str[len-1-j])
			{
				ret = false;
				break;
			}
		}
	}
	return ret;
}

int main()
{
	int T = 0; cin >> T;
	for (int x = 1; x <= T; x++)
	{
		cout << "Case #" << x << ": ";
		int A = 0, B = 0, N = 0;
		char str[256] = {0};
		cin >> A;
		cin >> B;
		for (int i = A; i <= B; i++)
		{
			sprintf(str, "%Lf", sqrt(i));
			char* dot = strstr(str, ".000000");
			if (dot)
			{
				str[strlen(str)-7] = 0;
				bool isFirst = IsPalindrome(str);
				sprintf(str, "%Lf", (double)i);
				str[strlen(str)-7] = 0;
				bool isSecond = IsPalindrome(str);
				if (isFirst && isSecond) N++;

			}
		}
		cout << N;
		cout << endl;
	}
	return 0;
}