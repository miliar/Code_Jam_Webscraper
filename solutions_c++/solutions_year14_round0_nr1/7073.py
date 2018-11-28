#include <stdio.h>
#include <stdlib.h>

int T;
int lig1[4];
int lig2[4];

int
main()
{
	scanf("%d", &T);
	
	for(int Case=1; Case <= T; Case++)
	{
		printf("Case #%d: ", Case);
		int answer;
		scanf("%d", &answer);
		//lig1
		for(int i = 0; i < 4; i++)
		{
			if((i+1) == answer)
			{
				for(int j = 0; j < 4; j++)
				{
					scanf("%d", &lig1[j]);
				}
			}
			else
			{
				int dummy;
				for(int j = 0; j < 4; j++)
				{
					scanf("%d", &dummy);
				}
			}
		}
		//lig2
		scanf("%d", &answer);
		for(int i = 0; i < 4; i++)
		{
			if((i+1) == answer)
			{
				int sInter = 0;
				int vInter = -1;
				for(int j = 0; j < 4; j++)
				{
					int v;
					scanf("%d", &v);
					for(int k = 0; k < 4; k++)
					{
						if(lig1[k] == v)
						{
							sInter++;
							vInter = v;
						}
					}
				}

				if(sInter > 1)
					printf("Bad magician!\n");
				else if(sInter == 0)
					printf("Volunteer cheated!\n");
				else if(sInter == 1)
					printf("%d\n", vInter);

			}
			else
			{
				int dummy;
				for(int j = 0; j < 4; j++)
				{
					scanf("%d", &dummy);
				}
			}
		}




	}


	return 0;
}
