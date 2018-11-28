#include <windows.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace::std;

__int64 A, N;
std::vector<__int64> buf;

__int64 rec(__int64 a, __int64 i, __int64 res)
{
	for (; i < N; i++)
	{
		if (a > buf[i])
		{
			a += buf[i];
		}
		else
		{
			if (a + a - 1 > buf[i])
			{
				a += a - 1 + buf[i];
				res++;
			}
			else if (a == 1)
			{
				res++;
			}
			else
			{
				//__int64 res1 = res + 1, res2 = res + 1, i1 = i, i2 = i;
				__int64 res1 = rec(a + a - 1, i, res + 1);
				__int64 res2 = rec(a, i + 1, res + 1);
				return min(res1, res2);
// 				if (res1 < res2)
// 				{
// 					res = res1;
// 					i = i1;
// 				}
// 				else
// 				{
// 					res = res2;
// 					i = i2;
// 				}
// 				i--;
			}
		}
	}
	return res;
}

int main(int argc, char* argv[])
{
	ifstream cin(argv[1]);

	int nCount, numCase = 1;
	cin >> nCount;

	while (numCase <= nCount)
	{
		cin >> A >> N;
		__int64 result = 0;

		buf.clear();
		buf.resize(N);
		for (__int64 i = 0; i < N; i++)
			cin >> buf[i];

		std::sort(buf.begin(), buf.end());

// 		for (__int64 i = 0; i < N; i++)
// 		{
// 			if (A > buf[i])
// 			{
// 				A += buf[i];
// 			}
// 			else
// 			{
// 				if (A + A - 1 > buf[i])
// 				{
// 					A += A - 1 + buf[i];
// 					result++;
// 				}
// 				else
// 				{
// 					result++;
// 				}
// 			}
// 		}

		result = rec(A, 0, 0);

		cout << "Case #" << numCase << ": ";
		cout << result;
		cout << "\n";

		numCase++;
	}
	return 0;
}
