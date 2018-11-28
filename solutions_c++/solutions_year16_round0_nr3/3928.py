#include<stdio.h>
#include<math.h>
int main()
{
	FILE *fp, *ofp;
	int t, i, j,m;
	int w = 0,w1=0, cun=0;
	char box[17];
	long long num[11], sum = 0,bin;
	fp = fopen("in.txt", "r");
	ofp = fopen("out.txt", "w");
	for (i = 0; i < 17; i++)
		box[i] = '0';
	box[0] = '1';
	fscanf(fp,"%d", &t);
	fscanf(fp, "%d %d", &i, &m);
	box[i - 1] = '1';
	fprintf(ofp, "Case #%d:\n", t);
		while (box[i-1] == '1')
		{
			//°è»ê.
			w1 = 0;
			for (long long k = 2; k <= 10; k++)
			{
				bin = 1;
				sum = 0;
				for (j = 0; j < i; j++)
				{
					if (box[j] == '1')
						sum += bin;
					bin *= k;
				}
				w = 0;
				for (int h = 2; h <= sqrt(sum); h++)
				{
					if (sum%h == 0)
					{
						num[k] = h;
						w = 1;
						w1++;
						break;
					}
				}
				if (w == 0)
					break;			
			}
			if (w1 == 9)
			{
				cun++;
				for (j = i - 1; j >= 0; j--)
					fprintf(ofp,"%c", box[j]);
				for (j = 2; j <= 10; j++)
					fprintf(ofp," %lld", num[j]);
				fprintf(ofp,"\n");
				if (cun >= m)
				{
					fclose(fp);
					fclose(ofp);
					return 0;
				}
			}
			j = 1;
			w = 1;
			while (w)
			{
				if (box[j] == '1')
				{
					w = 1;
					box[j++] = '0';
				}
				else
				{
					w = 0;
					box[j] = '1';
				}
			}
		}
}