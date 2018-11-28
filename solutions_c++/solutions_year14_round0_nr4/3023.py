#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
FILE *in, *out;
int time;
int num;
double a[2000], b[2000];
int ans1, ans2;
int compare(const void *a, const void *b)
{
	double c = *(double *)a;
	double d = *(double *)b;
	if (c >= d)
		return 1;
	return -1;
}
int read()
{
	fscanf(in,"%d",&num);
	int i;
	for (i = 0; i < num; i++)
		fscanf(in,"%lf",&a[i]);
	for (i = 0; i < num; i++)
		fscanf(in,"%lf",&b[i]);
	return 0;
}
int solve()
{
	qsort(a, num, sizeof(double), compare);
	qsort(b, num, sizeof(double), compare);
	ans1 = 0;
	ans2 = num;
	int i, j;
	j = 0;
	for (i = 0; i < num; i++)
	{
		while (j< num &&b[j] < a[i])
			j++;
		if (j == num)
			break;
		ans2 -= 1;
		j++;
	}
	j = 0;
	for (i = 0; i < num; i++)
	{
		while (j < num&&a[j] < b[i])
			j++;
		if (j == num)
			break;
		ans1 += 1;
		j++;
	}
	return 0;
}
int print(int i)
{
	fprintf(out,"Case #%d: ",i);
	fprintf(out,"%d %d\n",ans1,ans2);
	return 0;
}
int main()
{
	in = fopen("D-large.in","r");
	out = fopen("result.txt","w");
	fscanf(in,"%d",&time);
	int i;
	for (i = 1; i <= time; i++)
	{
		read();
		solve();
		print(i);
	}
	return 0;
}