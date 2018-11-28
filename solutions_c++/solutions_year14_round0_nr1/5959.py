#include <cstdio>

int T, ans1, ans2, cards1[4][4], cards2[4][4];

int main()
{
	FILE *fp;
	FILE *fout;
	fp=fopen("boda", "r");
	fout=fopen("boda2", "w");
	fscanf(fp, "%d", &T);
	for(int i=0; i<T; i++)
	{
		fscanf(fp, "%d", &ans1);
		ans1--;
		for(int j=0; j<4; j++)
			for(int k=0; k<4; k++)
				fscanf(fp, "%d", &cards1[j][k]);
		fscanf(fp, "%d", &ans2);
		ans2--;
		for(int j=0; j<4; j++)
			for(int k=0; k<4; k++)
				fscanf(fp, "%d", &cards2[j][k]);
		
		int a=0;
		for(int j=0; j<4; j++)
		{
			for(int k=0; k<4; k++)
			{
				if(cards2[ans2][k]==cards1[ans1][j])
				{
					if(a==0) //no common card yet
						a=cards2[ans2][k];
					else //common card already found
					{
						a=17;
						break;
					}
				}
			}
		}
		fprintf(fout, "Case #%d: ", i+1);
		if(a==0)
			fprintf(fout, "Volunteer cheated!\n");
		else if(a>16)
			fprintf(fout, "Bad magician!\n");
		else
			fprintf(fout, "%d\n", a);
	}
	fclose(fp);
	return 0;
}
