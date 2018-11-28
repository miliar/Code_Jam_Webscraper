
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;
typedef long long i8;

int ntc$, cas$;

i8 n,x;
char alf[255], str[10111];
int mtx[][5]={
		{0, 0, 0, 0, 0},
		{0, 1, 2, 3, 4},
		{0, 2,-1, 4,-3},
		{0, 3,-4,-1, 2},
		{0, 4, 3,-2,-1}
	};

int joi(int a, int b) {
	if (a<0) {
		if (b<0)
			return mtx[-a][-b];
		return -mtx[-a][b];
	}
	if (b<0)
		return -mtx[a][-b];
	return mtx[a][b];
}

i8 minf(char z, bool fw) {
	int v=1, zi=alf[z];
	for (int i=0; i<4*n; i++) {
		v=fw?joi(v, alf[str[i%n]]):joi(alf[str[i%n]],v);
		if (v==zi) {
			return i+1;
		}
	}
	return 100011100011100011LL;
}
	
bool solve() {
	scanf("%lld%lld",&n,&x);
	scanf("%s",str);
	
	int b=1;
	for (int i=0; i<n; i++) {
		b=joi(b, alf[str[i]]);
	}
	
	int t=1;
	for (int i=0; i<x%4; i++) {
		t=joi(t, b);
	}
	if (t!=-1)
		return false;

	i8 mI=minf('i',true);
	reverse(str,str+n);
	i8 mK=minf('k',false);
		
	return mI+mK<n*x;
}

main() {
	alf['i']=2;
	alf['j']=3;
	alf['k']=4;

	scanf("%d", &ntc$);
	for (int cas$=1; cas$<=ntc$; cas$++) {
		printf("Case #%d: %s\n", cas$, solve()?"YES":"NO");
	}
}
