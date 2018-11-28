#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;


int main()
{
	FILE *f1, *f2;
	freopen_s(&f1, "in.txt", "r+", stdin);
	freopen_s(&f2, "out.txt", "w+", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		string S;
		char pos = '+';
		int ans = 0;
		cin>>S;
		for (int i = S.length() - 1; i >= 0; i--)
		{
			if (pos != S[i])
			{
				pos = S[i];
				ans++;
			}
		}
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}

#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

long long power(long long a, long long b)
{
	long long res = 1;
	while (b)
	{
		if (b & 1)
		{
			res *= a;
		}
		a *= a;
		b >>= 1;
	}
	return res;
}

long long isprime(long long a)
{
	for (long long i = 2; i*i <= a; i++)
	{
		if (a%i == 0)
		{
			return i;
		}
	}
	return 1;
}

int main()
{
	FILE *f1, *f2;
	freopen_s(&f1, "in.txt", "r+", stdin);
	freopen_s(&f2, "out.txt", "w+", stdout);
	cout << "Case #1:" << endl;
	int T;
	cin >> T;
	int N = 16, J = 50;
	cin >> N >> J;
	int z = 32769;
	long long numb;
	long long ch[11];
	while (J > 0)
	{
		for (; z <= 65535&&J>0; z += 2)
		{
			bool flag = true;
			long long k = 0;
			for (long long i = 2; i <= 10; i++)
			{
				k = 0;
				for (int j = 1,t=0; j <= 1 << 16; j <<= 1,t++)
				{
					if (z&j)
					{
						k += power(i, t);
					}
				}
				ch[i] = isprime(k);
				if (ch[i] == 1)
				{
					flag = false;
					break;
				}
			}
			if (flag)
			{
				for (int j = 1<<15; j >0; j >>=1)
				{
					if (z&j)
					{
						cout << "1";
					}
					else
					{
						cout << "0";
					}
				}
				cout << " ";
				for (int j = 2; j <= 10; j++)
				{
					cout << ch[j] << " ";
				}
				cout << endl;
				J--;
			}
		}
	}
	cin >> T;
	//printf("Case #%d: %d\n", i, ans);
	return 0;
}