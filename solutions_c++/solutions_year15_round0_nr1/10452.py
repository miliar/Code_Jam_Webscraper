#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <vector>

using namespace std;

#define MOD 1000000007
#define llu long long unsigned
#define lld long long
#define ld long
#define gc getchar
#define pc putchar

int scan_d()
{
	int ip = gc(), ret = 0, flag = 1;
	for (; ip < '0' || ip > '9'; ip = gc())
		if (ip == '-')
		{
			flag = -1;
			ip = gc();
			break;
		}
	for (; ip >= '0' && ip <= '9'; ip = gc())
		ret = ret * 10 + ip - '0';
	return flag * ret;
}
ld scan_ld()
{
	int ip = gc(), flag = 1;
	ld ret = 0;
	for (; ip < '0' || ip > '9'; ip = gc())
		if (ip == '-')
		{
			flag = -1;
			ip = gc();
			break;
		}
	for (; ip >= '0' && ip <= '9'; ip = gc())
		ret = ret * 10 + ip - '0';
	return flag * ret;
}
lld scan_lld()
{
	int ip = gc(), flag = 1;
	lld ret = 0;
	for (; ip < '0' || ip > '9'; ip = gc())
		if (ip == '-')
		{
			flag = -1;
			ip = gc();
			break;
		}
	for (; ip >= '0' && ip <= '9'; ip = gc())
		ret = ret * 10 + ip - '0';
	return flag * ret;
}
llu scan_llu()
{
	int ip = gc();
	llu ret = 0;
	for (; ip < '0' || ip > '9'; ip = gc())
		;
	for (; ip >= '0' && ip <= '9'; ip = gc())
		ret = ret * 10 + ip - '0';
	return ret;
}

void print_d(int n)
{
	if (n < 0)
	{
		n = -n;
		pc('-');
	}
	int i = 10;
	char output_buffer[10];
	do
	{
		output_buffer[--i] = (n % 10) + '0';
		n /= 10;
	} while (n);
	do
	{
		pc(output_buffer[i]);
	} while (++i < 10);
}
void print_ld(ld n)
{
	if (n < 0)
	{
		n = -n;
		pc('-');
	}
	int i = 11;
	char output_buffer[11];
	do
	{
		output_buffer[--i] = (n % 10) + '0';
		n /= 10;
	} while (n);
	do
	{
		pc(output_buffer[i]);
	} while (++i < 11);
}
void print_lld(lld n)
{
	if (n < 0)
	{
		n = -n;
		pc('-');
	}
	int i = 21;
	char output_buffer[21];
	do
	{
		output_buffer[--i] = (n % 10) + '0';
		n /= 10;
	} while (n);
	do
	{
		pc(output_buffer[i]);
	} while (++i < 21);
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tt;
	tt = scan_d();
	for (int t = 1; t <= tt; t++)
	{
		lld stand = 0, add = 0, smax = 0;
		string s;
		cin >> smax >> s;

		for (lld si = 0; si <= smax; si++)
		{
			lld curr_s = s[si] - '0';

			if (curr_s != 0 && stand < si)
			{
				add += si - stand;
				stand += add;
			}
			stand += curr_s;
		}

		cout << "Case #" << t << ": " << add << endl;
	}

	return 0;
}
