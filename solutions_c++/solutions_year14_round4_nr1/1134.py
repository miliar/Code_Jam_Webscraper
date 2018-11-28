#include <bits/stdc++.h>

using namespace std;

int N,X,in[10005];
bool b[10005];

void input(){
	scanf("%d%d", &N, &X);
	for (int i=0; i<N; i++){
		scanf("%d", &in[i]);
	}
	sort(in,in+N);
	memset(b,0,sizeof(b));
}
void solve(int nT){
	int res=N;
	for (int i=0; i<N; i++){
		if (b[i])
			continue;
		for (int j=N-1; j>i; j--){
			if (in[i]+in[j] <= X && !b[j]){
				res--;
				b[j] = 1;
				break;
			}
		}
	}
	printf("Case #%d: %d\n", nT, res);
}
int main(){
	int nT;
	scanf("%d", &nT);
	for (int i=1; i<=nT; i++){
		input();
		solve(i);
	}
}