// pr1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include "stdio.h"
#include "string.h"


int check_0(char *ss)
{
int i=0,num=0;
int len=strlen(ss);
for(i=0;i<len;i++)
{
if (*(ss+i)=='0') num++; 
}

return num;
}


int first_0(char *ss)
{
int i=0,num=0;
int len=strlen(ss);
for(i=0;i<len;i++)
{
if (*(ss+i)!='0') break;
else num++;
}

return num;
}


int xfirst_0(char *ss)
{
int i=0,num=0;
int len=strlen(ss);
for(i=0;i<len;i++)
{
if (*(ss+i)!='0') break;
else num++;
}

return num;
}



int sumz(char *ss,int index)
{
int i=0,num=0;
int len=strlen(ss);
int sum=0;

for(i=0;i<index;i++)
{
sum=sum+ (*(ss+i)-'0'); 
}

return sum;
}

int need_idx=0;
int need_val[1000];

int new_sum(char *ss)
{
int i=0,j=strlen(ss);
int need_num=0;
int old_num=0;
	need_idx=0;
int  current_num=0; 
int delta_val=0;

for(i=0;i<j;i++)
	{
	if ( *(ss+i)!='0' )
		{
		current_num=(*(ss+i)-'0');
		if(need_num<0)
		{
		need_val[need_idx]=need_num;
		need_idx++;
		need_num=need_num+(*(ss+i)-'1')-need_val[need_idx-1];
		//need_num=0;
		//delta_val=delta_val+(*(ss+i)-'1');
		continue;
		}
		need_num=need_num+(*(ss+i)-'1');
		delta_val=delta_val+(*(ss+i)-'1');
		}
	else 
		{
			need_num--;

		}
	if (need_num<0 && current_num>0)
	{
		//need_val[need_idx]=old_num;
		//need_val[need_idx]=need_num;
		//need_idx++;
		//need_num=0;
	}
	old_num=need_num;


	}

if (need_num<0 ) 
{
		need_val[need_idx]=need_num;
		need_idx++;
}
return need_idx;

}

int get_last_0(char *ss)
{
int i=0,num=0;
int len=strlen(ss);
for(i=len-1;i>=0;i--)
{
if (*(ss+i)=='0') return i+1; 
}

return -1;
}


int _tmain(int argc, _TCHAR* argv[])
{
  FILE *fp,*out;
  int total_case;
  int i;
  char str[2000];
  char whitespc[4]="\r\n ";
  char *token;
	int token_cnt=0;

	out=fopen("output.txt","wt");

  fp=fopen("A-large.in","rt");
//	fp=fopen("input.txt","rt");
  if (fp)
  {
 	fscanf(fp,"%d\n",&total_case);
	for(i=0;i<total_case;i++)
	{
	fgets(str,1500,fp);
	token_cnt=0;
	token=strtok(str,whitespc);
	 while (token)
	 {

		printf("%s ",token);

		token_cnt++;
		if (token_cnt==2)
		{
			int k=0;
			int ans=0;
			memset(need_val,0,sizeof(need_val));
			int last0=new_sum(token);
			for(k=0;k<need_idx;k++)
			{
			ans=ans+need_val[k];
			}

			
				fprintf(out," Case #%d: %d\n",i+1,-ans);

		}


		token=strtok(NULL,whitespc);

	 }


	}




  }


 if (fp)
 {
	 fclose(fp);
	 fclose(out);


 }


	return 0;
}

