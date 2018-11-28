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

int num[6]={1,4,9,121,484 };

//#define LARGE
int main()
{
#ifdef SMALL
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
#endif
#ifdef LARGE
	freopen("A-large (1).in","r",stdin);
	//freopen("A-small.in","r",stdin);
	freopen("A-large.out","w",stdout);
#endif

	int case_n;
	char back;

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
		//scanf("%c",&back);

	//	printf("%d,%d\n",A,B);
		for(int x=0;x<5;x++)
		{
			if(num[x]>=A&&num[x]<=B)
				res++;
		}

		printf("Case #%d: ",i+1);
		printf("%d",res);
		printf("\n");
		scanf("%c",&temp);

	}
	return 0;
}
