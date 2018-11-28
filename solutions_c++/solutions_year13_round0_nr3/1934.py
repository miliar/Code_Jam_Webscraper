#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <set>
#include <vector>
using namespace std;
const long long MOD = 1000000007;
const int MAX = 10000;
const int MAXX = 100000000;
int b[MAXX];
int mul[5] = {1, 10, 100, 1000, 10000};
long long n,m;
long long w[MAX];
bool good(int i)
{
	long long q = i;
	long long p = q * q; q = p;


	long long rq = 0;
	long long tq = q;

	while (tq)
	{
		rq = rq * 10 + tq %10;
		tq/=10;
	}
	return rq == q;
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt;
	cin >> tt;
	int dcount = 1;
		for (int or = 1; or < MAX; ++or)
		{
			if (or == 10) dcount = 2; else if (or == 100) dcount = 3; else if (or == 1000) dcount = 4;

			int t = or;
			int newt = 0;
			int newor = 0; int cc = 0;
			while (cc++ < dcount)
			{
				newt = newt * 10 + t%10;
				t/=10;
			}
			newor = or * mul[dcount] + newt;

			b[newor] = true;
			t = or/10;
			newt = 0;
			cc = 0;
			while (cc++ < dcount-1)
			{
				newt = newt * 10 + t%10;
				t/=10;
			}
			newor = or * mul[dcount-1] + newt;

			b[newor] = true;
		}
	int wc = 0;
	for (int i = 0; i < MAXX; ++i)
		if (b[i] && good(i))
			w[wc++] = (long long)i * (long long )i;

					
	for (int t = 0; t < tt; ++t)
	{
		bool res = false;
		
		cin >> n  >> m;

	
		int count = 0;
		for (int i = 0; i < wc; ++i)
		{
			if (w[i] >=n && w[i] <=m )
			{
				count++;
				//cout << i << " " << (long long)i*i << endl;
			}
		}

		cout << "Case #" << t + 1 << ": " << count << endl;
	}
	return 0;
}