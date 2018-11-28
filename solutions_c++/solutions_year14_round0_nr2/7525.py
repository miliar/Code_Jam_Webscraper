#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
using namespace std; 
    //freopen("./ipt", "r", stdin);
#define lson rt<<1
#define rson rt<<1|1
#define INF 0x3f3f3f3f
#define LL long long
#define uLL unsigned long long
#define mod 1000000007
#define pi 3.1415926535898
#define mxn 105
#define mxe 10005
#define left left_
#define right right_

double x, c, f;

double foo(double p, double cur){
	if((f+p)*c-f*x<0)
		return c/p+foo(p+f, cur);
	else
		return cur/p;
}

int main(){
    //freopen("./B-large.in", "r", stdin);
	int T, tt=0;
	cin>>T;
	while(++tt<=T){
		cin>>c>>f>>x;
		double ans=foo(2, x);
		printf("Case #%d: %.7lf\n", tt, ans);
	}
	return 0;
}
