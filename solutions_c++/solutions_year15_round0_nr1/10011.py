#include <stdio.h>

int main()
{
	FILE* fin = fopen("A-small-attempt0.in", "r");
	FILE* fout = fopen("out.txt", "w");

	int n;
	fscanf(fin, "%d", &n);
	int arr[1000];

	for (int i = 0; i < n; i++)
	{
		for (int a = 0; a < 1000; a++)
			arr[a] = 0;
		int size;
		fscanf(fin, "%d", &size);
		int num, currentstand, add = 0;
		fscanf(fin, "%d", &num);
		for (int j = size; j >= 0; j--)
		{
			arr[j] = num % 10;
			num /= 10;
		}
		currentstand = arr[0];
		for (int k = 1; k < size + 1; k++)
		{
			if (arr[k] == 0)
				continue;
			if (currentstand < k)
			{
				add += k - currentstand;
				currentstand = k + arr[k];
				continue;
			}
			if (currentstand >= k)
			{
				currentstand += arr[k];
				continue;
			}
		}
		fprintf(fout, "Case #%d: %d\n", i+1, add);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}