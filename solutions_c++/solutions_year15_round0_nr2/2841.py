#pragma warning(disable :4996)
#include<stdio.h>
#include<queue>
#include<algorithm>
using namespace std;
queue<int> q;

int t, n, ans, sum, mi, loca,num;
int  p[1010];
int dp[1010];
int main(){
	
	FILE *f = fopen("B-large.in", "r");
	FILE *fo = fopen("out.txt", "w+");
	fscanf(f, "%d", &t);
	for (int i = 1; i <= t; i++)
	{
		fscanf(f, "%d", &n);
		for (int j = 1; j <= n; j++)
			fscanf(f, "%d", &p[j]);
		for (int j = 1; j <= 1000; j++)
		{
			for (int k = 1; k <= n; k++)
			{
				dp[j] += (p[k] - 1)/j;
			}
			dp[j] += j;
		}
		mi = 9999;
		for (int k = 1; k <= 1000; k++)
		{
			if (dp[k] < mi)
			{
				mi = dp[k];
			}
		}
		fprintf(fo, "Case #%d: %d\n", i, mi);
		for (int  a= 1; a <= 1000; a++)
		{
			dp[a] = 0;
		}
	}
	return 0;
}