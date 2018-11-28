#include <stdio.h>
#include <string.h>
#include <iostream>
#define _PATH_ 21
#define _MAX_STR_ 102

void change_path(char *path,char *pathout)
{
	int i,length;
	length=strlen(&path[0]);
	strcpy(pathout,path);
	for(i=--length;i>=0;i--)
	{
		if(path[i]=='.')
		{
			break;
		}
	}
	pathout[++i]='o';
	pathout[++i]='u';
	pathout[++i]='t';
	pathout[++i]=0;
}

int cut(char *str)
{
	int len=strlen(str);
	for(len--;len>=0;len--)
	{
		if(str[len]=='-')
		{
			break;
		}else
		{
			str[len]=0;
		}
	}
	return ++len;
}

void map(char *str,int end)
{
	int i;
	for(i=0;i<=end;i++)
	{
		if(str[i]=='+')
		{
			str[i]='-';
		}else
		{
			str[i]='+';
		}
	}
}

void trans(char *str,int end)
{
	char trstr[_MAX_STR_];
	int i;
	strcpy(trstr,str);
	for(i=0;i<=end;i++)
	{
		if(str[i]=='+')
		{
			trstr[end-i]='-';
		}else
		{
			trstr[end-i]='+';
		}
	}
	strcpy(str,trstr);
}

int rev(char *str)
{
	int len=cut(str),ans=0;
	if(len==0)
		return 0;
	else if(len==1)
	{
		return 1;
	}else if(len==2)
	{
		if(str[0]=='+'&&str[1]=='-')
			return 2;
		else if(str[0]=='-'&&str[1]=='-')
			return 1;
	}else
	{
		if(str[0]=='+'&&str[len-1]=='-')
		{
			map(str,--len);
		}else{
		trans(str,--len);
	}
		ans++;
		return ans+rev(str); 
	}
}

void deal(FILE* fip, FILE* fop)
{
	int i,t;
	char str[_MAX_STR_];
	fscanf(fip,"%d",&t);
	for(i=1;i<=t;i++){
			fscanf(fip,"%s",str);
			fprintf(fop, "Case #%d: %d\n",i,rev(str));
			fflush(fop);
	}
}

int main()
{
	char path[_PATH_],out[_PATH_];
	FILE *fip,*fop;
	do{
	scanf("%s",path);
	fip=fopen(path,"r");
	}while(fip==NULL);
	change_path(path,out);
	fop=fopen(out,"w");
	deal(fip,fop);
	fclose(fip);
	fclose(fop);
	return 0;
}