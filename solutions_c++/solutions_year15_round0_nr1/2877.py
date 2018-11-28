#include <cstdio>
#include <iostream>
using namespace std;
char a[1003];
int main()
{
	int t;
	scanf("%d", &t);
	for (int k=1; k<=t; k++)
	{
		int s;
		scanf("%d", &s);
		scanf("%s", a);
		int sum=0;
		int add=0;
		for (int i=0; i<=s; i++)
		{
			int p=(int)a[i]-(int)'0';
			int delta=max(0, i-sum);
			add+=delta;
			sum+=p+delta;
		}
		printf("Case #%d: %d\n", k ,add);
	}
	return 0;
}