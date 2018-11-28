#include<stdio.h>
#include <stdlib.h>

int chartoi(char c)
{
    return c-'0';
}

int main()
{

	FILE *fp;
	fp = fopen("C:\\bbb\\sample2.txt", "r");
	 if( fp == NULL )
   {
      perror("Error while opening the file.\n");
      exit(EXIT_FAILURE);
   }
	 FILE *fp1;
	 fp1 = fopen("C:\\bbb\\output.txt","w");
	  if( fp1 == NULL )
   {
      perror("Error while opening the file.\n");
      exit(EXIT_FAILURE);
   }

	char ch;
	char buff[255];
	int i;
	//ch = fgetc(fp);
	fscanf(fp,"%d",&i);
	//i = chartoi(ch);
	
	ch = fgetc(fp);
	int s = i;
	while(i>0)
	{
		int j;
		int max,count,flag;
		int output=0;
		count=0;
		fscanf(fp,"%d",&j);
		//j= chartoi(fgetc(fp));
		//printf("%d ",j);
		fgetc(fp);

		for(int k=0;k<=j;k++)
		{
			flag = 0;
			int temp;
			temp = chartoi(fgetc(fp)) ;
			if(temp > 0)
				flag=1;
			if(flag && count<k)
			{
				int re = k-count;
				count+=re;
				output+=re;
			}
			count+=temp;
			
		}
		//printf("\n");

		fprintf(fp1,"Case #%d: %d\n",s-i+1,output);
		//printf("Case #%d: %d\n",s-i+1,output);
		fgetc(fp);
		i--;
	}
	
	

    /*while( ( ch = fgetc(fp) ) != EOF )
      printf("%c",ch);*/
	 
	 return 0;

}