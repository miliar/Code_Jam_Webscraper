#include<cstdio>
#include<cstring>
#include<iostream>
#include<fstream>

using namespace std;
int arr[11];
bool check()
{
	for (int i = 0; i < 10; i++)
	{
		if (arr[i] == -1)
		{
			return false;
		}
	}
	return true;
}
int div(int n)
{
	long long i = 1, k = n, ret;
	while (check() != true)
	{

		ret = k;
		while (k != 0)
		{
			arr[k % 10] = k % 10;
			k = k / 10;
		}
		k = n*++i;
	}
	return ret;
}
int main()
{
	ofstream fout("output.out");
	ifstream fin("input.in");
	long long n;
	fin >> n;
	for (int i = 1; i <= n; i++)
	{

		long long in;
		fin >> in;
		memset(arr, -1, sizeof arr);
		if (in == 0)
		{
			fout << "Case #" << i << ": INSOMNIA" << endl;
		}
		else
		{
			long long ans;
			ans = div(in);
			fout << "Case #" << i << ": " << ans << endl;
		}
	}
}
