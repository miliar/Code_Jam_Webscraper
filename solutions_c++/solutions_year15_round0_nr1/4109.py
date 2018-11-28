#include <iostream>
#include <cstdio>
using namespace std;

int test;
int n;
int need, sum;
char shy[1001];
int cnt = 1;
int main(){
	FILE *fi = fopen("A-large.in", "r");
	FILE *fo = fopen("output.out", "w");

	fscanf(fi, "%d", &test);

	while (test--)
	{
		need = 0, sum = 0;
		fscanf(fi, "%d", &n);
		fscanf(fi, "%s", shy);

		for (int i = 1; i <= n; i++)
		{
			sum += shy[i - 1] - '0';
			if (sum >= i) continue;
			if (shy[i] == '0') continue;

			int tmp = i - sum;
			need += tmp;
			sum += tmp;
		}
		fprintf(fo, "Case #%d: %d\n", cnt++, need);
	}

}