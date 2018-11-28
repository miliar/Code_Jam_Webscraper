#include<stdio.h>
#include<string.h>

#pragma warning(disable:4996)
int cnt[2000];
int main()
{
	FILE *fi = fopen("input.txt", "r");
	FILE *fo = fopen("output.txt", "w");
	char input[2000];
	int l, i,t,p,sum,result;

	fscanf(fi,"%d", &t);

	for (p=1; p<=t; p++){
		fscanf(fi,"%d %s", &l, input);
		l = strlen(input);
		sum = result = 0;
		for (i = 0; i < l; i++){
			cnt[i] = 0;
			cnt[i] = input[i] - '0';
		}
		for (i = 0; i < l; i++){
			if (cnt[i] != 0){
				if (sum >= i){
					sum += cnt[i];
				}
				else{
					result += i - sum;
					sum = i + cnt[i];
				}
			}
		}
		fprintf(fo, "Case #%d: %d\n", p, result);
	}

	return 0;
}