#include <stdio.h>
#include <string.h>
#include <algorithm>

#define TEST_NUM "aa"
//#define DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG

char arr[1010];

void process()
{
	int k, l, r, i, j;
	scanf("%s%d", arr, &k);

	l = strlen(arr);
	r = 0;
	for(i = 0; i<l-k+1; i++)
	{
		if(arr[i] == '+')
			continue;
		r++;
		for(j = i; j<i+k; j++)
			arr[j] = ('+' + '-' - arr[j]);
	}

	for(i = l-k+1; i<l; i++)
	{
		if(arr[i] == '-')
		{
			printf("IMPOSSIBLE");
			return;
		}
	}

	printf("%d", r);
}

void pre_process()
{

}

int main()
{
#ifndef DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG
#ifdef _DEBUG
	fprintf(stderr, "\nYou are using DEBUG MODE!!!\n\n");
#endif
	char inname[100];
	char outname[100];
	sprintf(inname, "%s.in", TEST_NUM);
	sprintf(outname, "%s.out", TEST_NUM);
	freopen(inname, "r", stdin);
	freopen(outname, "w", stdout);
#endif
	int tn, ti;
	scanf("%d", &tn);
	pre_process();
	for(ti = 1; ti<=tn; ti++)
	{
		fprintf(stderr, "Case %d/%d\n", ti, tn);
		printf("Case #%d: ", ti);
		process();
		printf("\n");
	}
	return 0;
}