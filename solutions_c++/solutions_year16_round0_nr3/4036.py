#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
#include <string.h>
#include <string>
#include <queue>
#include <vector>
#include <time.h>
#include <complex>
#include <map>
#define LL long long
using namespace std;

const int MXN = 35, MXX = 15;

struct node {
	LL x, w[MXX]; //
};
int T, n, J;
LL mypow[MXX][MXN], record[MXX], record2[MXX];
vector <node> final;
void DFS(int step) {
	if(step == n) {
		bool ok = 0;
		//for(int i = 2; i <= 10; i++) printf("%I64d ", record[i]);printf("\n");
		for(int i = 2; i <= 10; i++) {
			LL tmp = min(record[i] - 1, ((LL)sqrt(record[i])) + 5); ///
			record2[i] = -1;
			for(int j = 2; j <= tmp; j++) { //
				if(record[i] % j == 0) {record2[i] = j; break;}
			}
			if(record2[i] < 0) {ok = 1; break;}
		}
		if(!ok) {
			node tmp;
			tmp.x = record[2];
			for(int i = 2; i <= 10; i++) tmp.w[i] = record2[i];
			final.push_back(tmp);
		}
		return ;
	}
	int w = 0;
	if(step == 0 || step == n - 1) w = 1; ///
	for(int i = w; i <= 1; i++) { //
		for(int j = 2; j <= 10; j++) record[j] += i * mypow[j][step]; //
		DFS(step + 1);
		if(final.size() == J) return ;
		for(int j = 2; j <= 10; j++) record[j] -= i * mypow[j][step]; //
	}
}
inline void solve() {
	scanf("%d", &T);
	scanf("%d%d", &n, &J); ///////
	for(int i = 2; i <= 10; i++) {
		mypow[i][0] = 1;
		for(int j = 1; j < n; j++) mypow[i][j] = mypow[i][j - 1] * i;
	}
	DFS(0);
	vector <int> tmp2;
	printf("Case #1: \n");
	for(int i = 0; i < final.size(); i++) { //
		LL tmp = final[i].x;
		tmp2.clear();
		while(tmp) {
			tmp2.push_back(tmp % 2); //
			tmp /= 2; //
		}
		for(int j = tmp2.size() - 1; j >= 0; j--) printf("%d", tmp2[j]);
		for(int j = 2; j <= 10; j++) printf(" %I64d", final[i].w[j]);
		printf("\n");
	}
}
int main() {
	freopen("C.in","r",stdin);freopen("C.out","w",stdout);
	solve();
	return 0;
}
