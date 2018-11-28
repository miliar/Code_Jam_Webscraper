#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <list>
#include <bitset>
#include <stack>
#include <cmath>
#include <iomanip>
#include <map>
#include <vector>
using namespace std;
#define ull unsigned long long
const int N = 16;
int J = 50;
#define cout fout
fstream fout("C.out");

ull prime(ull a)
{
	if (a < 4)
		return 0;
	ull n = sqrt(a);
	for (ull i = 2; i <= n; i++)
	{
		if (a%i == 0)
			return i;
	}
	return 0;
}

bool solve(ull a)
{
	ull A[9];
	bitset<N> b(a);
	if (b[0] == 0 || b[N - 1] == 0)
		return false;

	for (ull base = 2; base <= 10; base++)
	{
		ull num = 0;
		ull f = 1;
		for (int i = 0; i < N; i++)
		{
			num += b[i] * f;
			f *= base;
		}
		ull factor = prime(num);
		if (factor == 0)
			return false;
		else
			A[base - 2] = factor;		
	}
	cout << b << " ";
	for (int i = 0; i < 8; i++)
		cout << A[i] << " ";
	cout << A[8] << endl;
	return true;
}

int main()
{

	ull start = (1 << N - 1)+ 1;
	ull end = 1 << N;
	cout << "Case #1:" << endl;
	for (ull i = start; i < end && J; i++)
	{
		if (solve(i))
			J--;

	}

	system("pause");
	return 0;
}