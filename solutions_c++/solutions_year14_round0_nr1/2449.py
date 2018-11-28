#include<iostream>

using namespace std;

int main()
{
	int n,f,s;
	int map[4][4],first[4],second[4];
	int i,j;
	FILE *fp1,*fp2;

	fp1 = fopen("A-small-attempt1.in","r");
	fp2 = fopen("A-small-attempt1.out","w+");

	fscanf(fp1,"%d",&n);

	for(int k=1; k<=n; k++)
	{
		fscanf(fp1,"%d",&f);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{
				fscanf(fp1,"%d",&map[i][j]);
				if(i == f-1)
					first[j]=map[i][j];
			}

		fscanf(fp1,"%d",&s);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{
				fscanf(fp1,"%d",&map[i][j]);
				if(i == s-1)
					second[j]=map[i][j];
			}
		int t,count=0;

		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				if(first[i] == second[j])
				{
					count++;
					t=first[i];
				}
		
		if(count == 1)
			fprintf(fp2,"Case #%d: %d\n",k,t);
		else if(count == 0)
			fprintf(fp2,"Case #%d: Volunteer cheated!\n",k);
		else
			fprintf(fp2,"Case #%d: Bad magician!\n",k);
	}


	return 0;
}