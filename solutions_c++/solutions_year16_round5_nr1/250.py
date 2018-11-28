#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <stack>

#define TEST_NUM "a2"
//#define DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG
char inname[100];
char outname[100];

char arr[20010];
std::stack<char> stk;

void process()
{
	int r = 0, i;
	scanf("%s", arr);

	while(!stk.empty())
		stk.pop();

	for(i = 0; arr[i]; i++)
	{
		if(!stk.empty() && arr[i]==stk.top())
		{
			r += 10;
			stk.pop();
		}
		else
			stk.push(arr[i]);
	}
	r += stk.size()/2*5;
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