#include<cstdio>

int main()
{
	freopen("A-small-attempt5.in","r", stdin);
	freopen("a5.out","w",stdout);
	int t;
	scanf("%d", &t);
	for(int _case = 0; _case < t; ++_case)
	{
		int hashMaybeNum[16];
		int firstGuest;
		int secGuest;
		
		int witchLineTheNumberInSecG[16];
		int lineMarkedCountInSecG[4];

		//init
		for(int i = 0; i < 16; ++i)
		{
			lineMarkedCountInSecG[i / 4] = 0;
			hashMaybeNum[i] = 0;
		}
		
		scanf("%d,",&firstGuest);
		--firstGuest;
		for(int i = 0; i < 4; ++i)
		{
			for(int j = 0; j < 4; ++j)
			{
				int tmpVar;
				scanf("%d",&tmpVar);
				--tmpVar;
				if(i == firstGuest)
				{	
					hashMaybeNum[tmpVar] = 1;	
				}else
				{
					//empty	
				}	
			}	
		}
		
		int sthWrong = false;
		scanf("%d",&secGuest);
		--secGuest;
		for(int i = 0; i < 4; ++i)
		{
			for(int j = 0; j < 4; ++j)
			{
				int tmpVar;
				scanf("%d",&tmpVar);
				--tmpVar;
				if(1 == hashMaybeNum[tmpVar])
				{
					++lineMarkedCountInSecG[i];
					if(lineMarkedCountInSecG[i] > 1) sthWrong = true;
				}
				witchLineTheNumberInSecG[tmpVar] = i;
			}
		}
		
		//solve
		if((lineMarkedCountInSecG[secGuest] == 1))
		{
			for(int i = 0; i < 16; ++i)
			{
				if(hashMaybeNum[i] && (witchLineTheNumberInSecG[i] == secGuest))
				{
					printf("Case #%d: %d\n",_case + 1, i + 1);
					break;
				}			
			}
		}else
		{
			if(lineMarkedCountInSecG[secGuest] == 0)
			{
				printf("Case #%d: Volunteer cheated!\n", _case + 1);
			}
			else 
			{
				printf("Case #%d: Bad magician!\n", _case + 1);
			}
		}
	}
	return 0;
}

/*
3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Case #1: 7
Case #2: Bad magician!
Case #3: Volunteer cheated!
*/
