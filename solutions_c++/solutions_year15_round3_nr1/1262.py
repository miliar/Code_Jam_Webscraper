#include <stdio.h>

FILE *fin, *fout;

int main()
{
	int t, r, c, w, ans, find;

	fin = fopen("input.txt", "r");
	fout = fopen("output.txt", "w");

	fscanf(fin, "%d", &t);
	for (int i = 0; i < t; i++)
	{
		fscanf(fin, "%d %d %d", &r, &c, &w);
		
	
		find = c / w;

		if (c / 2 >= w)
		{
			ans = ((c-1) / w) + w;
		}
		else if (c==w) 
		{
			ans = w;
		}
		else
		{
			ans = w + 1;		
		}
		ans += find*(r - 1);
		
		fprintf(fout, "Case #%d: %d\n", i+1, ans);
	}
	fclose(fin);
	fclose(fout);

	return 0;
}