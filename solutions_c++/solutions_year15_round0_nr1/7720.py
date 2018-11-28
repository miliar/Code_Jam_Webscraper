#include <iostream>
#include <stdlib.h>
#include <vector>
#include <stdio.h>

int sum = 0;

using namespace std;

int main()
{
	vector<int> result;
	int casenum;
	int d[1111];
	FILE *in = fopen("A-large.in", "r");
	FILE *out = fopen("output.txt", "w");

	fscanf(in, "%d", &casenum);
	
	for( int i=0; i<casenum; i++){
		int total = 0;
		int smax;

		fscanf(in, "%d", &smax);

		for( int j=0; j < smax+1; j++){
			fscanf(in, "%1d", &d[j]);
		}

		for( int k=0; k<smax+1; k++){
			sum = 0;

			for( int l=0; l<k; l++){
 				sum += d[l];
			}

			if( sum < k){
				d[0] += k - sum;
				total += k - sum;
			}
		}

		result.push_back(total);
	}

	for( int x=0; x<casenum; x++){
		fprintf(out, "Case #%d: %d\n", x+1, result[x]);
	}

	fclose(in);
	fclose(out);
	
	return 0;
}