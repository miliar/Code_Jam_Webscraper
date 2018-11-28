#include<stdio.h>

int main(void)
{
	FILE *fp, *outfp;
	int T,num=0,k=0, temp = 0, i = 0, sum, box[10] = {0,},a;
	fp = fopen("in.txt", "r");
	outfp = fopen("out.txt", "w");
	fscanf(fp,"%d", &T);
	while (i < T)
	{
		i++;
		fscanf(fp, "%d", &num);
		if (num == 0)
		{
			fprintf(outfp, "Case #%d: INSOMNIA\n",i);
			continue;
		}
		k = 0;
		sum = 0;
		while (sum != 45 || box[0] == 0)
		{
			k++;
			temp = num*k;
			while (temp != 0)
			{
				a = temp % 10;
				temp /= 10;
				if (box[a] == 0)
				{
					sum += a;
					box[a] = 1;
				}
			}
		}
		fprintf(outfp, "Case #%d: ",i);
		fprintf(outfp, "%d\n", num*k);
		for (k = 0; k < 10; k++)
			box[k] = 0;
	}
	fclose(fp);
	fclose(outfp);
	return 0;
}

