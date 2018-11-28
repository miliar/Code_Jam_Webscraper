#include <iostream>
#include <math.h>
#include <algorithm>
#include <string>
#include <cstdio>

#define SC(x) scanf("%d", &x);
#define File freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);

using namespace std;
const long long inf =2147483647;
const int md=1e9+7;
const double eps=1e-6;

int n,m,i,j,ttt,tt,A,B,K,a,b,k;
long long ans;

int main(){
	File;
	SC(ttt);
	for (tt=1; tt<=ttt; tt++){
		printf("Case #%d:",tt);
		SC(A); SC(B); SC(K);
		ans=0;
		for (a=0; a<A; a++)
			for (b=0; b<B; b++){
				if ((a&b)<K) ans++;
			}
		printf(" %lld\n",ans);
	}
	return 0;
}
