#include<cstdio>
#include<iostream>
#include<string>
using namespace std;

int main()
{
	int T, Smax;
	string s;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		cin >> Smax >> s;
		int sum =0;
		int res = 0;
		for (int j = 0; j <= Smax; ++j)
		{
			if (sum < j)
			{
				res = res + j - sum;
				sum = j;
			}
			sum += (s[j] - '0');
		}
		printf("Case #%d: %d\n", i+1, res);

	}
}