#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <vector>

using namespace std;

#define INFILE fopen("A-small-attempt0.in","r");
#define OUTFILE fopen("A-small-attempt0.out","w");




int main(void){
	FILE *fp_in;
	FILE *fp_out;

	fp_in = INFILE;
	fp_out = OUTFILE;

	vector<int> PT;

	PT.push_back(1);

	for (int i = 1; i < 11; i++){
		PT.push_back(PT[i - 1] * 2);
	}

	int T;
	fscanf(fp_in, "%d", &T);



	for (int i = 0; i < T; i++){
		int P, Q;

		fscanf(fp_in,"%d/%d", &P, &Q);

		if (Q%P == 0){
			Q = Q / P;
			P = 1;
		}
		int chk = 1;
		for (int j = 0; j < PT.size(); j++){
			if (Q == PT[j]){
				chk = 0;
				break;
			}
		}
		if (chk){
			fprintf(fp_out,"Case #%d: impossible\n",i+1);
			continue;
		}

		int ans = 0;

		while (P < Q){
			P = P * 2;
			ans++;
		}

		fprintf(fp_out, "Case #%d: %d\n", i + 1, ans);
	}
}