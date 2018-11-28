#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <set>

using namespace std;

int answer[2];
int arrange[2][4][4];

int main(void)
{
	int T = 0;
	int TK = 0;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",++TK);

		for(int i = 0;i < 2;i++)
		{
			scanf("%d",&answer[i]); answer[i]--;
			for(int j = 0;j < 4;j++)
			{
				for(int k = 0;k < 4;k++) scanf("%d",&arrange[i][j][k]);
			}
		}

		for(int i = 0;i < 2;i++) sort(arrange[i][answer[i]],arrange[i][answer[i]]+4);
		int candidate[4];
		int size = set_intersection(arrange[0][answer[0]],arrange[0][answer[0]]+4,arrange[1][answer[1]],arrange[1][answer[1]]+4,candidate)-candidate;
		if(size == 1) printf("%d\n",candidate[0]);
		else if(size > 1) puts("Bad magician!");
		else puts("Volunteer cheated!");
	}
	return 0;
}