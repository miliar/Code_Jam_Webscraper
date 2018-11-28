#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int main()
{
	freopen("test.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testCases;
	scanf("%d", &testCases);
	for (int a=0; a<testCases;a++)
	{
		bool possibilities[17];
		memset (possibilities,false,sizeof(possibilities));
		int totalMatches;
		int matchingNumber;
		for (int b=0; b<2; b++)
		{
			totalMatches=0;
			int targetRow;
			scanf("%d", &targetRow);
			targetRow--;
			for (int bc=0; bc<4; bc++)
			{
				for (int dd=0; dd<4; dd++)
				{
					int index;
					scanf("%d", &index);
					if  (bc!=targetRow) continue;
					if (!possibilities[index]&&b>0) continue;
					possibilities[index]=true;
					if (b>0)
					{
						totalMatches++;
						matchingNumber=index;
					}
					
				}
			}
		}
		printf("Case #%d: ",a+1);
		if (totalMatches<=0) printf("Volunteer cheated!\n");
		else if (totalMatches>1) printf("Bad magician!\n");
		else printf("%d\n", matchingNumber);
	}

}