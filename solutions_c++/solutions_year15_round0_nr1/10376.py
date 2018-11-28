#include<iostream>
#include<cmath>
#include<cstdio>
using namespace std;
int main(){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("output.txt","w",stdout);
	int i, j, n = 0, cases, pep, shy, stand=0;
	char pepc;
	scanf("%d", &cases);

	for(i=0;i<cases;i++)
	{
		scanf("%d", &shy);
		n = stand = 0;
		scanf("%c", &pepc);
		for(j=0;j<=shy;j++)
		{
			scanf("%c", &pepc);
			pep = pepc - '0';
			if(j==0 && pep > 0)
			{
				stand = pep;
				continue;
			}
			if(stand >= j)
			{
				stand += pep;
			}
			else
			{
				n += abs(stand - j);
				stand += pep + abs(stand - j);
			}

		}
	printf("Case #%d: %d\n", i+1, n);
	}

return 0;
}
