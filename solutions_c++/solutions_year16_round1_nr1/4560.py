#include<stdio.h>
#include<string.h>
void main()
{
	FILE *fin = fopen("A-small-attempt1.in","rt");
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
	char input_s[1001]={'\0',};
	int i = 0;
	int alpha_len=0;
	char temp;
	char temp_c;
	
		

	fseek(fin,strlen(num)+1,SEEK_SET);
	for(repeat_num=0;repeat_num<input_num;repeat_num++)
	{
		memset(input_s,'\0',100);
		i=0;

		input_c = fgetc(fin);
		while((int)input_c != 10 && (int)input_c != -1)
		{
			input_s[i]=input_c;
			i++;
			input_c = fgetc(fin);
		}

	
		//compute
		alpha_len = strlen(input_s);
		for(int p=0;p<alpha_len;p++)
		{
			if(p==0)
			{
				temp = input_s[p];
				temp_c = '\0';
			}
			else
			{
				if((int)temp <= (int)input_s[p])
				{
					temp_c = input_s[p];
					input_s[p] = '\0';
					if(p>0 && p<alpha_len)
					{
						for(int q=p;q<alpha_len;q++)
						{
							input_s[q] = input_s[q+1];
						}
					}
					for(int t=alpha_len;t>=1;t--)
					{
						input_s[t] = input_s[t-1];
					}
					input_s[0] = temp_c;
					temp = input_s[0];
				}
			}
		}
		
		//출력
		fprintf(fop,"Case #%d: %s\n",repeat_num+1,input_s);
		//초기화
		
	}
	fclose(fin);
	fclose(fop);
}