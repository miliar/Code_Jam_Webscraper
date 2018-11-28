#include<stdio.h>
#include<string.h>
int main()
{
	FILE *fr,*fw;
	int t,i,j,k,l;
	fr=fopen("2.txt","r");
	fw=fopen("ans.txt","w");
	char str[1000];
	fscanf(fr,"%d",&t);
	long long int c;
	int l1;
	for(l1=0;l1<t;l1++)
	{
		c=0;
		fscanf(fr,"%s",str);
		int l=strlen(str);
		for(i=l-1;i>=0;i--)
		{
			if(str[i]!='+')
			{
				c++;
				for(j=0;j<=i;j++)
				{
					if(str[j]=='+')
					str[j]='-';
					else
					str[j]='+';
				}
			}
		}
		fprintf(fw,"Case #%d: %lld\n",l1+1,c);
	}
	return 0;
}
