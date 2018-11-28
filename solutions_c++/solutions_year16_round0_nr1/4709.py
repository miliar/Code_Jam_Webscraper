#include <stdio.h>
#include <stdlib.h>

bool chk[10];
int remain;

void func(int num)
{
	int a;
	
	if(num == 0) return;

	a = num%10;
	if(!chk[a])
	{
		chk[a] = 1;
		remain--;
	}
	func((int)(num/10));
}

int solve(int num)
{
	int i, prod;

	if(num == 0) return 0;

	for(i=0; i<10; i++) chk[i] = 0;
	remain = 10;

	for(i=1; i<=100000; i++)
	{
		prod = num*i;
		func(prod);
		if(remain == 0) return prod;
	}
	
	return 0;
}


int main()
{
	int i, totalCaseNum, data[100], tmpInt;

	FILE *fid = fopen("A-large.in", "r");

	fscanf(fid, "%d", &totalCaseNum);
	for(i=0; i<totalCaseNum; i++) fscanf(fid, "%d", &data[i]);
	fclose(fid);

	fid = fopen("B-output-large.out", "w");
	for(i=0; i<totalCaseNum; i++)
	{
		tmpInt = solve(data[i]);
		if(tmpInt == 0) fprintf(fid, "Case #%d: INSOMNIA\n", i+1);
		else fprintf(fid, "Case #%d: %d\n", i+1, tmpInt);
	}
	fclose(fid);

	return 0;
}