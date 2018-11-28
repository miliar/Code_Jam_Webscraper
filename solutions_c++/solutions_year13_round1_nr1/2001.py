#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <algorithm>
using namespace std;
#define Max(a,b) ((a)>(b)?(a):(b))
const double PI = acos(-1.0),eps = 1e-14;

int equa(double a,double b,double c){
	double x1,x2;
	double f = b * b - 4 * a * c;
	if(f<0)return -1;
	x1 = ( -b + sqrt(1.0 * f)) / (2 * a);
	x2 = ( -b - sqrt(1.0 * f)) / (2 * a);
	double x = Max(x1,x2);
	return floor(x);
}
int main(){
	freopen("e:\\A-small-attempt0.in","r",stdin);
	freopen("e:\\A-small-attempt0.out","w+",stdout);
	int t,cas=1;
	double r,v;
	scanf("%d",&t);
	while(t--){
		scanf("%lf%lf",&r,&v);
		int ans = equa(2,2 * r - 1,-v);
		printf("Case #%d: %d\n",cas++,ans);
	}return 0;
}