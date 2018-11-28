#include <stdio.h>
#include <cstring>
#include <math.h>

int check(char *str)
{
	int len = strlen(str);
	for(int i=0; i < len >> 1; i++)
	{
		if(str[i] != str[len - i - 1])
			return 0;
	}
	return 1;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int i=0; i<T; i++)
	{
		int A,B;
		char str_ori[20];
		char str_sqrt[20];
		getchar();
		scanf("%d%d", &A, &B);
		int cnt = 0;
		printf("Case #%d: ", i+1);
		for(int j=A; j<=B; j++)
		{
			int sq = sqrt(j);
			if(sq * sq != j)
				continue;
			sprintf(str_ori, "%d", j);
			sprintf(str_sqrt, "%d", sq);
			if(check(str_ori) && check(str_sqrt))
				cnt++;
		}
		printf("%d\n", cnt);
	}
	return 0;
}