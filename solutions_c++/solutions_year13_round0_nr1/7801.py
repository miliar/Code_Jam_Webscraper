#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main()
{
	char matrix[5][5], matrix2[5][5];
	char temp[3];
	int num=0;
	FILE *fp=NULL, *fpout = NULL;
	
	// 배열을 초기화한다.
	
	// 이진 화일을 쓰기 모드로 연다.
	if( (fp = fopen("A-small-attempt4.in", "r")) == NULL )
	{
		fprintf(stderr,"입력을 위한 화일을 열 수 없습니다.\n");
		exit(1);
	}

	if( (fpout = fopen("A-small-attempt4.out", "w")) == NULL )
	{
		fprintf(stderr,"출력을 위한 화일을 열 수 없습니다.\n");
		exit(1);
	}


	int scoreX =0, scoreY=0;
	fscanf(fp, "%s", temp);
	num = atoi(temp);

//	printf("%d \n", num);

	for(int i=0; i<num; i++)
	{
		fscanf(fp, "%s", matrix[0]);
		fscanf(fp, "%s", matrix[1]);
		fscanf(fp, "%s", matrix[2]);
		fscanf(fp, "%s", matrix[3]);

		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				//printf("%c", matrix2[i][j]);
				matrix2[i][j] = matrix[i][j];

				//printf("%c", matrix2[i][j]);
				if(matrix[i][j] == 'T')
					matrix[i][j] = 'X';
				if(matrix2[i][j] == 'T')
					matrix2[i][j] = 'O';
			//	printf("%c", matrix2[i][j]);
			
			}
			//printf("\n");
		}
		


			if(matrix[0][0] == matrix[1][1] && matrix[0][0] == matrix[2][2] && matrix[0][0] == matrix[3][3] && matrix[0][0] !='.')
			{
				if(matrix[0][0] == 'X')
				{
					scoreX++;
				}
			}
			if(matrix2[0][0] == matrix2[1][1] && matrix2[0][0] == matrix2[2][2] && matrix2[0][0] == matrix2[3][3] && matrix2[0][0] !='.')
			{
				if(matrix2[0][0] == 'O')
				{
					scoreY++;
				}
			}
			if(matrix[0][3] == matrix[1][2] && matrix[0][3] == matrix[2][1] && matrix[0][3] == matrix[3][0] && matrix[0][3] !='.')
			{
				if(matrix[0][3] == 'X')
				{
					scoreX++;
				}
			}


			if(matrix2[0][3] == matrix2[1][2] && matrix2[0][3] == matrix2[2][1] && matrix2[0][3] == matrix2[3][0] && matrix2[0][3] !='.')
			{
				if(matrix2[0][3] == 'O')
				{
					scoreY++;
				}
			}

			for(int j=0; j<4; j++)
			{
				for(int p=0; p<4; p++)
				{
					
					if(j<1)
					{
						if(matrix[j+1][p] == matrix[j][p] && matrix[j+2][p] == matrix[j][p] && matrix[j+3][p] == matrix[j][p] && matrix[j][p] !='.')
						{
							if(matrix[j][p] == 'X')
							{
								scoreX++;
							}
						}
						if(matrix2[j+1][p] == matrix2[j][p] && matrix[j+2][p] == matrix2[j][p] && matrix2[j+3][p] == matrix2[j][p]&& matrix[j][p] !='.')
						{
							if(matrix2[j][p] == 'O')
							{
								scoreY++;
							}
	//						else if(matrix[j][p] == 'O')
	//						{
	//							scoreY++;
	//						}
						}

						

					}
					if(p<1)
					{
						if(matrix[j][p+1] == matrix[j][p] && matrix[j][p+2] == matrix[j][p] && matrix[j][p+3] == matrix[j][p]&& matrix[j][p] !='.')
						{
							if(matrix[j][p] == 'X')
							{
								scoreX++;
							}
						}
						if(matrix2[j][p+1] == matrix2[j][p] && matrix2[j][p+2] == matrix2[j][p] && matrix2[j][p+3] == matrix2[j][p]&& matrix[j][p] !='.')
						{
							if(matrix2[j][p] == 'O')
							{
								scoreY++;
							}
	//						else if(matrix[j][p] == 'O')
	//						{
	//							scoreY++;
	//						}
						}
					}
				}
			}
			int com_bool=0;
			for(int i=0; i<4; i++)
			{
				for(int j=0; j<4; j++)
				{
									//printf("%c", matrix2[i][j]);
					if(matrix[i][j] == '.')
						com_bool=1;
			
				}
				//printf("\n");
			}
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
	
	}
}