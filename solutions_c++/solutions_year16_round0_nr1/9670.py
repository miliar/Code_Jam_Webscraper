#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;

set <int> d;
void f (long long x)
{
	while (x > 0)
	{
		d.insert(x%10);
		x /= 10;
	}
}

int main()
{
	int T;
	cin >> T;
	for (int test = 1; test <= T; test++)
	{
		long long n;
		cin >> n;
		printf("%s%d%s","Case #",test,": ");
		if (n == 0)
		{
			printf("%s\n","INSOMNIA");
			continue;
		}
		int l = n;
		while (d.size() < 10)
		{
			f(n);
			n += l;
		}
		printf("%I64d\n",n-l);
		d.clear();
	}
}
