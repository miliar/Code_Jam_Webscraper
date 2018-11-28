#include <iostream>
#include <math.h>
#include <algorithm>
#include <string>
#include <cstdio>

#define SC(x) scanf("%d", &x);
#define File freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
#define No {printf("GABRIEL\n"); continue;}
#define Yes {printf("RICHARD\n"); continue;}

using namespace std;
const long long inf =2147483647;
const int md=1e9+7;
const double eps=1e-6;

int n,m,i,j,k,ttt,tt,x;

int main(){
	File;
	SC(ttt);
	for (tt=1; tt<=ttt; tt++){
		printf("Case #%d: ",tt);
		SC(x); SC(n); SC(m);
		if (n>m) swap(n,m);
		if (x+x>n*m && x!=n*m) Yes; //5
		if (x>m) Yes; //1...
		if ((n*m)%x) Yes;
		if (n==1){
			if (m==1 && x>=2) Yes;
			if (x<=2) No;
			Yes;
		}
		if (n==2){
			if (x>=4) Yes;
			if (m==2 && x==3) Yes;
			No;
		}
		if ((n+n+1)<=x) Yes;
		if (x>=m+1 && x<=n*m-1) Yes; //4
		if (n>3 && (n-1)*2-1<=x) Yes; //6
		if (n==3 && n*2-1<=x) Yes;
		No;
		//printf("\n");
	}
	return 0;
}
