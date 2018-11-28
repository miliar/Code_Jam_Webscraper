#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>


int main()
{
	FILE *inpf,*outf;
	int buffer1[4],buffer2[4],temp[5][5];
	int i=0,j=0,ch=0,cases=0,k=1,input1,input2;
	
	inpf=fopen("magic.txt","r+");
	outf=fopen("magic_out.txt","w+");
	
	if(inpf!=NULL)
	{
		fscanf(inpf,"%d",&cases);
		while(k<=cases)
		{
			//----FOR TAKING THE INPUT FROM FILE
			fscanf(inpf,"%d",&input1);//for first set 
			ch=0;
			i=0;
			while(ch<4)
			{
				fscanf(inpf,"%d%d%d%d",&temp[i][0],&temp[i][1],&temp[i][2],&temp[i][3]);
				ch++;
				i++;
			}
			for(j=0;j<4;j++)
				buffer1[j]=temp[input1-1][j];
				
			fscanf(inpf,"%d",&input2);//for 2 set
			ch=0;
			i=0;
			while(ch<4)
			{
				fscanf(inpf,"%d%d%d%d",&temp[i][0],&temp[i][1],&temp[i][2],&temp[i][3]);
				ch++;
				i++;
			}
			for(j=0;j<4;j++)
				buffer2[j]=temp[input2-1][j];
			//--INPUT TAKEN AND STORED IN BUFFER1 AND BUFFER2
			
			//--CHECKING FOR A MATCH
			int count=0,ii;
			for(i=0;i<4;i++)	
				for(j=0;j<4;j++)
				if(buffer1[i]==buffer2[j])
				{
					count++;
					ii=i;					
				}
			
			char s1[]="Case #";
			char s2[3];//for the correct case
			char s3[]=": ";
			char s4[3]="0";//for the answer
			char s5[]="Bad magician!";
			char s6[]="Volunteer cheated!";	
			char s7[]="\n";
			if(count==1)//we got a hit
			{
				
				ch=buffer1[ii];			
				itoa(ch,s4,10);//the answer				
				itoa(k,s2,10);//the case number
				
				char *result = (char *)malloc(strlen(s1)+strlen(s2)+strlen(s3)+strlen(s4)+strlen(s7)+1);//+1 for the zero-terminator
				strcpy(result,s1);
				strcat(result,s2);
				strcat(result,s3);
				strcat(result,s4);
				strcat(result,s7);
				fputs(result,outf);
			}
			if(count==0)//volunteer cheated
			{
				itoa(k,s2,10);
				char *result = (char *)malloc(strlen(s1)+strlen(s2)+strlen(s3)+strlen(s6)+strlen(s7)+1);//+1 for the zero-terminator
				strcpy(result,s1);
				strcat(result,s2);
				strcat(result,s3);
				strcat(result,s6);
				strcat(result,s7);
				fputs(result,outf);
			}
			if(count>1)//bad magician
			{
				itoa(k,s2,10);
				char *result = (char *)malloc(strlen(s1)+strlen(s2)+strlen(s3)+strlen(s5)+strlen(s7)+1);//+1 for the zero-terminator
				strcpy(result,s1);
				strcat(result,s2);
				strcat(result,s3);
				strcat(result,s5);
				strcat(result,s7);
				fputs(result,outf);
			}
				
				
				
			k++;
		}
		if(k>cases)
			printf("Done..");
	}
	else
		printf("\nError in opening file: ");
}
