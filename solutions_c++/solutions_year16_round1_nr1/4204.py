#include<stdio.h>
#include<string.h>
int main()
{
	FILE *fp1,*fp2;
	fp1=fopen("input.in","r");
	fp2=fopen("output.out","w");
	int u;
	fscanf(fp1,"%d",&u);
	for(int a=0;a<u;a++)
	{

		char s[10000]="";
		char temp;
		char temp1[10000]="";
		char temp2[10000]="";
		
		fscanf(fp1,"%s",s);
		temp1[0]=s[0];

		for(int b=1;b<strlen(s);b++)
		{
			char temp3[1000]="";
			
			temp2[0]=s[b];
		
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
	
	
		fprintf(fp2,"Case #%d: %s\n",a+1,temp1);
		
	}
}
