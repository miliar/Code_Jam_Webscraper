#include "stdafx.h"
#include <vector>
#include <algorithm>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int T = 0, N = 0;
	scanf("%d", &T);

	vector<double> vecnaomi;
	vector<double> vecken;

	int i, j, k;
	double naomi;
	double ken;
	for(j = 0; j < T; j++)
	{
		vecnaomi.clear();
		vecken.clear();

		scanf("%d", &N);

		for(i = 0; i < N; i++)
		{
			scanf("%lf", &naomi);
			vecnaomi.push_back(naomi);
		}
		for(i = 0; i < N; i++)
		{
			scanf("%lf", &ken);
			vecken.push_back(ken);
		}
		sort(vecnaomi.begin(), vecnaomi.begin() + vecnaomi.size());
		sort(vecken.begin(), vecken.begin() + vecken.size());

		int dw = 0, w =0, ind = 0;
		for(i = ind; i < N; i++)
			for(k = ind; k < N; k++)
				if(vecnaomi[i] > vecken[k])
				{
					ind = k + 1;
					dw++;
					break;
				}

		ind = N-1;
		for(i = ind; i >= 0; i--)
			for(k = ind; k >= 0; k--)
				if(vecnaomi[i] > vecken[k])
				{
					w++;
					break;
				} 
				else
				{
					ind = k - 1;
					break;
				}

		printf("Case #%d: %d %d\n", j+1, dw, w); 
	}
	return 0;
}

