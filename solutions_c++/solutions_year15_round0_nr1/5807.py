#include <stdio.h>

using namespace std;

char a[1001];

int main()
{
	int t;
	FILE *inp;
	FILE *out;
	inp=fopen("InputFile.txt","r");
	out=fopen("OutputFIle.txt","w");
	fscanf(inp,"%d",&t);

	for(int j=1;j<=t;j++)
	{
		int le;
		fscanf(inp,"%d",&le);

		fscanf(inp,"%s",a);

		int res=0;
		int count1=0;

		for(int i=0;i<=le;i++)
		{
			if((a[i]-'0')==0)
			{
				continue;
			}
			else
			{
				if(count1<i)
				{
					res=res+i-count1;
					count1=i;
				}
				count1=count1+a[i]-'0';
			}
		}

		fprintf(out,"Case #%d: %d\n",j,res);
	}
return 0;}