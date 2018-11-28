#include <stdio.h>
#include <vector>
#include <queue>
#pragma warning (disable : 4996)
using namespace std;
int pqt = 0;
FILE * fp = fopen("A-large.in", "r");
FILE * fw = fopen("A-large.out", "w");
pair<int, int> escape(pair<int, int> p, int v)
{
	pqt -= v;
	for (int i = 0; i < v; ++i)
		fprintf(fw, "%c", 'A' + p.second);
	return{ p.first - v, p.second };
}
enum NUMBER{FIR, SEC, THR};

int main()
{
	int tc; fscanf(fp, "%d", &tc);
	for (int t = 1; t <= tc; ++t)
	{
		pqt = 0;
		int n; fscanf(fp, "%d", &n);
		vector<pair<int,int>> v;
		for (int i = 0; i < n; ++i)
		{
			int ii; fscanf(fp, "%d", &ii);
			v.push_back({ ii , i});
			pqt += ii;
		}

		fprintf(fw, "Case #%d:", t);
		while (pqt > 0)
		{
			fprintf(fw, " ");
			sort(v.begin(), v.end(), [](pair<int, int> p, pair<int, int> q) {
				return p.first > q.first;
			});

			if (v[FIR].first > v[SEC].first)
				v[FIR] = escape(v[FIR], 2);
			else
			{
				if (pqt == 3 && v[FIR].first == 1)
					v[FIR] = escape(v[FIR], 1);
				else
				{
					v[FIR] = escape(v[FIR], 1);
					v[SEC] = escape(v[SEC], 1);
				}
			}
		}
		fprintf(fw, "\n");


	}
	return 0;
}