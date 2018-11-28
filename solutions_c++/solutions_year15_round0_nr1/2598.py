#include <stdio.h>
int t;
int v[1005];
int conta[1005];
int main()
{
	scanf("%d",&t);
	int teste = 0;
	while(t--)
	{
		teste++;
		
		int soma = 0;
		int S;
		scanf("%d",&S);
		for (int i = 0; i<=S; i++)
		{
			char x;
			scanf(" %c",&x);
			v[i] = x - '0';
			//printf("%d\n",v[i]);
		}
		conta[0] = v[0];
		int resp = 0;
		for (int j=1;j<=S;j++)
		{
			int delta = 0;
			if (conta[j - 1] < j && v[j]>0)
				{resp+= j-conta[j - 1];
					delta = j-conta[j-1];
				}
			conta[j] = delta + conta[j-1] + v[j];
		}
		
		printf("Case #%d: ",teste);
		if (resp < 0) 
			resp = 0;
		printf("%d\n",resp);
	}


	return 0;
}