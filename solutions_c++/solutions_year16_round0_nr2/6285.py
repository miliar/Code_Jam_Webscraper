#pragma warning(disable :4996)
#include<stdio.h>
#include<string.h>
using namespace std;

int main(){
	int t, n,ans;
	char c[102];
	FILE *f = fopen("B-large.in", "r");
	FILE *fo = fopen("out.txt", "w+");
	fscanf(f, "%d", &t);
	for (int i = 1; i <= t; i++)
	{
		ans = 0;
		fscanf(f, "%s", c);
		int n = strlen(c);
		for (int i = 0; i < n-1; i++)
		{
			if (c[i] != c[i + 1])
				ans++;
		}
		if (c[n - 1] == '-')
			ans++;

		fprintf(fo, "Case #%d: %d\n", i, ans);

	}
	return 0;
}