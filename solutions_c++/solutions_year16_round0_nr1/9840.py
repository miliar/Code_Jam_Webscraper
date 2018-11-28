#include<stdio.h>
int main()
{
	freopen("A-large.in", "r", stdin);
	FILE *out = fopen("out.txt", "w");
	int Ncase, i, j, k,l, count,flag, total = 0, N[100000], arr[10] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 98 };

	scanf("%d", &Ncase);

	for (i = 0; i < Ncase; i++)
		scanf("%d", &N[i]);


	for (i = 0; i < Ncase; i++)
	{
		flag = 0;
		count = 1;
		flag = 0;
		for (l = 0; l < 10; l++)
			arr[l] = l;
		while (1)
		{
			if (N[i] == 0)
			{
				fprintf(out,"Case #%d: INSOMNIA\n", i + 1, N[i] * count);
				break;
			}
			total = N[i] * count;
			while (total >= 1)
			{
				for (j = 0; j < 10; j++)
					if (total % 10 == arr[j])
						arr[j] = 10;
				total = total / 10;
			}

			for (k = 0; k < 10; k++)
			{
				if (arr[k] != 10)
					flag++;
			}

			if (flag == 0)
			{
				fprintf(out,"Case #%d: %d\n", i + 1, N[i] * (count));
				break;
			}
			flag = 0;
			count++;
		}
		
	}
	return 0;

}