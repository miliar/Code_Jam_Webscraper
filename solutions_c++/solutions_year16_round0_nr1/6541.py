#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <string>

using namespace std;

long long int func(int n){
	long long int tmp = n;
	int arr[11] = { 0 };
	int count = 0;

	while (1){
		long long int test = tmp;

		while (1){
			int ones = test % 10;
			if (arr[ones] == 0){
				arr[ones] = 1;
				count++;
			}
			test = test / 10;
			if (test == 0){
				break;
			}
		}
		if (count >= 10){
			break;
		}
		tmp += n;
	}
	return tmp;
}

int main(){
	FILE *ifp,*ofp;
	ifp = fopen("A-large.in", "r");
	ofp = fopen("output.txt", "w");
	int t;
	fscanf(ifp, "%d", &t);

	for(int i=1;i<=t;i++){
		int n;
		fscanf(ifp, "%d", &n);

		if (n == 0){
			fprintf(ofp, "Case #%d: INSOMNIA\n", i);
			continue;
		}

		long long int ans = func(n);

		fprintf(ofp, "Case #%d: %d\n", i, ans);
	}
	return 0;
}