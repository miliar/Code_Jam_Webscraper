#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

ifstream fin("c.in");
ofstream fout("c.out");

void printBin(int x)
{
	if (x == 0) return;
	printBin(x >> 1);
	fout << (x & 1);
}

unsigned long long trans(int e, int base)
{
	unsigned long long ret = 0;
	unsigned long long b = 1;
	while (e > 0)
	{
		ret += (e & 1) * b;
		e = e >> 1;
		b *= base;
	}
	return ret;
}

int divisor(unsigned long long x)
{
	for (int i = 2; i <= int(sqrt(x)); i++)
		if (x % i == 0) return i;
	return 1;
}

int main()
{
	int T;
	fin >> T;
	int output[20];
	for (int ca = 1; ca <= T; ca++)
	{
		fout << "Case #" << ca << ":" << endl;
		int n, j;
		fin >> n >> j;
		int e = (1 << (n - 1)) + 1;
		for (; e < (1 << n); e++)
		{
			if ((e & 1) != 1) continue;
			bool flag = true;
			for (int base = 2; base <= 10; base++)
			{
				unsigned long long x = trans(e, base);
				int d = divisor(x);
				if (d == 1)
				{
					flag = false;
					break;
				}
				else output[base] = d;
			}
			if (flag)
			{
				printBin(e);
				for (int i = 2; i <= 10; i++) fout << " " << output[i];
				fout << endl;
				j--;
				if (j == 0) break;
			}
		}
	}
	return 0;
}