#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <string>

using namespace std;

int main(){
	FILE *ifp, *ofp;
	ifp = fopen("A-large.in", "r");
	ofp = fopen("output.txt", "w");

	int t;
	fscanf(ifp, "%d\n", &t);

	for(int i=1;i<=t;i++){
		string str;
		char tmp[1111] = { 0 };
		fgets(tmp, 1111, ifp);

		str = tmp;

		string ans = str.substr(0, 1);

		for (int j = 1; j < str.size(); j++){
			if (str[j] == '\n'){
				continue;
			}
			if (str[j] >= ans[0]){
				ans = str[j] + ans;
			}
			else{
				ans = ans + str[j];
			}
		}

		for (int j = 0; j < ans.size(); j++){
			tmp[j] = ans[j];
		}
		tmp[ans.size()] = '\n';

		fprintf(ofp, "Case #%d: %s", i, tmp);
	}
	return 0;
}