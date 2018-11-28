#include <fstream>
#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;

int T, N;
double Naomi[1000], Ken[1000];
int p, q;
int nCnt, kCnt;

int main(){
	FILE* in = fopen("C:\\Users\\Jinhyuk\\Desktop\\CodeJam 2014\\Qual\\D-large.in", "r");
	FILE* out = fopen("C:\\Users\\Jinhyuk\\Desktop\\CodeJam 2014\\Qual\\testResult.txt", "w");
	
	fscanf(in, "%d", &T);
	for(int i=0; i<T; i++){
		fscanf(in, "%d", &N);
		p = q = N-1;
		nCnt = kCnt = 0;
		for(int j=0; j<N; j++) fscanf(in, "%lf", &Naomi[j]);
		for(int j=0; j<N; j++) fscanf(in, "%lf", &Ken[j]);
		sort(Naomi, Naomi+N);
		sort(Ken, Ken+N);
		while(1){
			if(Naomi[p] > Ken[q]){
				nCnt++;
				p--;
				q--;
			}else {
				q--;
			}
			if(p == -1 || q == -1) break;
		}
		p = q = N-1;
		while(1){
			if(Naomi[p] < Ken[q]){
				kCnt++;
				p--;
				q--;
			}else {
				p--;
			}
			if(p == -1 || q == -1) break;
		}
		fprintf(out, "Case #%d: %d %d\n", i+1, nCnt, N-kCnt);
	}
	fclose(in);
	fclose(out);
	return 0;
}

