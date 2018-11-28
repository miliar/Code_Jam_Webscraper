#include<stdio.h>
#include<string.h>
void main()
{
	FILE *fin = fopen("A-large.in","rt");
	FILE *fop = fopen("output.txt","wt");

	char num[5];
	int input_num=0;
	int null_num;
	int repeat_num =0;


	//get how many number
	fgets(num,5,fin);

	for(int a=0;a<5;a++)
	{
		if((int)num[a]==-1 ||(int)num[a]==10)
		{
			null_num = a;
			break;
		}
	}
	for(int a=null_num;a<5;a++)
	{
		num[a]='\0';
	}

	sscanf(num,"%d",&input_num);


	//get number and compute number

	char input_c='\0';
	char input_s[10]={'\0',};
	char check_arr[11]="0000000000";
	int start = 1;
	int sheep_num=0;
	int i=0;
	int input=0;
	int length=0;

	fseek(fin,strlen(num)+1,SEEK_SET);

	for(repeat_num=0;repeat_num<input_num;repeat_num++)
	{
		memset(check_arr,'0',10);

		input_c = fgetc(fin);
		while((int)input_c != 10 && (int)input_c != -1)
		{
			input_s[i]=input_c;
			i++;
			//fseek(fin,1,SEEK_CUR);
			input_c = fgetc(fin);
		}

		//compute it
		sscanf(input_s,"%d",&input);

		while(strcmp(check_arr,"1111111111") != 0)
		{
			if(start == 1)
			{
				sheep_num=input;
			}
			else
			{
				sheep_num = input*start;
				sprintf(input_s,"%d",sheep_num);
			}

			length = strlen(input_s);

			for(int c=0;c<length;c++)
			{
				switch(input_s[c])
				{
				case '0':
					check_arr[0]='1';
					break;
				case '1':
					check_arr[1]='1';
					break;
				case '2':
					check_arr[2]='1';
					break;
				case '3':
					check_arr[3]='1';
					break;
				case '4':
					check_arr[4]='1';
					break;
				case '5':
					check_arr[5]='1';
					break;
				case '6':
					check_arr[6]='1';
					break;
				case '7':
					check_arr[7]='1';
					break;
				case '8':
					check_arr[8]='1';
					break;
				case '9':
					check_arr[9]='1';
					break;
				}
			
			}
		
			start++;
		
			if(strcmp(check_arr,"1111111111") == 0)
			{
				fprintf(fop,"Case #%d: %d\n",repeat_num+1,sheep_num);
				sheep_num=0;
				start = 1;
				memset(input_s,'\0',9);
				i=0;
			}
			else if(start > 100 || sheep_num == 0)
			{
				fprintf(fop,"Case #%d: INSOMNIA\n",repeat_num+1);
				memset(input_s,'\0',9);
				start = 1;
				sheep_num=0;
				i=0;
				break;
			}
		}
	}
	fclose(fin);
	fclose(fop);
}