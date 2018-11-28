#include <algorithm>
#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <sstream>
#include <stdio.h>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <list>
#include <set>
#include <map>
using namespace std;
 
#define N  128
#define ALL(x)     x.begin(),x.end()
#define CLR(x,a)   memset(x,a,sizeof(x))
typedef long long    ll;
const int INF  = 0x3fffffff;
const int MOD  = 1000000007;
/*-----------code------------*/
double C,F,X;

double  solve(int num){
	double sum=0.0,add=2.0;
	while(num--){
		sum+=C/add;
		add+=F;
	}
	sum+=X/add;
	return sum;
}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("output.out","w",stdout);
	int re,Case=1;
	scanf("%d",&re);
	while(re--){
		scanf("%lf%lf%lf",&C,&F,&X);
		int n=floor(X);
		double ans=1e30;
		for(int i=0;i<=n;i++){
			double now=solve(i);
			if(now<ans) ans=now;
			else break;
		}
		printf("Case #%d: %.9lf\n",Case++,ans);
	}
	return 0;
}
