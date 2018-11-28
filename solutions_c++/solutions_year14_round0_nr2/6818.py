#pragma warning(disable:4996)

#include <stdio.h>
#include <conio.h>
#include <set>

using namespace std;

int main(int argc, const char *argv[])
{
	int test_case_totalnum, now_case_num = 0;
	FILE *hFile;

	double C, F, X;
	int purchase_count = 0;
	hFile = fopen(argv[1], "r");
	fscanf(hFile,"%d", &test_case_totalnum);
	
	
	while (now_case_num++ < test_case_totalnum)
	{
		printf("Case #%d: ", now_case_num);
		fscanf(hFile, "%lf", &C);
		fscanf(hFile, "%lf", &F);
		fscanf(hFile, "%lf", &X);

		purchase_count = 0;

		double T1 = 0, T2 = 0, sum = 0;
		double min = X / 2;

		while (1)
		{
			T1 += C / (2 + F*purchase_count);
			T2 = X / (2 + F*(purchase_count+1));
			sum = T1 + T2;
			purchase_count++;
			if (min < sum)
			{
				printf("%.7lf\n", min);
				break;
			}
			else
			{
				min = sum;
			}
		}
	}

	return 0;
}