#include<stdio.h>
#include<algorithm>
#include<stdlib.h>
#include<memory.h>
using namespace std;
int c = 1;
FILE *fp;
FILE *fp2;
void test_case()
{
	int n;
	bool check[10];
	memset(check, false, sizeof(check));
	fscanf(fp, "%d", &n);
	//printf("%d\n", n);
	long long save;
	long long gop = 1;
	fprintf(fp2,"Case #%d: ", c++);
	if (n == 0)
	{
		fprintf(fp2,"INSOMNIA\n");
		return;
	}
	while (1)
	{
		bool ans_ok = true;
		save = n*gop;
		while (save > 0)
		{
			check[save % 10] = true;
			save /= 10;
		}
		for (int i = 0; i <= 9; i++)
		{
			if (!check[i])
				ans_ok = false;
		}
		if (ans_ok)
			break;
		gop++;
	}
	fprintf(fp2,"%lld\n", n*gop);
}
int main()
{
	int t;
	fp = fopen("A-large.in", "r");
	fp2 = fopen("output2.out", "w");
	fscanf(fp,"%d", &t);
	while (t--)
		test_case();
	fclose(fp);
	fclose(fp2);
	return 0;
}