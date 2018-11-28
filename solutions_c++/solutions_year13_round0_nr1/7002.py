#include<stdio.h>
#include<stdlib.h>

#define X_COMPLETE_WIN 352
#define X_PARTIAL_WIN 348

#define O_COMPLETE_WIN 316
#define O_PARTIAL_WIN 321

//ord('X')*4 = 352
//(ord('X')*3)+ord('T') = 348

//ord('O')*4 = 316
//(ord('O')*3)+ord('T') = 321

//ord('.')*4 = 184


int play(char *row_0,char *row_1,char *row_2,char *row_3,int roundNo);


int main(int argc,char *argv[])
{
	char *line=NULL;
	size_t lineLen=0;
	int totalRounds=0;
	FILE *fp=NULL;
	fp=fopen(argv[1],"r");
	if(fp!=NULL)
	{
		getline(&line,&lineLen,fp);
		totalRounds=atoi(line);
		for(int i=0;i<totalRounds;i++)
		{			
			char *rows[4]={NULL,NULL,NULL,NULL};
			getline(&rows[0],&lineLen,fp);
			getline(&rows[1],&lineLen,fp);
			getline(&rows[2],&lineLen,fp);
			getline(&rows[3],&lineLen,fp);
			getline(&line,&lineLen,fp);
			play(rows[0],rows[1],rows[2],rows[3],i+1);
		}

		fclose(fp);
	}
	return 0;
}



int play(char *row_0,char *row_1,char *row_2,char *row_3,int roundNo)
{
	int row_sums[4],col_sums[4],diag_sum[2],sums[10];

	sums[0]=row_0[0]+row_0[1]+row_0[2]+row_0[3];
	sums[1]=row_1[0]+row_1[1]+row_1[2]+row_1[3];
	sums[2]=row_2[0]+row_2[1]+row_2[2]+row_2[3];
	sums[3]=row_3[0]+row_3[1]+row_3[2]+row_3[3];
	sums[4]=row_0[0]+row_1[0]+row_2[0]+row_3[0];
	sums[5]=row_0[1]+row_1[1]+row_2[1]+row_3[1];
	sums[6]=row_0[2]+row_1[2]+row_2[2]+row_3[2];
	sums[7]=row_0[3]+row_1[3]+row_2[3]+row_3[3];
	sums[8]=row_0[0]+row_1[1]+row_2[2]+row_3[3];
	sums[9]=row_0[3]+row_1[2]+row_2[1]+row_3[0];


	for(int i=0;i<10;i++)
	{
		switch(sums[i])
		{
			case X_COMPLETE_WIN:
			case X_PARTIAL_WIN:
				printf("Case #%d: X won\n",roundNo);
				return 0;
			case O_COMPLETE_WIN:
			case O_PARTIAL_WIN:
				printf("Case #%d: O won\n",roundNo);
				return 0;
		}
	}
	for(int i=0;i<10;i++)
	{
		if( sums[i]<=O_COMPLETE_WIN)
		{
			printf("Case #%d: Game has not completed\n",roundNo);
			return 0;
		}
	}
	printf("Case #%d: Draw\n",roundNo);
	return 0;
}
