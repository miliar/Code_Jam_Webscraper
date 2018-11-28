#include<stdio.h>
#include<string.h>
int main()
{
	FILE *p1,*p2;
	p1=fopen("input1.in","r");
	p2=fopen("output.out","w");
	int u;
	fscanf(p1,"%d",&u);
	for(int a=0;a<u;a++)
	{
	
	
	
	
	
		char string[10000]="";
		char temp;
		char temp1[10000]="";
		char temp2[10000]="";
		
		fscanf(p1,"%s",string);
		temp1[0]=string[0];

		for(int b=1;b<strlen(string);b++)
		{
			char temp3[1000]="";
			
			temp2[0]=string[b];
		
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
