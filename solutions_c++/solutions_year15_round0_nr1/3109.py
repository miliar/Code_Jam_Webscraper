#include"stdio.h"
#include"cmath"
int n,m,sum,ans;
char c;
int main()
{
    FILE* in=fopen("1.in","r");
    FILE* out=fopen("1.out","w");
	//scanf("%d", &n);
	fscanf(in,"%d", &n);
	for (int i = 0; i < n; i++)
	{
		//scanf("%d ", &m);
		fscanf(in,"%d ", &m);
		sum = 0;
		ans = 0;
		for (int j = 0; j <= m; j++)
		{
			//scanf("%c", &c);
			fscanf(in,"%c", &c);
			if (j > sum && c!='0')
			{
				ans += (j - sum);
				sum+=(j - sum);
			}
			sum += (int)(c - '0');
		}
		//printf("Case #%d: %d\n", i + 1, ans);
		fprintf(out,"Case #%d: %d\n", i + 1, ans);
	}
	return 0;
}
