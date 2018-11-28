#include <bits/stdc++.h>

#define FWD(a,b,c) for(int a=(b); a<(c); ++a)
#define SIZE(a) ((int)a.size())
#define pb push_back
#define PII pair<int, int>
#define x first
#define y second

using namespace std;

typedef long long LL;

int n, p, q;
int H[110];
int G[110];

bool cmp(const int a, const int b){
	return G[a] > G[b];
}

bool C[110];
int ord[110];
LL res;

int ceil(int a, int b){
	return (a+b-1)/b;
}

bool check(){
	int shots = 1;
	FWD(i,0,n){
		if(!C[i]){
			shots += ceil(H[i], q);
		}else{
			int k;
			if(H[i] % q){
				shots += H[i] / q;
				k = ceil(H[i] % q, p);
			}else{
				shots += H[i] / q - 1;
				k = ceil(q, p);
			}
			if(shots < k) return 0;
			shots -= k;
		}
	}
	return 1;
}

int main(){
	int Z; scanf("%d", &Z); FWD(z,1,Z+1){
		scanf("%d %d %d", &p, &q, &n);
		FWD(i,0,n){
			scanf("%d %d", &H[i], &G[i]);
			ord[i] = i;
			C[i] = 0;
		}
		res = 0;
		sort(ord, ord+n, cmp);
		FWD(_i,0,n){
			int i = ord[_i];
			C[i] = 1;
			if(!check())
				C[i] = 0;
			else
				res += G[i];
		}
		printf("Case #%d: %lld\n", z, res);
	}
	return 0;
}
