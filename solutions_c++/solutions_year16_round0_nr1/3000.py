#include <cstdio>
#include <vector>
#include <stdlib.h>
#include <iostream>
#include <stdio.h>
#include <fstream>
using namespace std;

vector <int> used(10);
int need = 10;

void to_string(long long x)
{
	long long y = x;
	while (y != 0)
	{
		int g = y % 10;
		if (used[g] == 0)
		{
			need--;
			used[g] = 1;
		}
		y /= 10;
	}
}

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int qq;
	cin >> qq;
	for (int qqq = 0; qqq < qq; qqq++)
	{
		cout << "Case #" << qqq+1 << ": ";
		long long n;
		cin >> n;
		int flag = 0;
		for (int i = 0; i < 10; i++)
			used[i] = 0;
		need = 10;
		long long cur = n;
		for (int i = 0; i < 123456789; i++)
		{
			to_string(cur);
			if (need <= 0)
			{
				cout << cur << endl;
				flag = 1;
				break;
			}
			cur += n;
		}
		if (flag == 0)
			cout << "INSOMNIA\n";

	}
	return 0;
}