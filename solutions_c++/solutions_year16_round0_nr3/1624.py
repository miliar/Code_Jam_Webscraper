#include "stdafx.h"
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
#include <math.h>
const int N = 16;
int aa[N];
long long int dd[10];
using namespace std;
int j;
map<long long int, int> m;
void solve(int i){
	if (j <= 0 || i > 15) return;
	for (int it = 0; it < 10; it++){
		dd[it] = 0;
	}
	for (int b = 2; b <= 10; b++){
		bool pf = true;
		long long int bn = 0;
		for( int it = 0; it <= N - 1; it++){
			bn = aa[it] + bn * b;
		}
		if (b == 10) {//printf("%d %lli\n", b, bn);
			if (m.find(bn) != m.end()) break;
		}
		for (long long int i = 2; i <= sqrtl(bn); i++){
			if (bn % i == 0) {
				dd[b - 2] = i;
				pf = false;
				break;
			}
		}
		if (pf == true) break;
		else { 
			if (b == 10){
				if (m.find(bn) == m.end()){
					m.insert(pair<long long int, int>(bn, 1));
					printf("%lli", bn);
					for (int it = 0; it < 9; it++){
						printf(" %lli", dd[it]);
					}
					printf("\n");
					j--;
				}
			}
		}
	}
	//j--;
	//for (int ii = i; ii <= 14; ii++){
	if (i > 14) return;
	aa[i] = 0;
	solve(i + 1);
	aa[i] = 1;
	solve(i + 1);
	aa[i] = 0;
		//aa[ii] = 0;
	//}
}
int main(int argc, char** argv){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tt;
	scanf(" %d", &tt);
	int n;
	scanf(" %d %d", &n, &j);
	aa[0] = 1; aa[15] = 1;
	printf("Case #1:\n");
	solve(1);
	//long long int jj = 1<<14;
	//long long int j = 1;
	//while (j <= jj){
		
	//}
}