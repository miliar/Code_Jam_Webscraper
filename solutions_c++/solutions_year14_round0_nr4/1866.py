#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <time.h>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
	int caMax;
	vector <double> bl1, bl2;

	FILE *fin = fopen("1.in", "r");
	FILE *fout = fopen("out.txt", "w");
	fscanf(fin,"%d", &caMax);
	for (int ca = 1; ca <= caMax; ca++)
	{
		int n;
		double db;
		fscanf(fin,"%d", &n);
		bl1.clear();
		bl2.clear();

		for (int i = 0; i < n; i++)
		{
			fscanf(fin,"%lf", &db);
			bl1.push_back(db);
		}
		for (int i = 0; i < n; i++)
		{
			fscanf(fin,"%lf", &db);
			bl2.push_back(db);
		}
		sort(bl1.begin(), bl1.end());
		sort(bl2.begin(), bl2.end());

		//속이기
		int i1 = 0, i2 = 0;
		int op1 = 0, op2 = 0;
		while (1)
		{
			if (bl1[i1] > bl2[i2])
			{
				op1++;
				i1++;
				i2++;
			}
			else 
				i1++;

			if (i1 == n)
				break;
		}

		//정상
		i1 = 0;
		i2 = 0;
		while (1)
		{
			if (bl2[i2] > bl1[i1])
			{
				i1++;
				i2++;
			}
			else 
			{
				i2++;
				op2++;
			}

			if (i2 == n)
				break;
		}

		fprintf(fout, "Case #%d: %d %d\n", ca, op1, op2);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
/*
int main()
{
	int caMax;
	double c, f, x;

	FILE *fout = fopen("out.txt", "w");
	scanf("%d", &caMax);
	for (int ca = 1; ca <= caMax; ca++)
	{
		scanf("%lf", &c);
		scanf("%lf", &f);
		scanf("%lf", &x);
//		scanf("%lf %lf %lf", &c, &f &x);

		double minTime = -1.0f;
		double ft, mt, lt = 0.0f;
		double cc = 2.0f;

		while (1)
		{
			ft = x / cc + lt;
			if (minTime > ft ||  minTime < 0)
				minTime = ft;

			mt = c / cc;
			lt = lt + mt; 
			cc = cc + f;

			if (lt > minTime)
				break;
		}

		fprintf(fout, "Case #%d: %.7lf\n", ca, minTime);
	}
	fclose(fout);
	return 0;
}
*/