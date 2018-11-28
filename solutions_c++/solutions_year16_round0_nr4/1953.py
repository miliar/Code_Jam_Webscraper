#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cstdlib>

using namespace std;
#define rep(i,a,b) for (int i=(a);i<=(b);i++)
#define repd(i,a,b) for (int i=(a);i>=(b);i--)

int k,c,s;

int main() {
	freopen("d.out","w",stdout);
	int T;scanf("%d\n",&T);
	rep(t,1,T) {
		printf("Case #%d:",t);
		scanf("%d%d%d\n",&k,&c,&s);
		rep(i,1,s) printf(" %d",i);
		puts("");
	}
	return 0;
}
