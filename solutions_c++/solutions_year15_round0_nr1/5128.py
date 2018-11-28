#include<iostream>
#include<stdio.h>
using namespace std;
char str[1100];
int T, Smax;
int main(){
	FILE *fp1 = fopen("A-large.in", "r");
	FILE *fp2 = fopen("output2.txt", "w");

	fscanf(fp1, "%d", &T);
	for (int t = 0; t < T; t++){
		int pchk = 0, pplus = 0;
		fscanf(fp1, "%d %s", &Smax, str);
		for (int i = 0; i <= Smax; i++){
			if (pplus + pchk < i){
				pplus += i - pchk - pplus;
				pchk += str[i] - '0';
			}
			else{
				pchk += str[i] - '0';
			}
		}
		fprintf(fp2,"Case #%d: %d\n", t+1, pplus);
	}
	fclose(fp1);
	fclose(fp2);
}