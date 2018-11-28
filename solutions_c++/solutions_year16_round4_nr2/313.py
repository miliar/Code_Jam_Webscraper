#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>

#define TEST_NUM "b2"
//#define DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG
char inname[100];
char outname[100];

double p[200];
double c[200];
double arr[210][210];

void process()
{
	int n, k, i, j, l;
	double r = 0;
	scanf("%d%d", &n, &k);
	for(i = 0; i<n; i++)
		scanf("%lf", &p[i]);

	std::sort(p, p+n);

	for(i = 0; i<=k; i++)
	{
		for(j = 0; j<i; j++)
			c[j] = p[j];
		for(j = 0; j<k-i; j++)
			c[i+j] = p[n-1-j];

		arr[0][0] = 1-c[0];
		arr[0][1] = c[0];
		for(l = 1; l<k; l++)
		{
			arr[l][0] = arr[l-1][0]*(1-c[l]);
			for(j = 1; j<=l+1; j++)
				arr[l][j] = arr[l-1][j-1]*c[l] + arr[l-1][j]*(1-c[l]);
		}
		r = std::max(r, arr[k-1][k/2]);
	}
	printf("%.10lf", r);
}

void pre_process()
{

}

int main()
{
#ifndef DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG
	sprintf(inname, "%s.in", TEST_NUM);
	sprintf(outname, "%s.out", TEST_NUM);
#endif
	freopen(inname, "r", stdin);
	freopen(outname, "w", stdout);
	int tn, ti;
	scanf("%d", &tn);
	pre_process();
	for(ti = 1; ti<=tn; ti++)
	{
		printf("Case #%d: ", ti);
		process();
		printf("\n");
	}
	return 0;
}