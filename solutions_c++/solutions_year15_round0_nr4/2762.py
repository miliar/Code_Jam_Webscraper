#include<stdio.h>
#include <stdlib.h>

int chartoi(char c)
{
    return c-'0';
}

int min(int x,int y)
{
	if(y<x)
		return y;
	else 
		return x;
}
int main()
{

	FILE *fp;
	fp = fopen("C:\\bbb\\sampled.txt", "r");
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
	//printf("%d",i);
	//i = chartoi(ch);
	
	ch = fgetc(fp);
	int s = i;
	while(i>0)
	{
		int x,r,c;
		int max,count,flag;
		int output=0;
		count=0;
		fscanf(fp,"%d %d %d",&x,&r,&c);
		//j= chartoi(fgetc(fp));
		//printf("%d ",j);
		int arr[4][4] = {-9};
		for(int g=0;g<r;g++)
			for(int h=0;h<c;h++)
				arr[g][h]=0;
		if(x==1)
			flag=0;
		else if(x>(r*c) || x>=7)
			flag = 1;
		else if((r*c)%x !=0)
			flag =1;
		else if(x>=3 && (r==1 || c==1))
			flag = 1;
		else if(x>=3 && min(r,c)<=(x-2))
			flag =1;
		else
		{
			flag=0;




		}

		char *name;
		if(flag)
			name="RICHARD";
		else
			name ="GABRIEL";
		fprintf(fp1,"Case #%d: %s\n",s-i+1,name);
		//printf("Case #%d: %d\n",s-i+1,output);
		fgetc(fp);
		i--;
	}
	
	

    /*while( ( ch = fgetc(fp) ) != EOF )
      printf("%c",ch);*/
	 
	 return 0;

}