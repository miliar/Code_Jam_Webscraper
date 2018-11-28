#include <stdio.h>
#include <stdlib.h>

int min(int a, int b){
	if (a > b)
		return b;
	else
		return a;

}
int mint(int d[3001],int n){
	int max = 0,tmp;
	for (int i = 0; i < n; i++)
	{
		if (max < d[i]){
			max = d[i];
			tmp = i;
		}
	}
	if (max < 4)
		return max;
	int dd[3001] = { 0, };
	int ddd[3001] = { 0, };

	for (int i = 0; i < n; i++){
		dd[i] = d[i] - 1;
		ddd[i] = d[i];
	}
	if (max != 9){
		ddd[n] = max / 2;
		ddd[tmp] = max / 2 + max % 2;
	}
	else{
		ddd[n] = 6;
		ddd[tmp] = 3;
	}
	return min(mint(dd, n), mint(ddd, n + 1))+1;
}
int main(){
	FILE *fi = fopen("B-small-attempt3.in", "r");
	FILE *fo = fopen("output.txt", "w");
	int T;

	fscanf(fi,"%d", &T);

	for (int t = 1; t <= T; t++){
		int time = 0;
		int d[3001] = { 0, };
		int ch[3001] = { 0, };
		int num;
		int tmp, max = 0;
		fscanf(fi,"%d", &num);
		for (int i= 0; i < num; i++)
			fscanf(fi,"%d", &d[i]);
		
		fprintf(fo,"Case #%d: %d\n", t, mint(d,num));
	}
	return 0;
}