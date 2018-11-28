#include <stdio.h>
#include <stdlib.h>
#include <string.h>




void main()
{
	char start[20], end[20];
	int original_mt[100][100], fix_mt[100][100], temp_mt[100];
	char temp[6], yes_no[5];
	int num=0, max_num=0, stop_flag=0, fix_num=0;
	FILE *fp=NULL, *fpout = NULL;
	
	// 배열을 초기화한다.
	
	// 이진 화일을 쓰기 모드로 연다.
	if( (fp = fopen("B-small-attempt2.in", "r")) == NULL )
	{
		fprintf(stderr,"입력을 위한 화일을 열 수 없습니다.\n");
		exit(1);
	}

	if( (fpout = fopen("B-small-attempt2.out", "w")) == NULL )
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
		
		
		for(int i=0; i<atoi(start);i++)
		{
			for(int j=0; j<atoi(end);j++)
			{
				fscanf(fp, "%d", &original_mt[i][j]);
				if(original_mt[i][j]>max_num)
					max_num=original_mt[i][j];

				printf("%d", original_mt[i][j]);
			}
			printf("\n");
		}
		//printf("max = %d", max_num);
		fix_num= max_num-1;
		printf("\n");printf("\n");
		//fix_mt init
		for(int i=0; i<atoi(start);i++)
		{
			for(int j=0; j<atoi(end);j++)
			{ 
				
				fix_mt[i][j] = max_num;
				//if(fix_mt[i][j] ==2)
				//printf("%d", fix_mt[i][j]);
			}
			//printf("\n");
		}
		//printf("\n");printf("\n");
		//행 빼기
		for(int i=0; i<atoi(start);i++)
		{
			for(int j=0; j<atoi(end);j++)
			{ 
				temp_mt[j] = fix_mt[i][j];
				fix_mt[i][j]=fix_num;

				if(fix_mt[i][j] < original_mt[i][j] || fix_mt[i][j] < 1)
				{
					for(int p=0; p<=j; p++)
					{
						if(fix_mt[i][p] < 1)
							stop_flag=1;
						fix_mt[i][p]=temp_mt[p];
						
					}
					break;
				}
								
			}
			if(stop_flag==1)
				break;
			if(i ==(atoi(start)-1))
			{
				fix_num--;
				i= i%(atoi(start));
			}
		}
		stop_flag=0;
		fix_num= max_num-1;
		//열 빼기
		for(int i=0; i<atoi(end);i++)
		{
			for(int j=0; j<atoi(start);j++)
			{ 
				temp_mt[j] = fix_mt[j][i];
				fix_mt[j][i]=fix_num;
				if(fix_mt[j][i] < original_mt[j][i] || fix_mt[j][i] < 1)
				{
					for(int p=0; p<=j; p++)
					{
						if(fix_mt[p][i] < 1)
							stop_flag=1;
						fix_mt[p][i]=temp_mt[p];
						
					}
					break;
				}
								
			}
			if(stop_flag==1)
				break;
			if(i ==(atoi(end)-1))
			{
				fix_num--;
				i= i%(atoi(end));
			}
		}
		stop_flag=0;
		//print after fixing
		for(int i=0; i<atoi(start);i++)
		{
			for(int j=0; j<atoi(end);j++)
			{
				//fscanf(fp, "%d", &original_mt[i][j]);
				//if(original_mt[i][j]>max_num)
				//	max_num=original_mt[i][j];

				printf("%d", fix_mt[i][j]);
			}
			printf("\n");
		}
		stop_flag=0;
		//원본과 비교
		for(int i=0; i<atoi(start);i++)
		{
			for(int j=0; j<atoi(end);j++)
			{
				
				if(original_mt[i][j] != fix_mt[i][j])
				{
					strcpy(yes_no, "NO");
					stop_flag=1;
					break;
				}
				else
					strcpy(yes_no, "YES");

				//printf("%d", original_mt[i][j]);
			}
			if(stop_flag==1)
				break;
			//printf("\n");
		}
		printf("Case #%d: %s\n", i+1, yes_no);
		fprintf(fpout, "Case #%d: %s\n", i+1, yes_no);
		stop_flag=0;

		max_num =0;
		//printf("palindromes = %d\n", palindromes_count);
		//printf("Case #%d: %d\n", i+1, palindromes_count);
		//fprintf(fpout, "Case #%d: %d\n", i+1, palindromes_count);
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