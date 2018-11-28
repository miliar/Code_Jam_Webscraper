/****************************************
* File Name: b.cpp
* Author: sky0917
* Created Time: 2014Äê04ÔÂ12ÈÕ 10:24:57
****************************************/
#include <map>
#include <cmath>
#include <queue>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const int maxn = 10005;

double c, f, x;
int main(){
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);

	int T;
	int ca = 1;
	double res;
    scanf("%d",&T);
	while (T--){
		scanf("%lf %lf %lf",&c,&f,&x);
		double res = x / 2.0;
		double tmp = 0;
		double ti = 0, cnt = 2.0;
		for (double i = 1; ; i += 1){
			if (c * i > x) break;
			tmp = ti + c / cnt + x / (cnt+f);
			ti += c / cnt;
			cnt += f;
			res = min(tmp, res);
		}
		printf("Case #%d: %.7lf\n",ca++, res);
	}
	return 0;
}

