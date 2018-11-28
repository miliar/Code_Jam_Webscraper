#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cstdlib>

using namespace std;

void read(int cards[])
{
	int Answer;
	scanf("%d",&Answer);
	for(int row=1;row<=4;row++)
	{
		if(row==Answer)
		{
			scanf("%d %d %d %d",&cards[0],&cards[1],&cards[2],&cards[3]);
			continue;
		}
		int t=0;
		scanf("%d %d %d %d",&t,&t,&t,&t);
	}
}

int main()
{
	int Testcases=0;
	scanf("%d",&Testcases);

	for(int nTestcases=1;nTestcases<=Testcases;nTestcases++)
	{
		int cards1[4];read(cards1);
		int cards2[4];read(cards2);
		int countMatched=0,cardnumber=0;

		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(cards1[i]==cards2[j]){countMatched++;cardnumber=cards1[i];}			
			}
		}

		if(countMatched==0){printf("Case #%d: Volunteer cheated!\n",nTestcases);}
		else if(countMatched==1){printf("Case #%d: %d\n",nTestcases,cardnumber);}
		if(countMatched>=2){printf("Case #%d: Bad magician!\n",nTestcases);}

	}
	return 0;
}
