#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>


using namespace std;
int check(int * nums, int size)
{
	int flag = 1;
	for (int i = 0; i < size; i++)
	{
		if (nums[i] == 0) return 0;
	}
	return flag;
}
void fill(int x, int * nums, int size)
{
	while (x > 0)
	{
		int i = x % 10;
		nums[i] = 1;
		x = x / 10;
	}

}
int main()
{
	FILE * infp = fopen("input.txt", "r");
	FILE * outfp = fopen("output.txt", "w");
	int T, n;
	int nums[10];

	int i, j;
	int k;
	fscanf(infp, "%d", &T);

	for (k = 0; k < T; k++)
	{
		memset(nums, 0, sizeof(nums));
		fscanf(infp, "%d", &n);
		unsigned long long x = n;
		
		fprintf(outfp, "Case #%d: ", k+1);
		if (x > 0)
		{
			while (1)
			{
				fill(x, nums, 10);
				if (check(nums, 10)) break;
				else
					x += n;
			}
			fprintf(outfp, "%d\n", x);
		}
		else
			fprintf(outfp, "INSOMNIA\n");
	}
	return 0;
}
