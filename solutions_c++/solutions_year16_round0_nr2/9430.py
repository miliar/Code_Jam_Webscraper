#include<stdio.h>
#include<string.h>
void main()
{
	FILE *fin = fopen("B-large.in","rt");
	FILE *fop = fopen("output.txt","wt");

	char num[4];
	int input_num=0;
	int null_num=0;
	int repeat_num =0;


	//get how many number
	fgets(num,4,fin);

	for(int a=0;a<4;a++)
	{
		if((int)num[a]==-1 ||(int)num[a]==10)
		{
			null_num = a;
			break;
		}
	}
	if(null_num!=0){
		for(int a=null_num;a<4;a++)
		{
			num[a]='\0';
		}
	}

	sscanf(num,"%d",&input_num);	//input_num = T

	char input_c='\0';
	char input_s[101]={'\0',};
	char temp[101]={'\0',};
	int limit=0;
	int i = 0;
	int a=0;
	int b=1;
	int howmany=0;
		

	fseek(fin,strlen(num)+1,SEEK_SET);
	for(repeat_num=0;repeat_num<input_num;repeat_num++)
	{
		limit=0;
		howmany=0;
		memset(temp,'\0',100);
		memset(input_s,'\0',100);
		b=0;
		i=0;

		input_c = fgetc(fin);
		while((int)input_c != 10 && (int)input_c != -1)
		{
			input_s[i]=input_c;
			i++;
			input_c = fgetc(fin);
		}

	
		//compute
		for(b=1;b<strlen(input_s);b++)
		{
			if(input_s[a]==input_s[b])
			{
				limit=b;
			}
			else
			{
				howmany++;
				for(int c=0;c<limit+1;c++)
				{
					temp[100-c] = input_s[c];
					if(temp[100-c] == '+')
						temp[100-c] = '-';
					else if(temp[100-c] == '-')
						temp[100-c] = '+';
				}							
				for(int d=100-limit;d<101;d++)
				{	
					input_s[d-(100-limit)]=temp[d]; 
				}
			
				if(limit+1 != strlen(input_s))
				{
					b=0;
					limit = 0;
				}

			}
			
		}

		if((limit+1) == strlen(input_s) && input_s[0] == '-')
		{
			howmany++;
			for(int a=0; a<strlen(input_s);a++)
			{
				input_s[a] = '+';
			}
		}
		
		//출력
		fprintf(fop,"Case #%d: %d\n",repeat_num+1,howmany);
		//초기화
		
	}
	fclose(fin);
	fclose(fop);
}