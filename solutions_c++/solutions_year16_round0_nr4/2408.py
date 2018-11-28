#include <cstdio>
#include <vector>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <stdio.h>
#include <fstream>
using namespace std;


int div(long long h)
{
	if (h % 2 == 0)
		return 2;
	long double x = sqrt(h);
	long long up = (int(x) + 5);
	for (int i = 3; i < up; i += 2)
	{
		if (h%i == 0)
			return i;
	}
	return -1;
}

long long res(string h, long long base)
{
	string x = h;
	int l = x.length();
	long long res = 0;
	for (int i = 0; i < l; i++)
	{
		res *= base;
		res += (x[i]-'0');
	}
	return res;
}


string gen(long long k,int len)
{
	string res(len, '0');
	long long x = k;
	int i = len - 1;
	while (x != 0)
	{
		res[i] = (x % 2)+'0';
		i--;
		x /= 2;
	}
	return res;
}

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");


	int qq;
	cin >> qq;
	for (int qqq = 0; qqq < qq; qqq++)
	{
		cout << "Case #" << qqq + 1 << ": ";
		long long k, c, s;
		cin >> k >> c >> s;
		for (int i = 1; i <= k; i++)
		{
			cout << i << " ";
		}
		cout << endl;
	}





		/*cout << endl;
		long long n,k;
		cin >> n>>k;
		string x(n,0);
		int start = 32769;
		int finish = 65536;
		for (int i = start; i < finish; i += 2)
		{
			if (k>0)
			{

				string x = gen(i, 16);
				vector <int> ans;
				for (int j = 2; j <= 10; j++)
				{
					long long num = res(x, j);
					int h = div(num);
					if (h == -1)
						break;
					ans.push_back(h);
				}
				if (ans.size() == 9)
				{
					k--;
					cout << x << " ";
					for (int i = 0; i < 9; i++)
					{
						cout << ans[i] << " ";
					}
					cout << endl;
				}
			}
			
		}

		

	}
	*/
	return 0;
}