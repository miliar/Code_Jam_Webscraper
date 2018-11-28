#include<stdio.h>
#include<string.h>

int main()
{
	int test, i,j,k,l,m;
	char str[1001], res[2500];
	freopen("a.txt","rt", stdin);
	freopen("a_out.txt","wt", stdout);
	scanf("%d",&test);
	for(i = 1; i <= test; i++)
	{
		scanf("%s", str);
		res[1300] = str[0];
		k = 1300;
		l = 1300;
		k++;
		for(j = 1; str[j]; j++)
		{
			if(str[j]<res[l])
			{
				res[k] = str[j];
				k++;

			}
			else
			{
				l--;
				res[l] = str[j];
			}
		}
		printf("Case #%d: ",i);
		for(j = l; j < k; j++)
			printf("%c",res[j]);
		printf("\n");

	}
	return 0;
}