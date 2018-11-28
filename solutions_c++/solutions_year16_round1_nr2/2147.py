#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <algorithm>

using namespace std;

int N, k;

struct roc{
	int roc[51];
}a[2501];

bool cmp(const roc &a, const roc &b){
	return a.roc[k]<b.roc[k];
}

int main(){
	int T,C;
	int ans[51], ano[51];
	for (scanf("%d", &T), C = 1; C <= T; C++){
		printf("Case #%d: ", C);
		scanf("%d", &N);
		for (int i = 0; i < 2*N-1; i++)
			for (int j = 0; j < N; j++)
				scanf("%d", &a[i].roc[j]);
		int wh = 0;
		for (int i = 0; i < N; i++){
			k = i;
			sort(a, a+2*N-1, cmp);
			if (a[i*2].roc[i]!=a[i*2+1].roc[i]){
				wh = i;
				for (int j = 0; j < N; j++) ano[j] = a[i*2].roc[j];
				ans[i] = a[i*2].roc[i];
				break;
			}
		}
		int cnt = 0;
		for (int i = 0; i < 2*N-1;)
			if (cnt == wh){
				i++;
				cnt ++;
			} else {
				//printf("%d\n", i);
				k = cnt;
				sort(a, a+2*N-1,cmp);
				if (a[i].roc[wh] == ano[cnt]) ans[cnt] = a[i+1].roc[wh];
				else ans[cnt] = a[i].roc[wh];
				i+=2;
				cnt ++;
			}

		printf("%d", ans[0]);
		for (int i = 1; i < N; i++)
			printf(" %d", ans[i]);
		printf("\n");
	}
	return 0;
}