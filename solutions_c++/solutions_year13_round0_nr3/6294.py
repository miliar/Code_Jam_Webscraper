#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main()
{
	char start[6], end[6];
	char arr[6], palindromes[6];
	char temp[5];
	int num=0;
	FILE *fp=NULL, *fpout = NULL;
	
	// 배열을 초기화한다.
	
	// 이진 화일을 쓰기 모드로 연다.
	if( (fp = fopen("C-small-attempt0.in", "r")) == NULL )
	{
		fprintf(stderr,"입력을 위한 화일을 열 수 없습니다.\n");
		exit(1);
	}

	if( (fpout = fopen("C-small-attempt0.out", "w")) == NULL )
	{
		fprintf(stderr,"출력을 위한 화일을 열 수 없습니다.\n");
		exit(1);
	}


//	int scoreX =0, scoreY=0;
	fscanf(fp, "%s", temp);
	num = atoi(temp);

//	printf("%d \n", num);
	int palindromes_count=0;
	for(int i=0; i<num; i++)
	{
		fscanf(fp, "%s", start);
		//fflush(stdin);
		fscanf(fp, "%s", end);
		//printf("%s\n", arr);
		//palindromes part
		//printf("%s to %s\n", start, end);
		palindromes_count=0;
		for(int k=atoi(start); k<=atoi(end); k++)
		{
			int p=0;
			//fflush(stdout);
			itoa(k, arr, 10);
		//scanf("%s", arr);
			p = strlen(arr);
			//printf("%d\n", k);

		
			for(int j=0; j<p; j++)
			{
				palindromes[j] = arr[p-j-1];
	//			printf("ar = %s, palindromes = %s\n", arr, palindromes);
			}
			palindromes[p] = NULL ;
			//	printf("ar = %s, palindromes = %s\n", arr, palindromes);
			
			if(strcmp(arr, palindromes) ==0)
			{
				
				
				for(int m=0; m<atoi(arr)+1; m++)
				{
					if(m*m == atoi(arr))
					{
						itoa(m, arr, 10);
					//	printf("ar = %s\n", arr);
						p = strlen(arr);
						for(int j=0; j<p; j++)
						{
							palindromes[j] = arr[p-j-1];
						}
						palindromes[p] = 0 ;
						//printf("ar = %s, palindromes = %s\n", arr, palindromes);
						if(strcmp(arr, palindromes) ==0)
						{
							//
							palindromes_count++;
						}
					}
				}

			}
				//printf("회문\n");
			else
				;
				//printf("아님\n");

		
		}
		//printf("palindromes = %d\n", palindromes_count);
		printf("Case #%d: %d\n", i+1, palindromes_count);
		fprintf(fpout, "Case #%d: %d\n", i+1, palindromes_count);
			/*
			if(scoreX == scoreY && com_bool==0)
			{
				printf("Case #%d: Draw\n", i+1);
				fprintf(fpout, "Case #%d: Draw\n", i+1);
			}
			else if(scoreX > scoreY)
			{
				printf("Case #%d: X won\n", i+1);
				fprintf(fpout, "Case #%d: X won\n", i+1);
			}
			else if(scoreX < scoreY)
			{
				printf("Case #%d: O won\n", i+1);
				fprintf(fpout, "Case #%d: O won\n", i+1);
			}
			else 
			{
				printf("Case #%d: Game has not completed\n", i+1);
				fprintf(fpout, "Case #%d: Game has not completed\n", i+1);
			}
			//printf("%d ", i+1);
			//fprintf(fpout, "score x = %d Y = %d\n", scoreX, scoreY);
			//printf("score x = %d Y = %d\n", scoreX, scoreY);
			scoreX=0;
			scoreY=0;
	*/
	}
}