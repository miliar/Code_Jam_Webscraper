#include <stdio.h>
#include <string.h>
#include <algorithm>

#define TEST_NUM "a2"
//#define DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG
char inname[100];
char outname[100];

bool chk[10];

void process()
{
	memset(chk, 0, sizeof(chk));

	bool u;
	int i, j;
	long long n, c, t;
	scanf("%lld", &n);

	if(n==0)
	{
		printf("INSOMNIA");
		return;
	}

	c = n;
	while(1)
	{
		t = c;
		while(t)
		{
			chk[t%10] = 1;
			t /= 10;
		}

		u = 1;
		for(i = 0; i<10; i++)
		{
			if(!chk[i])
			{
				u = 0;
				break;
			}
		}

		if(u)
			break;

		c += n;
	}
	printf("%lld", c);
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