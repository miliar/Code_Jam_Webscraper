#pragma warning(disable:4996)

#include <conio.h>
#include <stdio.h>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main(int argc, const char *argv[])
{
	int test_case_totalnum, now_case_num = 0;
	FILE *hFile;

	vector<int> cur, tmpvec, curL;
	vector<int> req, reqL, reqLr;

	int A, B, K;
	int i, j;
	int tmp;
	int count = 0;

	hFile = fopen(argv[1], "r");
	fscanf(hFile, "%d", &test_case_totalnum);

	while (now_case_num++ < test_case_totalnum)
	{
		printf("Case #%d: ", now_case_num);
		fscanf(hFile, "%d", &A);
		fscanf(hFile, "%d", &B);
		fscanf(hFile, "%d", &K);

		count = 0;

		for (i = 0; i < A; i++)
		for (j = 0; j < B; j++)
		{
			if ((i&j) < K)
			{
				count++;
			}
		}

		printf("%d\n", count);



	}
	return 0;
}