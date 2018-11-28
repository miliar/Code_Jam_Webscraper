#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>


//using namespace std;



void doet()
{
	int x, y; scanf("%d%d", &x, &y);
	for (int i = 0; i < abs(x); i++)
		printf(x > 0 ? "WE" : "EW");
	for (int i = 0; i < abs(y); i++)
		printf(y > 0 ? "SN" : "NS");
	printf("\n");
}


int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		printf("Case #%d: ", i+1);
		doet();
	}
	return 0;
}

