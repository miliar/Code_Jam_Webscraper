#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

#define FILE_NAME "A-small-attempt1"
#define ULL unsigned long long

char buffer[2048];

int main()
{
	int case_num, i, chosenRow, num;
	vector<int> first,second;

	sprintf(buffer, "%s.in", FILE_NAME);
	freopen(buffer, "r", stdin);
	sprintf(buffer, "%s.out", FILE_NAME);
	freopen(buffer, "w", stdout);

	scanf("%d", &case_num);
	i=1;
	while(i<=case_num)
	{
		printf("Case #%d: ", i);
		
		first.clear();
		second.clear();
		scanf("%d", &chosenRow);
		for(int m=0;m<4;m++)
		{
			for(int n=0;n<4;n++)
			{
				scanf("%d", &num);
				if((m+1)==chosenRow)
					first.push_back(num);
			}
		}
		scanf("%d", &chosenRow);
		for(int m=0;m<4;m++)
		{
			for(int n=0;n<4;n++)
			{
				scanf("%d", &num);
				if((m+1)==chosenRow)
				{
					second.push_back(num);
				}
			}
		}

		int match = 0, answer = 0;
		for(int m=0;m<4;m++)
		{
			for(int n=0;n<4;n++)
			{
				if(first[m]==second[n])
				{
					match++;
					answer = first[m];
					continue;
				}
			}
		}

		if(match>=2)
			printf("%s", "Bad magician!");
		else if(match==1)
			printf("%d", answer);
		else
			printf("%s", "Volunteer cheated!");

		printf("\n");
		i++;
	}
		
	return 0;
}