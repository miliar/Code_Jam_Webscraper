#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

struct data{
	int no, va, rk;
};

struct data A[1024], B[1024];
int po[1024];

bool cmp1(const data &a, const data &b){
	if (a.no > b.no){
		return false;
	}
	else return true;
}

bool cmp2(const data &a, const data &b){
	if (a.va > b.va){
		return false;
	}
	else return true;
}

int main(){
	int T, ti, N;
	int tmp, tm, p, q, count, fg;
	int i, j;
	FILE * inf, *outf;
	inf = fopen("B-large(1).in", "r");
	outf = fopen("B-large(1).out", "w");
	fscanf(inf, "%d", &T);
	for (ti = 0; ti < T; ti++){
		fscanf(inf, "%d", &N);
		memset(A, 0, sizeof(A));
		memset(B, 0, sizeof(B));
		for (i = 0; i < N; i++){
			fscanf(inf, "%d", &(A[i].va));
			A[i].no = i;
		}
		sort(A, A + N, cmp2);
		for (i = 0; i < N; i++){
			A[i].rk = i;
			B[i] = A[i];
		}
		sort(B, B + N, cmp1);
		for (i = 0; i < N; i++){
			po[A[i].rk] = A[i].no;
		}
		tmp = 0;
		count = 0;
		p = 0; 
		q = N - 1;
		for (i = 0; i < N; i++){
			if (po[A[i].rk] - p < q - po[A[i].rk]){
				tmp += po[A[i].rk] - p;
				for (j = A[i].rk + 1; j < N; j++) if (po[j] < po[A[i].rk]) po[j] += 1;
				p++;
			}
			else {
				tmp += q-po[A[i].rk];
				for (j = A[i].rk + 1; j < N; j++) if (po[j] > po[A[i].rk]) po[j] -= 1;
				q--;
			}
		}
		fprintf(outf, "Case #%d: %d\n", ti + 1, tmp);
		printf("Case #%d: %d\n", ti + 1, tmp);
	}
	fclose(inf);
	fclose(outf);
	return 0;
}

