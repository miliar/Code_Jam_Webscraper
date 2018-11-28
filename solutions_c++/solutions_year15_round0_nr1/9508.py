#include <cstdio>

int calcTest()
{
	int nShy;
	char shy[2000];
	
	char cShy;
	int total = 0;
	int needed = 0;
	scanf("%d ",&nShy);
	for (int c = 0; c <= nShy; c++)
	{
		scanf("%c",&cShy);
		if (total < c)
		{
			needed += c - total;
			total = c;
		}
		total += cShy -'0';
	}
	return needed;
}

int main()
{
	int nTest;
	scanf("%d",&nTest);
	for (int c = 1; c<= nTest; c++)
	{
		int r = calcTest();
		printf("Case #%d: %d\n",c,r);
	}
}
