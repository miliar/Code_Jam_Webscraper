#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <map>

using namespace std;

int pn = 20;
int prm[1000];

bool checkPrime(int x)
{
	for (int i = 2; i * i <= x; i ++)
		if (x % i == 0) return false;
	return true;
}

void prepare()
{
	int now = 0, x = 2;
	while (now < pn)
	{
		while (!checkPrime(x)) x ++;
		prm[++ now] = x ++;
	}
}

int n, J;
int a[40];
map<int, bool> hash;

void genOne() //[0, 2^30)
{
	int x;
	while (true)
	{
		x = ((rand() & 32767) << 15) + (rand() & 32767);
		x %= (1 << (n - 2));
		if (!hash[x]) break;
	}
	hash[x] = true;
	a[0] = a[n - 1] = 1;
	for (int i = 1; i < n - 1; i ++)
		if (x & (1 << (i - 1))) a[i] = 1;
	else a[i] = 0;
}

int check(int base)
{
	for (int j = 1; j <= pn; j ++)
	{
		int x = prm[j];
		int v = 0;
		for (int i = n - 1; i >= 0; i --) v = (v * base + a[i]) % x;
		if (!v) return x;
	}
	return 0;
}

void print()
{
	for (int i = n - 1; i >= 0; i --) cout << a[i];
	for (int i = 2; i <= 10; i ++) cout << ' ' << check(i);
	cout << endl;
}

void gen()
{
	while (true)
	{
		bool ok = true;
		genOne();
		for (int i = 2; i <= 10 && ok; i ++)
			if (!check(i)) ok = false;
		if (ok) break;
	}
	print();
}

int main()
{
	freopen ("b.in", "r", stdin);
	freopen ("b.out", "w", stdout);
	prepare();
	cin >> n;
	cin >> n >> J;
	cout << "Case #1:" << endl;
	for (int i = 1; i <= J; i ++) gen();
	return 0;
}