#include <iostream>

FILE *f = fopen("input.in", "r");
FILE *g = fopen("output.out", "w");

const int L = 1000200;

int T, n, K;
char *sir, *final;

unsigned long long rez = 0;

bool isConson(char x)
{
	if (x == 'a') return false;
	if (x == 'e') return false;
	if (x == 'i') return false;
	if (x == 'o') return false;
	if (x == 'u') return false;

	return true;
}

int main()
{
	fscanf(f, "%d\n", &T);

	sir = new char[L];
	final = new char[L];
	for (int t = 0; t < T; ++t)
	{
		fgets(sir, L, f);
		int i = 0;
		while (sir[i] >= 'a' && sir[i] <= 'z')
		{
			final[i] = sir[i];
			i++;
		}
		final[i] = '\0';
		K = i;

		i++; // space
		n = 0;
		while (sir[i] >= '0' && sir[i] <= '9')
		{
			n = n * 10 + (sir[i] - '0');
			i++;
		}

		rez = 0;
		int prevPos = -1;
		for (int i = 0; i < K - n + 1; ++i)
		{
			// poz i
			bool sirOK = true;
			for (int j = i; j < i + n; ++j)
			{
				if (!isConson(final[j]))
				{
					sirOK = false;
					j = n + 1 + i;
				}
			}
			if (sirOK)
			{
				rez ++; //sirul in sine
				int a = 0; // cate litere sunt inainte
				int b = 0; // cate litere sunt dupa
				if (prevPos == -1)
				{
					a = i;
				}
				else
				{
					a = i - prevPos - 1;
				}
				prevPos = i;
				b = K - (i + n);
				rez = rez + a + b + (a * b);
			}
		}

		fprintf(g, "Case #%d: %llu\n", t + 1, rez); 
	}

	fclose(f);
	fclose(g);

	return 0;
}