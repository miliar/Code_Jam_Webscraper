#include <bits/stdc++.h>

using namespace std;

const int MXN = 1005;

int N,x[MXN],in[MXN];
int mxPos;
int bit[MXN];

int lb(int asdf){
	return asdf & -asdf;
}
void update(int st){
	bit[st]++;
	return ;
	for (int i=st; i>0; i-=lb(i)){
		bit[i]++;
	}
}
int query(int st){
	int res=0;
	for (int i=st; i<MXN; i++){
		res += bit[i];
	}
	return res;
	for (int i=st; i<MXN; i+=lb(i)){
		res += bit[i];
	}
	return res;
}
void input(){
	scanf("%d", &N);
	mxPos = 0;
	for (int i=0; i<N; i++){
		scanf("%d", &in[i]);
		if (in[i] > in[mxPos]){
			mxPos = i;
		}
		x[i] = in[i];
	}
	sort(x,x+N);
	for (int i=0; i<N; i++){
		for (int j=0; j<N; j++){
			if (in[i] == x[j]){
				in[i] = j + 1;
				break;
			}
		}
	}
	/*
	for (int i=0; i<N; i++)
		printf("%d ", in[i]);
	puts("");
	*/
}
int check(){
	int res = 0;
	int y[MXN];
	for (int i=0; i<N; i++){
		y[x[i]] = i;
	}
	for (int i=0; i<N; i++){
		x[i] = y[in[i]];
	}
	for (int i=0; i<N; i++)
		for (int j=i+1; j<N; j++)
			if (x[i] > x[j])
				res++;
	return res;
}
void solve(int nT){
	int res=N*N;
	int per[MXN];
	for (int i=0; i<N; i++)
		per[i] = i;
	do{
		int pos=0;
		for (int i=0; i<N; i++){
			x[i] = in[per[i]];
			if (x[i] > x[pos])
				pos = i;
		}
		int fail = 0;
		for (int i=0; i<pos; i++)
			if (x[i] > x[i+1])
				fail = 1;
		for (int i=N-1; i>pos; i--){
			if (x[i] > x[i-1])
				fail = 1;
		}
		if (!fail){
			int tmp = check();
			if (tmp < res)
				res = tmp;
		}
	}	while (next_permutation(per,per+N));
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