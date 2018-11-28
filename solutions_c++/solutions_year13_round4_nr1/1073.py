#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>

using namespace std;

const int MMax = 2*1100;
const int modulo = 1000002013;

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int testnum = 0;
	cin >> testnum;
	for (int testcase = 1; testcase <= testnum; testcase++)
	{
		unsigned long long in[MMax], out[MMax], stat[MMax], now[MMax] = {0};
		int col = 0;
		int n, m;
		cin >> n >> m;
		
		unsigned long long wnt = 0;
		for (int i = 1; i <= m; i++)
		{
			int a, b, p;
			cin >> a >> b >> p;
			wnt += ((((b - a)*(2*n - (b - a -1))/2) % modulo) * p) % modulo;

			bool pa = false, pb = false;
			for (int j = 1; j <= col; j++)
			{
				if (stat[j] == a)
				{
					pa = true;
					in[j] += p;
				}
				if (stat[j] == b)
				{
					pb = true;
					out[j] += p;
				}
			}

			if (!pa)
			{
				col++;
				stat[col] = a;
				in[col] = p;
				out[col] = 0;
			}

			if (!pb && a != b)
			{
				col++;
				stat[col] = b;
				in[col] = 0;
				out[col] = p;
			}

			if (a == b && !pa)
			{
				out[col] = p;
			}
		}
	
		for (int i = 1; i < col; i++)
			for (int j = i+1; j <= col; j++)
				if (stat[i] > stat[j])
				{
					swap(stat[i], stat[j]);
					swap(in[i], in[j]);
					swap(out[i], out[j]);
				}
		
		unsigned long long res = 0;
		
		for (int i = 1; i <= col; i++)
		{
			int cur = stat[i];
			now[i] += in[i];

			int pep = out[i];
			int j = i;
			while (pep > 0)
			{
				if (now[j] >= pep)
				{
					now[j] -= pep;

					res +=  ((((stat[i] - stat[j])*(2*n - (stat[i] - stat[j] -1))/2) % modulo) * pep) % modulo;
					pep = 0;
				}
				else
				{
					res +=  ((((stat[i] - stat[j])*(2*n - (stat[i] - stat[j] -1))/2) % modulo) * now[j]) % modulo;
					pep -= now[j];
					now[j] = 0;
				}
				j--;
			}
		}

		cout << "Case #" << testcase << ": " << wnt - res << endl;
	}

	return 0;
}
