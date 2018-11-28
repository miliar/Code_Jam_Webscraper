
/**
 * Created by hoangtung on 4/11/15.
 */

#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
using namespace std;

#define MAX_SIZE 10005

int ERROR = -10000;
int multTable[5][5] = {{0, 0, 0, 0, 0}, {0, 1, 2, 3, 4}, {0, 2, -1, 4, -3}, {0, 3, -4, -1, 2}, {0, 4, 3, -2, -1}};
string solve(int l, int x, const string& pattern);
int reduce(int seq[], int start, int end);
int multiply(int left, int right);

int main()
{
	int nbTest;
	cin >> nbTest;

	for (int idx = 1; idx <= nbTest; ++idx)
	{
		int L, X;
		cin >> L >> X;
		string pattern;
		cin >> pattern;
		cout << "Case #" << idx << ": " << solve(L, X, pattern) << endl;;
	}
}

string solve(int l, int x, const string& pattern)
{
	int xl = x * l;
	int seq[MAX_SIZE];
	int o[MAX_SIZE];
	for (int i = 0; i < l; ++i)
	{
		o[i] = pattern[i] - 'i' + 1;
	}
	for (int i = 0; i < xl; ++i)
	{
		seq[i] = o[i % l];
	}


	int iVal = 1;
	
	for (int i = 0; i < xl; ++i)
	{
		iVal = multiply(iVal, seq[i]);
		if (iVal == 2)
		{
			int jVal = 1;
			for (int j = i + 1; j < xl; ++j)
			{
				jVal = multiply(jVal, seq[j]);
				if (jVal == 3)
				{
					int kVal = 1;
					for (int k = j + 1; k < xl; ++k)
					{
						kVal = multiply(kVal, seq[k]);
					}
					if (kVal == 4)
					{
						return "YES";
					}
				}
			}
		}
	}
	

	return "NO";
}

int reduce(int* seq, int xl, int start, int end)
{
	if (start < xl && end < xl)
	{
		int val = seq[start];
		for (int i = start + 1; i <= end; ++i)
		{
			val = multiply(val, seq[i]);
		}
	}

	return ERROR;
}

int multiply(int left, int right)
{
	int sign = left < 0 ? -1 : 1;
	left = abs(left);
	return sign * multTable[left][right];
}

