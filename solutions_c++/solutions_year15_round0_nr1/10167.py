#include<stdio.h>
#include<iostream>
#include<vector>

using namespace std;

int T, inputi;
char inputc[1001];

int main(int argc, char* argv[]){
	FILE* f = fopen(argv[1], "r");
	FILE* out = fopen("out.txt", "w+");
	fscanf(f, "%d", &T);
	for (int k = 0; k < T; k++){
		fscanf(f, "%d", &inputi);
		int res = 0;
		fscanf(f, "%s", inputc);
		for (int i = 0; i < inputi; i++) inputc[i] -= '0';
		for (int i = 1; i <= inputi; i++){
			if (i <= inputc[i - 1]){
				inputc[i] += inputc[i - 1];
			}
			else{
				res += i - inputc[i - 1];
				inputc[i] += i;
			}
		}
		printf("Case #%d: %d\n", k + 1, res);
	}
	return 0;
}