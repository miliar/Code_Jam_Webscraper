#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <fstream>
#include <stdio.h>
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int II = 0; II < T; II++)
	{
		bool val = 0;
		int num;
		int num2;
		int N = 1;
		cin >> num;
		num2 = num;
		int A[10] = {0,0,0,0,0,0,0,0,0,0};
		if (num == 0)
		{
			val = 1;
			cout << "Case #" << II+1 << ": INSOMNIA" << endl;
		}
		while (val == 0)
		{
			val = 0;
			num = num2 * N;
		while (num != 0)
		{
			int mod = num % 10;
			if (A[mod] != 1)
			{
				A[mod] = 1;
			}
			num = num / 10;
		}
		for (int i = 0; i < 10; i++)
		{
			if (A[i] != 1)
			{
				val = 1;
				break;
			}
		}
		if (val == 1)
		{
			val = 0;
			N++;
		}
		else
		{
			val = 1;
			cout << "Case #" << II+1 << ": " << num2 * N << endl;
		}

		}
	}
	return 0;
}