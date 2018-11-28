#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>

using namespace std;


void doCase(int caseNumber)
{
	int x,y;
	scanf("%d %d",&x,&y);

	int ** arr = new int *[x];
	for(int i = 0; i < x; i++)
		arr[i] = new int[y];

	for(int i = 0; i < x; i++)
		for(int j = 0; j < y; j++)
			scanf("%d",&arr[i][j]);

	int * xmax = new int[x];
	int * ymax = new int[y];

	memset(xmax,0,sizeof(int)*x);
	memset(ymax,0,sizeof(int)*y);

	for(int i = 0; i < x; i++)
		for(int j = 0; j < y; j++)
			if(arr[i][j] > xmax[i])
				xmax[i] = arr[i][j];

	for(int i = 0; i < y; i++)
		for(int j = 0; j < x; j++)
			if(arr[j][i] > ymax[i])
				ymax[i] = arr[j][i];

	for(int i = 0; i < x; i++)
		for(int j = 0; j < y; j++)
			if(arr[i][j] < xmax[i] && arr[i][j] < ymax[j])
			{
				printf("Case #%d: NO\n",caseNumber);
				return;
			}

	printf("Case #%d: YES\n",caseNumber);
	
}

int main(int argc, char const *argv[])
{
	int testCases;
	scanf("%d",&testCases);

	for(int i = 0; i < testCases; i++)
		doCase(i+1);

	return 0;
}
