#include<stdio.h>
#include<string.h>
int main()
{
	FILE *p1,*p2;
	p1=fopen("large.in","r");
	p2=fopen("output.out","w");
	int t;
	fscanf(p1,"%d",&t);
	for(int a=0;a<t;a++)
	{
	
	
	
	
	//printf("yoo");
		char name[10000]="";
		char temp;
		char temp1[10000]="";
		char temp2[10000]="";
		
		fscanf(p1,"%s",name);
		temp1[0]=name[0];
	//	printf("\n%s\n",temp1);
		for(int b=1;b<strlen(name);b++)
		{
			char temp3[1000]="";
			
			temp2[0]=name[b];
		//	printf("\n  %s   %s",temp2,temp1);
			strcpy(temp3,temp2);
			if(temp2[0]>=temp1[0])
			{
				
				strcpy(temp1,(strcat(temp3,temp1)));
			
			}
			else
			{
				strcpy(temp1,(strcat(temp1,temp3)));
			}
		}
	
	
		fprintf(p2,"Case #%d: %s\n",a+1,temp1);
		
	}
}
