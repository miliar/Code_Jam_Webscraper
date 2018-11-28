#include <cstdio>
#include <algorithm>
#define ll long long
using namespace std;
#include <iostream>
#define D(a...)do{cout<<#a<<" = ";_2,a;cout<<endl;cout.flush();}while(0)
struct _1{template<typename T>_1&operator,(const T&v){cout<<v<<"; ";return*this;}}_2;

const int MAXN = 20;

int N, J;
ll powx[MAXN][MAXN];

ll div(ll x) {
	for(ll d = 2; d*d <= x; d++) {
		if(x%d == 0)
			return d;
	}
	return 0;
}

int main() {
	for(int i = 0; i < MAXN; i++) {
		for(int j = 0; j < MAXN; j++)
			powx[i][j] = j? i*powx[i][j-1] : 1;
	}
	freopen("C-small-attempt0.in", "r", stdin);
	scanf("%d", &N);
	scanf("%d%d", &N, &J);
	puts("Case #1:");
	for(int i = 0; i < 1<<(N-2) && J; i++) {
		vector<ll> d;
		int x = (1<<(N-1)) + (i<<1) + 1;
		for(int b = 2; b <= 10; b++) {
			ll bx = 0;
			for(int i = 0; i < N; i++)
				bx += powx[b][i]*((x>>i)&1);
			if(div(bx) == 0)
				goto end;
			d.push_back(div(bx));
		}
		for(int j = N-1; j >= 0; j--)
			printf("%d", (x>>j)&1);
		printf(" ");
		for(ll x: d)
			printf("%lld ", x);
		puts("");
		J--;
		end:;
	}
}