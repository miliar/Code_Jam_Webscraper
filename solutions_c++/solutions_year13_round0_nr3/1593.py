#include<iostream>
#include<stdio.h>
#include<string>
using namespace std;

long long int ans[50] = {0,}, cnt = 0;
int test, k;
long long int a, b, n, i, j, res;
char p[20] = {0,};
FILE *fo = fopen("output.txt","w");

bool isPalin(long long int s)
{
	if(s < 10) return true;
	k = 0;
	while(s > 0) {
		p[k++] = (s % 10) + '0';
		s /= 10;
	}
	for(j = 0; j < k/2; j++) {
		if(p[j] != p[k-1-j]) return false;
	}
	return true;
}

int main()
{
	FILE *fp = fopen("C-large-1.in", "r");
	fscanf(fp, "%d", &test);

	a = 1;
	b = 100000000000000;
	for(i = a; i*i <= b; i++) {
		n = i * i;
		if(isPalin(n) && isPalin(i)) {
			ans[cnt++] = n;
			//printf("%lld %lld\n", i, n);
		}
	}
	//printf("%d\n", cnt);

	for(int t = 1; t <= test; t++) {
		res = 0;
		fscanf(fp, "%lld %lld", &a, &b);

		for(int k = 0; k < cnt; k++) {
			if(a <= ans[k] && ans[k] <= b) res++;
		}

		fprintf(fo, "Case #%d: %d\n", t, res);
	}

	fclose(fp);
	fclose(fo);
	return 0;
}