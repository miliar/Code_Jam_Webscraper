#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

void inputf(FILE *in, FILE *out);
void process(FILE *in, FILE *out, int n1, int n2, int input1[4][4], int input2[4][4]);

int main(void)
{
	FILE *in=fopen("input.in", "r");
	FILE *out=fopen("output.out","w");

	int testcase;
	fscanf(in, "%d", &testcase);

	for(int i=0;i<testcase;i++)
	{
		fprintf(out,"Case #%d: ",i+1);
		inputf(in,out);
	}

	fclose(out);
	fclose(in);

	return 0;
}

void inputf(FILE *in, FILE *out)
{
	int n1, input1[4][4];
	fscanf(in, "%d", &n1);
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			fscanf(in, "%d", &input1[i][j]);

	int n2, input2[4][4];
	fscanf(in, "%d", &n2);
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			fscanf(in, "%d", &input2[i][j]);

	process(in,out,n1,n2,input1,input2);

	return;
}

void process(FILE *in, FILE *out, int n1, int n2, int input1[4][4], int input2[4][4])
{
	int count=0;
	int number=0;

	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(input1[n1-1][i]==input2[n2-1][j])
			{
				number=input1[n1-1][i];
				count++;
			}
	
	if(count==0)
		fprintf(out, "Volunteer cheated!\n");
	else if(count==1)
		fprintf(out, "%d\n", number);
	else
		fprintf(out, "Bad magician!\n");

	return;
}
