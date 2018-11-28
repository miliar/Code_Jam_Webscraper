#include <fstream>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <iomanip>
#define PW 32
#define togen 500
#pragma comment(linker, "/STACK:200000000")
using namespace std;
int  isprime(unsigned int n, int base)
{
	for (int mod = 2; mod <= 99; ++mod)
	{
		int ans = 0;
		int pow = 1;
		for (int i = 0; i < PW; ++i)
		{
			if ((1 << i)&n)
			{
				ans += pow;
			}
			pow = (pow*base) % mod;
		}
		if (ans%mod == 0)
			return mod;
	}
	return -1;
}
int main()
{
	ofstream out("small.out");
	unsigned int st = (1 << PW-1) +1;
	unsigned int dst = st-1;
	int total = 0;
	out << "Case #1:" << endl;
	for (int i = 2; i < dst&&total<togen; i+=2)
	{
		cout << i << endl;
		int ans;
		unsigned int cur = i + st;
		queue<int> anss;
		for (int j = 2; j <= 10; ++j)
		{
			ans = isprime(cur, j);
			if (ans == -1)
			{
				cout << j << " " << cur << endl;
				break;
			}
				
			anss.push(ans);
		}
		if (ans != -1)
		{
			for (int i = PW-1; i >=0; --i)
			{
				if (((1 << i)&cur))
					out << 1;
				else
					out << 0;
			}
			while (!anss.empty())
			{
				out << " " << anss.front();
				anss.pop();
			}
			out << endl;
			total++;
		}
	}
	//system("pause");
	out.close();
	return 0;
}