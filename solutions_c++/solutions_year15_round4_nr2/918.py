#include <stdio.h>

#define TEST_NUM 3

char inname[100];
char outname[100];

inline double ab(double x)
{
	return x<0 ? -x : x;
}

inline double mx(double x, double y)
{
	return x>y ? x : y;
}


double ori[100][2];
long long arr[100][2];
/*
void process()
{
	int n, i;
	double ov, ox, r;
	long long v, x;
	scanf("%d%lf%lf%lf%lf", &n, &ov, &ox);
	for(i=0;i<n;i++)
		scanf("%lf%lf", &ori[i][0], &ori[i][1]);
	v=ov*10000;
	x=ox*10000;
	for(i=0;i<n;i++)
	{
		arr[i][0]=ori[i][0]*10000;
		arr[i][1]=ori[i][1]*10000;
	}
	if(n==1)
	{
		if(arr[0][1]==x)
			printf("%.10lf", 1.0*v/arr[0][0]);
		else
			printf("IMPOSSIBLE");
	}
	else
	{
		if(arr[0][1]==arr[1][1])
		{
			if(arr[0][1]==x)
				printf("%.10lf", mx();
		}
	}
}*/

void process()
{
	int n;
	double a, b, c, d, t1, t2, t, x, y;
	scanf("%d%lf%lf%lf%lf", &n, &x, &y, &a, &b);
	if(n==1)
	{
		if(ab(b-y)<1e-5)
			printf("%.10lf", x/a);
		else
			printf("IMPOSSIBLE");
	}
	else
	{
		scanf("%lf%lf", &c, &d);
		if(ab(b-d)<1e-5)
		{
			if(ab(b-y)<1e-5)
			{
				printf("%.10lf",x/(a+c));
			}
			else
				printf("IMPOSSIBLE");
		}
		else
		{
			t1=(y-d)*x/(b-d)/a;
			t2=(b-y)*x/(b-d)/c;
			if(t1>=0&&t2>=0)
				printf("%.10lf", t1>t2 ? t1 : t2);
			else
				printf("IMPOSSIBLE");
		}
	}
}

void pre_process()
{

}

int main()
{
	sprintf(inname, "%d.in", TEST_NUM);
	sprintf(outname, "%d.out", TEST_NUM);
	freopen(inname, "r", stdin);
	freopen(outname, "w", stdout);
	int tn, ti;
	scanf("%d", &tn);
	pre_process();
	for(ti=1;ti<=tn;ti++)
	{
		printf("Case #%d: ", ti);
		process();
		printf("\n");
	}
	return 0;
}