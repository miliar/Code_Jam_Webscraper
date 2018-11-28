#include<stdio.h>
#include<map>
#include<string>
#include<vector>
#include<stdlib.h>
#include<string.h>

using namespace std;

map< string, int > Map;
char str[11111111];
char *small;

int T, N;

int A[2222][2222];
int AN[2222];
int Color[111111];

int main(void)
{
	int l1, l2, l3, flag;
	int l0;

	gets(str);
	sscanf(str, "%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		gets(str);
		sscanf(str, "%d", &N);

		Map.clear();

		for(l1 = 0; l1 < N; l1++)
		{
			AN[l1] = 0;
			gets(str);
			for(small = strtok(str, " "); small; small = strtok(NULL, " "))
			{
				if(Map.count(small) == 0)
				{
					int newidx = Map.size();
					Map[small] = newidx;
				}
				A[l1][ AN[l1]++ ] = Map[small];
			}
		}

		int words = Map.size();

		int ret = 1000000000;
		int thelast = (1 << (N-2));
		for(flag = 0; flag < thelast; flag++)
		{
			for(l1 = 0; l1 < words; l1++) Color[l1] = 0;
			for(l1 = 0; l1 < AN[0]; l1++) Color[A[0][l1]] |= 1;
			for(l1 = 0; l1 < AN[1]; l1++) Color[A[1][l1]] |= 2;
			for(l1 = 2; l1 < N; l1++)
			{
				if(flag & (1 << (l1 - 2)))
				{
					for(l2 = 0; l2 < AN[l1]; l2++) Color[A[l1][l2]] |= 1;
				}
				else
				{
					for(l2 = 0; l2 < AN[l1]; l2++) Color[A[l1][l2]] |= 2;
				}
			}
			
			int curr = 0;
			for(l1 = 0; l1 < words; l1++) if(Color[l1] == 3) curr++;
			if(curr < ret) ret = curr;
		}

		printf("Case #%d: %d\n", l0, ret);
	}
}
