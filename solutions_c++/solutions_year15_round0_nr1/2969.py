#pragma warning(disable :4996)
#include<stdio.h>
#include<string.h>
using namespace std;
int main(){
	int t, n, ans,sum;
	char s[1010];
	FILE *f = fopen("A-large.in", "r");
	FILE *fo = fopen("out.txt", "w+");
	fscanf(f, "%d", &t);
	for (int i = 1; i <= t; i++)
	{
		sum = 0;
		ans = 0;
		fscanf(f, "%d", &n);
		fscanf(f, "%s", s);
		for (int k = 0; k <= n; k++)
		{
			if ((s[k] - 48) == 0)
			{
			}
			else if (sum >= k)
			{
				sum += (s[k] - 48);
			}
			else{
				ans += k - sum;
				sum += k - sum;
				sum += (s[k] - 48);
			}
		}
		fprintf(fo, "Case #%d: %d\n",i, ans);
	}
	return 0;
}