#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>

#define TEST_NUM "a2"
//#define DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG
char inname[100];
char outname[100];

char res[5000];
char tmp[5000];

void swp(int m)
{
	char t = tmp[m];
	tmp[m] = tmp[m+1];
	tmp[m+1] = t;
}

void process()
{
	int n, r, p, s, a, b, c, x, y, z, t, l, m, i, j;
	scanf("%d%d%d%d", &n, &r, &p, &s);
	t = r+p+s;
	a = p;
	b = r;
	c = s;

	for(i = 0; i<n; i++)
	{
		x = (a+b-c)/2;
		y = (b+c-a)/2;
		z = (c+a-b)/2;
		if(x<0 || y<0 || z<0)
		{
			printf("IMPOSSIBLE");
			return;
		}
		a = x;
		b = y;
		c = z;
	}

	if(x)
		res[0] = 'P';
	else if(y)
		res[0] = 'R';
	else
		res[0] = 'S';
	l = 1;

	for(i = 0; i<n; i++)
	{
		m = 0;
		for(j = 0; j<l; j++)
		{
			if(res[j] == 'P')
			{
				tmp[m] = 'P';
				tmp[m+1] = 'R';
				if((n-i-1)%6>=3)
					swp(m);
				m += 2;
			}
			else if(res[j] == 'R')
			{
				tmp[m] = 'R';
				tmp[m+1] = 'S';
				if(1<=(n-i-1)%6 && (n-i-1)%6<=3)
					swp(m);
				m += 2;
			}
			else
			{
				tmp[m] = 'P';
				tmp[m+1] = 'S';
				if(2<=(n-i-1)%6 && (n-i-1)%6<=4)
					swp(m);
				m += 2;
			}
		}
		for(j = 0; j<m; j++)
			res[j] = tmp[j];
		l = m;
	}

	res[l] = '\0';
	printf("%s", res);
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