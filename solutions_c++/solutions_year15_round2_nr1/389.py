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

int n,m,i,j,k,ttt,tt,t,ii,d[1009009];
long long ans;

int main(){
	File;
	SC(ttt);
	for (tt=1; tt<=ttt; tt++){
		printf("Case #%d:",tt);
		SC(n);
		d[1]=1;
		for (i=2; i<=n; ++i){
			d[i]=d[i-1]+1;
			if ((i%10)==0) continue;
			t=0;
			ii=i;
			while (ii){
				t=t*10+(ii%10);
				ii/=10;
			}
			if (t<i) d[i]=min(d[i], d[t]+1);
		}
		printf(" %d\n", d[n]);
	}
	return 0;
}
