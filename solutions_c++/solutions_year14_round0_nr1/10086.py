#include "iostream"
#include "stdio.h"

void solve(FILE* fi, FILE* fo, int num)
{
	int a1, a2;
	int* n1;
	int* n2;

	n1 = new int[16];
	n2 = new int[16];

	fscanf(fi, "%d", &a1);
	for(int i = 0; i<16; i++)
		fscanf(fi, "%d", &n1[i]);
	
	fscanf(fi, "%d", &a2);
	for(int i = 0; i<16; i++)
		fscanf(fi, "%d", &n2[i]);

	int* res = new int[4];
	int k = 0;
	for(int i = (a1-1)*4; i < a1*4; i++)
	{
		for(int j = (a2-1)*4; j < a2*4; j++)
		{
			if (n1[i] == n2[j])
			{
				res[k++] = n1[i];
			}
		}
	}
	if (k==1) 
	{
		fprintf(fo, "Case #%d: %d\n", num, res[0]);
	}
	else if(k==0)
	{
		fprintf(fo, "Case #%d: Volunteer cheated!\n", num);
	}
	else
	{		
		fprintf(fo, "Case #%d: Bad magician!\n", num);
	}
	
	delete res;
	delete n1;
	delete n2;
}

int main()
{
	int t;
	FILE* fi = fopen("input.txt", "r");
	fscanf(fi, "%d", &t);
	FILE* fo = fopen("output.txt", "w");

	for(int i = 0; i < t; i++)
	{
		solve(fi, fo, i+1);
	}
	fclose(fi);
	fclose(fo);
	
	return 0;
}