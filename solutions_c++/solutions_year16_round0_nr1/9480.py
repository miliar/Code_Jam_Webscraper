#include <stdio.h>

int main()
{
	int t, n;

	FILE *in = fopen("input.txt", "r");
	FILE *out = fopen("ouput.txt", "w");
	
	fscanf(in, "%d", &t);

	for (int tcnt = 1; tcnt <= t; tcnt++)
	{
		fscanf(in, "%d", &n);
		if (n == 0)
		{
			fprintf(out, "Case #%d: INSOMNIA\n", tcnt);
		}
		else
		{
			int check[10];
			for (int i = 0; i < 10; i++)
				check[i] = 0;

			int count = 0, N = n;
			while (true)
			{
				int temp = n;
				while (temp > 0)
				{
					if (check[temp % 10] == 0)
					{
						count++;
						check[temp % 10] = 1;
					}

					temp /= 10;
				}

				if (count == 10)
					break;

				n += N;
			}

			fprintf(out, "Case #%d: %d\n", tcnt, n);
		}
	}

	fclose(out);

	return 0;
}