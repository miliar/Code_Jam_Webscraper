#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
#define N_MAX 1010
using namespace std;

int N;
double Nao[N_MAX], Ken[N_MAX],  Naos[N_MAX], Kens[N_MAX];
int solve(double *weak, double *op){
	int ret = 0;
	for(int i = 0; i < N; i++){
		int ptr = -1;
		for(int j = 0; j < N; j++){
			if( op[j] > weak[i] && (ptr == -1 || op[j] < op[ptr]) ) ptr = j;
		}
		if(ptr != -1){
			ret++;
			op[ptr] = -1;
		}
	}
	return ret;
}
int main(){
	freopen("D-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int cnt = 1; cnt <= T; cnt++){
		scanf("%d", &N);
		for(int i = 0; i < N; i++) scanf("%lf", &Nao[i]);
		for(int i = 0; i < N; i++) Naos[i] = Nao[i];
		for(int i = 0; i < N; i++) scanf("%lf", &Ken[i]);
		for(int i = 0; i < N; i++) Kens[i] = Ken[i];
		printf("Case #%d: %d %d\n", cnt, solve(Ken, Nao), N - solve(Naos, Kens));
	}
	return 0;
}
