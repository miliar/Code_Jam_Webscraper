#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
using namespace std;
bool check(char c)
{
	if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u')
	{
		return true;
	}
	return false;

}
int main(void)
{
	int test,count=0;
	FILE *fr=fopen("A-small-attempt0.in","r");
	FILE *fw=fopen("out.txt","w");
	fscanf(fr,"%d",&test);
	while(test--)
	{
		count++;
		char name[120];
		int n_value;
		fscanf(fr,"%s",name);
		fscanf(fr,"%d",&n_value);
		int i,j,k,len=strlen(name);
		int result=0;
		for(i=0;i<len;++i)
		{
			for(j=i+n_value-1;j<len;++j)
			{
				int tmpnum=0;
				for(k=i;k<=j;++k)
				{
					if(!check(name[k]))
					{
						tmpnum++;
						if(tmpnum>=n_value)
						{
							result++;
							break;

						}
						
					}
					else
					{
						tmpnum=0;
					}
				}
			}
		}
		fprintf(fw,"Case #%d: %d\n",count,result);
	}

		

	fclose(fr);
	fclose(fw);
	return 0;
}