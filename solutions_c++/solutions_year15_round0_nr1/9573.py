#include<stdio.h>

int main()
{
	int casos, i, j,s ,rsq[1010], resp;
	char entrada[1010];
	scanf ("%d", &casos);
	for (i=1;i<=casos;i++)
	{
		scanf (" %d", &s);
		scanf (" %s", entrada);
		rsq[0]=0;
		resp=0;
		for (j=1;j<=s;j++)
		{
			rsq[j]=rsq[j-1]+(entrada[j-1]-48);
		}
		for (j=1;j<=s;j++)
		{
			//printf("%d>%d\n",j, rsq[j]+resp);
			if (j>(rsq[j]+resp))
			{
				resp+=j-(rsq[j]+resp);
				//printf("novo resp %d\n", resp);
			}
		}
		printf("Case #%d: %d\n",i, resp);
	}
}
