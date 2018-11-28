#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
#define maxn 202

FILE *fp, *fp2;
int K, C, S;
/* 
void check(int numOfBit, vector<int> bits, int cb)
{
	if(numOfBit==0)
	{
		for(int i=0;i<bits.size();i++)
		{
			for(int j=1;j<K;j++)
			{
				
			}
		}
	}
	if(cb==K)
		return;
	bits.push_back(cb);
	check(numOfBit-1, bits, cb+1);
	bits.pop_back();
	check(numOfBit, bits, cb+1);
} 
*/

int main()
{
	fp = fopen("D-small-attempt0.in", "r");
	fp2 = fopen("Doutput.txt", "w");
	int test_case;
	fscanf(fp, "%d", &test_case);
	for(int i=1;i<=test_case; i++)
	{
		fprintf(fp2, "Case #%d:", i);
		fscanf(fp, "%d %d %d", &K, &C, &S);
		for(int j=1;j<=S;j++)
			fprintf(fp2, " %d", j);
		fprintf(fp2, "\n");
	}
	
	fclose(fp);
	fclose(fp2);
	return 0;
}
