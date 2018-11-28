#include <iostream>
#include <cstdio>
using namespace std;
int main()
{int list[5]= {1,4,9,121,484};
	int t;
		scanf("%d",&t);
	FILE* p;
	p = fopen("output.txt","w");
	for (int j = 1;j <= t;j++)
	{ int a,b;
		scanf("%d %d",&a,&b);
	  int count=0;
	  for (int i=0;i<5;i++)
	  	if (list[i]>=a && list[i]<=b)
			count++;
	 fprintf(p,"Case #%d: %d\n",j,count);
	}
 return 0;}


