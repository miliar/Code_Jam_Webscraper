#include<stdio.h>

int main(void)
{
	FILE *fp, *ofp;
	char box[101],tmp;
	int t, i, j, ans , len;
	fp = fopen("in.txt", "r");
	ofp = fopen("out.txt", "w");
	fscanf(fp,"%d", &t);
	i = 0;
	while (i < t)
	{
		i++;
		ans = 0;
		len = 0;
		fscanf(fp,"%s", &box);
		for (j = 0; box[j] != 0; j++);
		len = j;
		tmp = '+';
		for (j = len - 1; j >= 0; j--)
		{
			if (tmp != box[j])
			{
				ans++;
				if (tmp == '+')
					tmp ='-';
				else
					tmp = '+';
			}
		}
		fprintf(ofp, "Case #%d: ", i);
		fprintf(ofp, "%d\n", ans);
	}
	fclose(fp);
	fclose(ofp);
}