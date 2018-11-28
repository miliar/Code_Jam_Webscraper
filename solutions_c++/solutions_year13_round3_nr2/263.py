#include "stdio.h"
#include "stdlib.h"
#include <vector>
#include <list>
#include <queue>
#include <string>
using namespace std;



int main()
{
	
	char str[10][10];
	int N;
	scanf("%d",&N);
	gets(str[0]);
	for(int I=1; I<=N; ++I)
	{
		int x, y;
		scanf("%d%d", &x, &y);
		printf("Case #%d: ", I);
		int i;
		if( x < 0 )
		{
			for(i=0; i<-x; ++i)
			{
				printf("EW");
			}
		}
		else 
		{
			for(i=0; i<x; ++i)
			{
				printf("WE");
			}
		}
		if( y < 0 )
		{
			for(i=0; i<-y; ++i)
			{
				printf("NS");
			}
		}
		else 
		{
			for(i=0; i<y; ++i)
			{
				printf("SN");
			}
		}


		printf("\n", y);
	}
	return 0;
}

