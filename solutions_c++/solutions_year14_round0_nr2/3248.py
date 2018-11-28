#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;


int main()
{
	FILE *fp = fopen("B-large.in", "r");
	FILE *fout = fopen("B.out", "w");
	int t;
	//cin >> t;
	fscanf(fp, "%d", &t);
	for (int k = 0; k < t; k++)
	{
        double C, F, X;
        double B = 2, T = 0;
        fscanf(fp, "%lf %lf %lf", &C, &F, &X);
        double T1 = X / B;
        double T2 = C / B + X / (B + F);
        while (T1 > T2)
        {
            T = T + C / B;
            B = B + F;
            T1 = X / B;
            T2 = C / B + X / (B + F);
        }
        T = T + T1;
        fprintf(fout, "Case #%d: %0.7lf\n", k + 1, T);
	}
	fclose(fp);
    fclose(fout);
	return 0;
}
