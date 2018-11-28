#include <iostream>
#include <cstdio>
#include <string.h>
#include <algorithm>
using namespace std;

void print(double *a, int n)
{
    for (int i = 0;i < n;i ++)
        cout<<a[i]<<" ";
    cout<<endl;
}

int game1(double *aa, double *bb, int n)
{
    int res = n;
    aa[n] = 2;
    bb[n] = 2;
    int l1 = 0, l2 = 0;
    while (l2 < n)
    {
        while (aa[l1] > bb[l2])
            l2 ++;
        if (l2 == n)
            break;
        l1 ++;
        l2 ++;
        res --;
    }
    return res;
}

int game2(double *a, double *b, int n)
{
    int l1 = 0, l2 = n - 1;
    while (a[l1] < b[l2] && l2 >= 0)
    {
        l1 ++;
        l2 --;
    }
    return l2 + 1;
}

int main()
{
	FILE *fp = fopen("D-large.in", "r");
	FILE *fout = fopen("D-large.out", "w");
	int t;
	//cin >> t;
	fscanf(fp, "%d", &t);
	double a[1001], b[1001];
	for (int k = 0; k < t; k++)
	{
        int n;
        fscanf(fp, "%d", &n);
        for (int i = 0;i < n;i ++)
            fscanf(fp, "%lf", &a[i]);
        for (int i = 0;i < n;i ++)
            fscanf(fp, "%lf", &b[i]);
        sort(a, a + n);
        sort(b, b + n);

        //print(a, n);
        //print(b, n);

        int res1 = game1(a, b, n);
        int res2 = game1(b, a, n);
	    fprintf(fout, "Case #%d: %d %d\n", k + 1, n - res2, res1);
    }
	fclose(fp);
    fclose(fout);
	return 0;
}
