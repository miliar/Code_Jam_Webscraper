#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <string>

using namespace std;

int main(){
	FILE *ifp, *ofp;
	ifp = fopen("B-small-attempt0.in", "r");
	ofp = fopen("output.txt", "w");

	int t;
	fscanf(ifp, "%d\n", &t);

	for(int i=1;i<=t;i++){
		int n;
		fscanf(ifp, "%d", &n);
		char tmp[55] = {0};
		int arr[2555] = { 0 };

		for (int j = 0; j < 2*n-1; j++){
			fgets(tmp, 55, ifp);
			if (tmp[0] == '\n'){
				j--;
				continue;
			}

			int count = 0;
			int position = 0;

			while (count != n){
				int tmp1 = 0;
				for (int k = position; k < 55; k++){
					if (tmp[k] != ' ' && tmp[k]!='\n' && tmp[k]!=NULL){
						tmp1 *= 10;
						tmp1 += tmp[k] - '0';
					}
					else{
						position = k+1;
						break;
					}
				}
				arr[tmp1]++;
				count++;
			}
		}

		fprintf(ofp, "Case #%d:", i);
		for (int j = 0; j < 2555; j++){
			if (arr[j] % 2 == 1){
				fprintf(ofp, " %d", j);
			}
		}
		fprintf(ofp, "\n");
	}
	return 0;
}