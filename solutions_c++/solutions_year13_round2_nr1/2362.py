#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>

using namespace std;

struct test
{
	int p;
	int k;
	int a;
};

int main()
{
	int t;
	ifstream fi;
	ofstream fo;
	fi.open("F:\\t\\in");
	fo.open("F:\\t\\out", ios::trunc);
	fi >> t;

	for (int q = 0; q < t; ++q)
	{
		int a;
		int n;
		int *o;
		int c = 10000;
		fi >> a >> n;
		o = new int[n];
		for (int i = 0; i < n; ++i)
			fi >> o[i];

		fo << "Case #" << q + 1 << ": ";

		qsort(o, n, sizeof(int), [](const void *x, const void *y){ return *(int*)x - *(int*)y; });

		queue<test> qq;
		test tmp = {0};
		tmp.k = 0;
		tmp.p = 0;
		tmp.a = a;
		qq.push(tmp);

		while (!qq.empty())
		{
			test tp = qq.front();
			qq.pop();
			if (tp.p == n)
			{
				if (tp.k < c) c = tp.k;
			}
			else
			{
				if (tp.a > o[tp.p])
				{
					test tt;
					tt.k = tp.k;
					tt.p = tp.p + 1;
					tt.a = tp.a + o[tp.p];
					qq.push(tt);
				}
				else
				{
					test tt;
					tt.k = tp.k + 1;
					tt.p = tp.p;
					tt.a = tp.a * 2 - 1;
					if (tp.a * 2 - 1 > 1)
						qq.push(tt);

					tt.k = tp.k + 1;
					tt.p = tp.p + 1;
					tt.a = tp.a;
					qq.push(tt);
				}
			}
		}

		fo << c << endl;
	}
	fi.close();
	fo.close();
	return 0;
}