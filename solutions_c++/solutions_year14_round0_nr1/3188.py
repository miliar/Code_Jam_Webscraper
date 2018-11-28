#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
int time;
int count,answer;
int flag[17];
FILE *in, *out;
int read()
{
	int row,num;
	fscanf(in,"%d",&row);
	row -= 1;
	int i;
	for (i = 0; i <= 15; i++)
	{
		fscanf(in,"%d", &num);
		if (i / 4 == row)
			flag[num]++;
	}
	return 0;
}
int solve()
{
	int i;
	count = 0;
	for (i = 1; i <= 16; i++)
	if (flag[i] == 2)
	{
		answer = i;
		count++;
	}
	return 0;
}
int print(int x)
{
	fprintf(out,"Case #%d: ",x);
	if (count == 1)
		fprintf(out,"%d\n", answer);
	else if (count > 1)
		fprintf(out,"Bad magician!\n");
	else if (count == 0)
		fprintf(out,"Volunteer cheated!\n");
	return 0;
}
int main()
{
	in = fopen("A-small-attempt2.in","r");
	out = fopen("result.txt","w");
	fscanf(in,"%d",&time);
	int i;
	for (i = 1; i <= time; i++)
	{
		memset(flag,0,sizeof(flag));
		read();
		read();
		solve();
		print(i);
	}
	return 0;
}