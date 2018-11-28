# include<stdio.h>
# include<string.h>
# include <stdlib.h>

# define STRLEN 1000 

int check(char string[],int n);
void find(char A[],char B[]);

int main()
{
	int T,n,i,count;
	char string[STRLEN],str[STRLEN];
	FILE *fp_in,*fp_out;

	fp_in=fopen("A-small-attempt0.in","r");
	fp_out=fopen("result.txt","a+");

	fgets(str,STRLEN,fp_in);

	T=atol(str);
//	scanf("%d",&T);
	//	printf("%d\n",T);
//	fprintf(fp_out,"%d\n",T);
	for(i=0;i<T;i++)
	{
		fgets(string,STRLEN,fp_in);
		find(string,str);
		n=atoi(str);

//		scanf("%s%d",string,&n);
//		printf("%s %d\n",string,n);
//		fprintf(fp_out,"%s %d\n",string,n);
		count=check(string,n);

//		printf("Case #%d: %d\n",i+1,count);
		fprintf(fp_out,"Case #%d: %d\n",i+1,count);
	}
	fclose(fp_in);
	fclose(fp_out);
	return 0;
}

int check(char string[],int n)
{
	int count=0,i,j,len,flag;
//	char *pstr,*p,*pstr_end;
	len=strlen(string);
	for(i=0;i<len;i++)
	{
		flag=0;
		for(j=i;j<len;j++)
		{
			if(j>0 && flag!=0 && !(string[j]!='a' && string[j]!='e' && string[j]!='i' && string[j]!='o' && string[j]!='u'))
			{
				flag=0;
			}
			if(string[j]!='a' && string[j]!='e' && string[j]!='i' && string[j]!='o' && string[j]!='u')
			{
				flag++;
				if(flag==n)
				{
					count+=(len-j);
					break;
				}
			}
			
		}
	}
	/*	pstr=string;
	pstr_end=&string[len-1];
	while(pstr!=pstr_end)
	{
	p=pstr;
	i=0;
	while(p!=pstr_end)
	{
	if(*p!='a' && *p!='e' && *p!='i' && *p!='o' && *p!='u' && p!=pstr_end)
	{
				flag++;
				if(flag==n)
				{
				count+=;
				flag=0;
				break;
				}
				}
				else
				{
				flag=0;
				}
				p++;
				i++;
				}
				pstr++;
}*/
	return count;
}
void find(char A[],char B[])
{
	int i;
	char *p=NULL;
	for(i=0;i<strlen(A);i++)
	{
		if(A[i]==' ')
		{
			p=&A[i];
			p++;
			A[i]='\0';
			break;
		}
	}
	strcpy(B,p);
}