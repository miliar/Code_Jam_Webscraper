#include<stdio.h>

int main()
{
	FILE *i_fileOut;
	fopen_s(&i_fileOut, "QualA.out", "w");
	int n;
	scanf("%d", &n);
	for (int i_case = 1 ; i_case <= n ; i_case++)
	{
		printf("Case #%d: ", i_case);
		fprintf(i_fileOut, "Case #%d: ", i_case);
		
		int Smax = 0;
		scanf("%d", &Smax);

		int i_current = 0;
		int i_ans = 0;

		for (int i = 0 ; i <= Smax ; i++)
		{
			unsigned char ch;
			while (true)
			{
				scanf("%c", &ch);
				if (ch >= '0' && ch <= '9') break;
			}

			ch -= '0';

			if (i_current >= i)
			{
				i_current += ch;
			} else
			{
				i_ans += (i - i_current);
				i_current = i + ch;
			}
		}

		printf("%d\n", i_ans);
		fprintf(i_fileOut, "%d\n", i_ans);
	}

	fclose(i_fileOut);
	return 0;
}