#include<stdio.h>


const int n=4;


int cases;

int first[n+1][n+1];
int second[n+1][n+1];

int f_line;
int s_line;

int result[101];
int r_count=1;

int card_n[101];



int input();
int process();
int output();


int main()
{

	input();
	output();



	return 0;

}


int input()
{

	int i, j, k;

	FILE *fi;

	fi=fopen("input.txt", "rt");

	fscanf(fi, "%d", &cases);

	for(i=1; i<=cases; i++)
	{
	
		fscanf(fi, "%d", &f_line);
		for(j=1; j<=n; j++)
		{
			for(k=1; k<=n; k++)
				fscanf(fi, "%d", &first[j][k]);
		}

		fscanf(fi, "%d", &s_line);
		for(j=1; j<=n; j++)
		{
			for(k=1; k<=n; k++)
				fscanf(fi, "%d", &second[j][k]);
		}


		process();

	}


	return 0;
	

}

int process()
{
	int i, j;

	bool check[n*n+1];

	int count;

	count=0;

	for(i=1; i<=n*n; i++)
		check[i]=false;

	for(i=1; i<=n; i++)
		check[first[f_line][i]]=true;

	for(i=1; i<=n; i++)
	{
		if(check[second[s_line][i]]==true)
			result[r_count]++;
	}

	if(result[r_count]==1)
	{
		for(i=1; i<=n; i++)
		{
			for(j=1; j<=n; j++)
			{
				if(first[f_line][i]==second[s_line][j])
				{
					card_n[r_count]=first[f_line][i];
					break;
				}
			}
			if(card_n[r_count])
				break;
		}
	}

	r_count++;


	return 0;
	
}


int output()
{

	int i;

	FILE *fo;

	fo=fopen("output.txt", "wt");

	for(i=1; i<=cases; i++)
	{
		if(result[i]==0)
			fprintf(fo, "Case #%d: Volunteer cheated!\n", i);
		else if(result[i]==1)
			fprintf(fo, "Case #%d: %d\n", i, card_n[i]);
		else
			fprintf(fo, "Case #%d: Bad magician!\n", i);

	}

	return 0;

}

/*

3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

*/
