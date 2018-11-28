#include <stdio.h>
#include <string.h>
#include <vector>
#define _PATH_ 21
#define _STR_ 2002

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

void print_num(FILE* fop,int out[])
{
	int i,j;
	for(i=0;i<10;i++)
	{
		for(j=0;j<out[i];j++)
		{
			fprintf(fop,"%d",i);
		}
	}
}

int main()
{
	int i,j,k,t,sum[27],out[10];
	char path[_PATH_],pathout[_PATH_],str[_STR_];
	FILE* fip,*fop;
	scanf("%s",path);
	fip=fopen(path,"r");
	change_path(&path[0],&pathout[0]);
	fop=fopen(pathout,"w");
	fscanf(fip,"%d",&t);
	for(i=1;i<=t;i++)
	{
		memset(sum,0,sizeof(sum));
		memset(out,0,sizeof(out));
		fscanf(fip,"%s",str);
		k=strlen(str);
		for(j=0;j<k;j++)
		{
			sum[(str[j]-'A')]++;
		}
		out[0]+=sum['Z'-'A'];
		out[2]+=sum['W'-'A'];
		out[8]+=sum['G'-'A'];
		out[6]+=sum['X'-'A'];
		out[4]+=sum['U'-'A'];
		out[3]=sum['T'-'A']-out[2]-out[8];
		out[7]=sum['S'-'A']-out[6];
		out[1]=sum['O'-'A']-out[0]-out[2]-out[4];
		out[5]=sum['V'-'A']-out[7];
		out[9]=sum['I'-'A']-out[5]-out[8]-out[6];
		fprintf(fop, "Case #%d: ",i);
		print_num(fop,out);
		fprintf(fop,"\n");
	}
	fclose(fip);
	fclose(fop);
	return 0;
}