#include <cstdio>

using namespace std;

const long long g_fairNum[39] = {
1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};

int main()
{
	char inFile[30], outFile[30], tmp1[1000], tmp2[1000];
	FILE *fin, *fout;
	int testNum, from, to;
	long long start, end;
	scanf("%s", inFile);
	scanf("%s", outFile);
	fin = fopen(inFile, "r");
	fout = fopen(outFile,"w");
	fscanf(fin, "%d", &testNum);
	for (int i = 1; i <= testNum; i++)
	{
		fscanf(fin, "%lld %lld", &start, &end);
		for (int j = 0; j < 39; j++)
		{
			if (g_fairNum[j] >= start)
			{
				from = j;
				break;
			}
		}
		for (int j = 38; j >= 0; j--)
		{
			if (g_fairNum[j] <= end)
			{
				to = j;
				break;
			}
		}
		fprintf(fout, "Case #%d: %d\n", i, to-from+1);
	}

	fclose(fin);
	fclose(fout);
}
	
