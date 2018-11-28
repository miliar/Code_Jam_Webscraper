#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> S;

int main(){
	int T, ti, N;
	int tmp, X,count;
	int i, j;
	FILE * inf, *outf;
	inf = fopen("A-large.in", "r");
	outf = fopen("A-large.out", "w");
	fscanf(inf,"%d", &T);
	//fscanf(inf, "%d", &T);
	for (ti = 0; ti < T; ti++){
		//fscanf(inf, "%d", &N);
		fscanf(inf,"%d%d", &N, &X);
		S.clear();
		for (i = 0; i < N; i++){
			fscanf(inf,"%d", &tmp);
			S.push_back(tmp);
		}
		sort(S.begin(), S.end());
		tmp = N - 1;
		for (i = 0,count=0; i < N - 1;i++){
			for (j = tmp; j > i&&(S[i]+S[j]>X); j--);
			tmp = j-1;
			if (j > i && (S[i] + S[j]<=X)) count++;
		}
		fprintf(outf, "Case #%d: %d\n", ti + 1,N-count);
		printf("Case #%d: %d\n", ti + 1,N-count);
	}
	fclose(inf);
	fclose(outf);
	return 0;
}
