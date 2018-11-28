#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <set>
#include <functional>
#include <numeric>

using namespace std;

typedef unsigned long long ull;

ull reverse_num(ull num)
{
ull rev = 0,dig;

	while (num > 0)
	{
		dig = num % 10;
		rev = rev * 10 + dig;
		num = num / 10;
	}

	return rev;
}

int main() {
int t;
ull n,res,revn;
ull x;
ull y,cof,cof2;

	FILE *in, *out;
	freopen_s(&in, "in.txt", "r", stdin);
	freopen_s(&out, "out.txt", "w", stdout);

	cin >> t;

	for (int i=1;i<=t;i++)
	{
		cin >> n;

		res = 0;

		while (n)
		{
			//cout << "n1:" << n << " res:" << res << endl;

			if (n<=20)
			{
				res += n;
				break;
			}

			if (n % 10 == 0)
			{
				n--;
				res++;
			}

			y = (1+((ull)log10((double)n))) / 2;

			for (ull q=0;q<y;q++)
			{
				if (q==0)
				{
					x = n % 10;
					if (x != 1)
					{
						n -= (x - 1);
						res += (x - 1); 
					}
					//cout << "n2:" << n << " res:" << res << endl;
				}
				else
				{
					cof2 = (ull)pow((double)10,(double)q); 
					cof = cof2*10;
					x = (n % cof) / cof2;
					if (x != 0)
					{
						n -= (cof2 * x);
						res += (cof2 * x); 
					}
					//cout << "n2:" << n << " res:" << res << endl;
				}
			}

			revn = reverse_num(n);

			if (revn < n)
			{
				n = revn;
				res++;
			}
			else
			{
				n--;
				res++;
			}
		}

		cout << "Case #" << i << ": " << res << endl;
	}

	return 0;
}
