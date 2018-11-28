
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
using namespace std;
#define SMALL

//int num[6]={1,4,9,121,484 };

int lawn[105][105];
bool test[105];

//#define LARGE
int main()
{
#ifdef SMALL
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
#endif
#ifdef LARGE
	freopen("A-large (1).in","r",stdin);
	//freopen("A-small.in","r",stdin);
	freopen("A-large.out","w",stdout);
#endif

	int case_n;
	char back;
	bool OK=true;

	scanf("%d", &case_n);
	scanf("%c",&back);

	for (int i=0; i<case_n; i++)
	{
		char temp;
		int A;
		int B;
		int res=0;
		scanf("%d",&A);
		scanf("%c",&back);
		scanf("%d",&B);

		OK=true;
		//scanf("%c",&back);

		for(int x=0;x<105;x++)test[x]=false;
		for(int x=0;x<A;x++)
		{
			for(int y=0;y<B;y++)
			{
				scanf("%d",&lawn[x][y]);
				scanf("%c",&back);
			}
			//scanf("%c",&back);
		}
/*
		for(int x=0;x<A;x++)
		{
			for(int y=0;y<B;y++)
			{
				printf("%d ",lawn[x][y]);
			}
			printf("\n");
		}
		printf("\n");

		printf("%d,%d\n",A,B);
*/
		for(int x=0;x<A;x++)
		{
			int max_l=0;
			for(int y=0;y<B;y++)
			{
				if(lawn[x][y]>max_l)max_l=lawn[x][y];
			}
			for(int y=0;y<B;y++)
			{
				if(lawn[x][y]<max_l)test[y]=true;
			}
			for(int y=0;y<B;y++)
			{
				if(test[y]==true)
				{
					for(int m=0;m<A;m++)
					{
						if(m!=x)
						{
							if(lawn[m][y]>lawn[x][y])
							{
								OK=false;
								break;
							}
						}
					}
				}
			}
		}

		printf("Case #%d: ",i+1);
		if(OK==true)printf("YES");
		else printf("NO");
		printf("\n");
		//scanf("%c",&temp);

	}
	return 0;
}
