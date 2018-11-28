#include <iostream>

bool CheckFillavail(int x, int c, int r)
{
	if (x == 1) return true;
	if (((x+1) / 2) > r || ((x+1) / 2) > c) return false;
	if ((r*c) % x != 0) return false;

	switch (x){
	case 2:
		if (r % 2 == 0 || c % 2 == 0) return true;
		break;
	case 3:
		if (r%3==0||c%3==0) return true;
		break;
	case 4:
		if ((r==4&&c>2)||(c==4&&r>2)) return true;
	}
	return false;
}
void main()
{
	FILE *fs = fopen("input.txt", "r");
	FILE *fp = fopen("output.txt", "w");

	int testcase;
	fscanf(fs, "%d", &testcase);

	for (int t = 0; t < testcase; t++)
	{
		int x, r, c;

		fscanf(fs, "%d %d %d", &x, &r, &c);
		if (CheckFillavail(x, r, c) == true)
			fprintf(fp, "Case #%d: GABRIEL\n", t + 1);
		else
			fprintf(fp, "Case #%d: RICHARD\n", t + 1);
	}
	fclose(fs);
	fclose(fp);
}