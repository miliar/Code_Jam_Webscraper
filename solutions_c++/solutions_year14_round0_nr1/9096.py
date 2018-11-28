#include <stdio.h>
typedef struct{
	int r[4];
	int c[4];
}google;
google goo;
int main()
{
	int c[4][4],d[4][4];
	int i,j,n,Case,answer,a,b,answer2,count=0,count2=0;
	FILE *p;
	FILE *q;
	p=fopen("A-small-attempt2.in","rt");
	
	q=fopen("output.txt","w");
	if (p==NULL)      { 
		printf("에러 : input.txt파일을 열 수 없습니다.\n");   
		return 0;    
	} 
	fscanf(p,"%d",&Case);
	while(Case--){
		count++;
		fscanf(p,"%d",&answer);
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			fscanf(p,"%d",&c[i][j]);
		}
	}
	fscanf(p,"%d",&answer2);
		for(a=0;a<4;a++)
	{
		for(b=0;b<4;b++)
		{
			fscanf(p,"%d",&d[a][b]);
		}
	}
		 
	i=answer-1;
	for(j=0;j<4;j++){
		goo.r[j]=c[i][j];
	}
	i=answer2-1;
	for(j=0;j<4;j++){
		goo.c[j]=d[i][j];
	}
	for(i=0;i<4;i++){
		for(j=0;j<4;j++)
		{
			if(goo.r[i]==goo.c[j])
			{
				n=goo.r[i];count2++;
			}
			
		}
	}
	if(count2==0)
	{ 
		fprintf(q,"Case #%d: Volunteer cheated!\n",count);
		
	}
	else if(count2==1){
		fprintf(q,"Case #%d: %d\n",count,n);
	}
			else if(count>1){
				fprintf(q,"Case #%d: Bad magician!\n",count);
			}
			
				count2=0;
	}
	return 0;
}
