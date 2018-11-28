#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

int main(){
	FILE* fi = fopen("A-large.in", "r");
	FILE* fo = fopen("output.txt", "w");
	int T;
	fscanf(fi, "%d", &T);
	for (int I = 0; I < T; I++){
		int check[10] = {0,};
		int a, b, c, ok = 0,d = 1, ans;
		fscanf(fi, "%d", &a);
		if (a == 0){
			fprintf(fo, "Case #%d: INSOMNIA\n", I +1);
			continue;
		}
		b = a;
		while (1){
			while (a > 0){
			c = a % 10;
			a /= 10;
			check[c] = 1;
			}
			for (int i = 0; i < 10; i++){
				if (check[i] == 1){
					ok = 1;
				}
				else{
					ok = 0;
					break;
				}
			}
			if (ok == 1) break;
			d++;
			a = d * b;
			ans = a;
		}
		fprintf(fo, "Case #%d: %d\n", I + 1,ans);
	}
	return 0;
}