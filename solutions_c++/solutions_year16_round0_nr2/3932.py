#include <stdio.h>
#include <string.h>
#include <algorithm>

#define TEST_NUM "b2"
//#define DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG
char inname[100];
char outname[100];

char arr[101];

void process()
{
	int r = 0, i;
	scanf("%s", arr);

	for(i = 0; arr[i]; i++)
		if(arr[i+1]&&arr[i]!=arr[i+1] || !arr[i+1]&&arr[i]=='-')
			r++;

	printf("%d", r);
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