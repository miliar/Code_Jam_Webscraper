#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <string>
#include <math.h>

using namespace std;

int N, J;
int test;
vector<long long> v(11);
vector<long long> print(11);
string str;
int exitFlag = 0;

FILE * fp;
FILE * fp2;

bool isPrime(long long n, int num)
{
	if (n <= 1)
		return false;

	if ((n & 1) == 0)
	{
		if (n == 2) return true;
		else
		{
			print[num] = n / 2;
			return false;
		}
	}

	for (long long i = 3; i*i <= n; i++)
	{
		if (n % i == 0)
		{
			print[num] = n / i;
			return false;
		}
	}
	return true; 
}

void solve(int num, vector<long long> argv, char c)
{
	if (exitFlag) return;
	if (num == N)
	{
		if (str[num - 2] == '0' || c == '0')
			return;

		int flag = 0;
		for (int i = 2; i <= 10; i++)
			if (isPrime(v[i], i) == true)
			{
				flag = 1;
				break;
			}
		if (flag) return;
		else
		{
			fprintf(fp2, "1%s ", str.c_str());
			for (int i = 2; i <= 10; i++)
				fprintf(fp2, "%lld ", print[i]);
			fprintf(fp2, "\n");
			J--;
		}
		if (!J)
			exitFlag = 1;

		return;
	}
	
	str += c;

	for (int i = 2; i <= 10; i++)
	{
		argv[i] = (powl(i, (N-1) - num) * (c - '0'));
		v[i] += argv[i];
	}

	solve(num + 1, argv, '1');
	if (exitFlag) return;
	solve(num + 1, argv, '0');
	if (exitFlag) return;

	for (int i = 2; i <= 10; i++)
	{
		v[i] -= argv[i];
	}
	str.erase(str.length() - 1, 1);
}
int main()
{
	int test;
	fp = fopen("C:/Users/Mycom/Documents/Visual Studio 2013/Projects/pro/Debug/C-small-attempt0.in", "r");
	fp2 = fopen("C:/Users/Mycom/Documents/Visual Studio 2013/Projects/pro/Debug/C-small-attempt0.out", "w");
	fscanf(fp, "%d", &test);

	for (int t = 1; t <= test; t++)
	{
		fscanf(fp, "%d %d", &N, &J);
		vector<long long> argv(11);
		for (int i = 2; i <= 10; i++)
			v[i] = powl(i, (N - 1));
	
		fprintf(fp2, "Case #%d: \n", t);
		solve(1, argv, '1');
		solve(1, argv, '0');

		exitFlag = 0;
		str.clear();

		for (int i = 0; i <= 10; i++)
		{
			v[i] = 0;
			argv[i] = 0;
		}
	}
}