
#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<vector>
#include<stdio.h>
#include<memory.h>
#include<set>
#include<queue>
#include<map>
#include<string>
#include<algorithm>
using namespace std;
vector<string>all;

int n, j, t;
void gen(string s)
{
	if (s.size() == n)
	{
		if(s[0]=='1' && s[s.size()-1]=='1' )
			all.push_back(s);
		return;
	}
	gen(s + '0');
	gen(s + '1');
}
bool is_prime(long long p)
{
	if (p == 1)
		return 0;
	if (p == 2)
		return 0;
	for (long long i = 2; i*i <= p; ++i)
		if (p%i == 0)
			return 0;
	return 1;
}
long long getconv(string s, int base)
{
	long long f = 1;
	reverse(s.begin(), s.end());
	long long sum = 0;
	for (int i = 0; i < s.size(); ++i)
	{
		if (s[i] == '1')
			sum += f;
		f *= base;
	}
	return sum;
}
long long getdivisor(long long n)
{
	for (long long i = 2; i*i <= n; ++i)
	{
		if (n%i == 0)
			return i;
	}
}
int main() {
	//freopen("C-small-attempt3.in", "r", stdin);
	//freopen("output.out", "w", stdout);
	scanf("%d", &t);
	scanf("%d %d", &n, &j);
	gen("");
	vector<string>jamcoin;
	long long mx = 0;
	for (int i = 0; i < all.size(); ++i)
	{
		bool f = 1;
		for (int j = 2; j < 11; ++j)
		{
			long long ans = getconv(all[i], j);
			mx = max(ans, mx);
			if (is_prime(ans))
			{
				f = 0;
				break;
			}
		}
		if (f)
			jamcoin.push_back(all[i]);
	}
	cout << "Case #1:" << endl;
	for (int i = 0; i < jamcoin.size(); ++i)
	{
		if (!j)
			break;
		cout << jamcoin[i];
		for (int base = 2; base < 11; ++base)
		{
			long long f = getdivisor((getconv(jamcoin[i], base)));
			cout << " " << f;
		}
		cout << endl;
		--j;

	}
	//	cout << getdivisor(getconv("1001", 2)) << endl;
}