#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <string>

using namespace std;

int main(){
	FILE *ifp, *ofp;
	ifp = fopen("B-large.in", "r");
	ofp = fopen("output.txt", "w");

	int t;
	fscanf(ifp, "%d\n", &t);

	for(int i=1;i<=t;i++){
		char str[111] = {0};
		fgets(str, sizeof(str), ifp);

		int position = 0;
		int ans = 0;
		int size = 0;
		while (str[size] != '\0' && str[size]!='\n'){
			size++;
		}

		if (str[0] == '-'){
			ans--;
		}

		for (int j = 1; j < size; j++){
			if (str[j - 1] == '-' && str[j] == '+'){
				ans += 2;
			}
		}
		if (str[size - 1] == '-'){
			ans += 2;
		}

		fprintf(ofp, "Case #%d: %d\n", i, ans);
	}
	return 0;
}