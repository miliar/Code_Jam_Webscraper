#pragma warning(disable:4996)

#include <stdio.h>
#include <set>

using namespace std;

int main(int argc, const char *argv[])
{
	int test_case_totalnum, now_case_num = 0;
	int row, i;
	int val;
	set<int> testset;
	char tmpstr[999];
	int count = 0;
	int answer = 0;
	FILE *hFile;

	hFile = fopen(argv[1], "r");
	fscanf(hFile,"%d", &test_case_totalnum);
	while (now_case_num++ < test_case_totalnum)
	{
		printf("Case #%d: ", now_case_num);
		testset.clear();
		count = 0;

		fscanf(hFile,"%d", &row);

		for (i = 1; i <= 4; i++)
		{
			if (row == i)
			{
				fscanf(hFile,"%d", &val);	testset.insert(val);
				fscanf(hFile,"%d", &val);	testset.insert(val);
				fscanf(hFile,"%d", &val);	testset.insert(val);
				fscanf(hFile,"%d", &val);	testset.insert(val);
			}
			else
			{
				fscanf(hFile,"%d", &val);
				fscanf(hFile,"%d", &val);
				fscanf(hFile,"%d", &val);
				fscanf(hFile,"%d", &val);
			}
		}
		
		fscanf(hFile,"%d", &row);

		for (i = 1; i <=4; i++)
		{
			if (row == i)
			{
				fscanf(hFile,"%d", &val);	testset.insert(val).second || (count++, answer = val);
				fscanf(hFile,"%d", &val);	testset.insert(val).second || (count++, answer = val);
				fscanf(hFile,"%d", &val);	testset.insert(val).second || (count++, answer = val);
				fscanf(hFile,"%d", &val);	testset.insert(val).second || (count++, answer = val);
			}
			else
			{
				fscanf(hFile,"%d", &val);
				fscanf(hFile,"%d", &val);
				fscanf(hFile,"%d", &val);
				fscanf(hFile,"%d", &val);
			}

		}
		if (count == 0)
		{
			puts("Volunteer cheated!");
		}
		else if (count == 1)
		{
			printf("%d\n", answer);
		}
		else
		{
			puts("Bad magician!");
		}
	}

	return 0;
}