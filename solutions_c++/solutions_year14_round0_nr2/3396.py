#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <ctime>
#include<cstdlib>
using namespace std;
#define eps 1e-10
#define maxn 100010
#define pi acos(-1.0)
double r;
double c, f, x;
int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int t;
	scanf("%d", &t);
	int kase = 0;
	while (t--){
		scanf("%lf %lf %lf", &c, &f, &x);
		double ans = 100000;
		r = 2;
		double tmp = 0;
		for (int i = 0; i <= 100000; i++){
			ans = min(ans, x / r+tmp);
			tmp += c / r;
			r += f;
		}
		printf("Case #%d: %.7lf\n", ++kase, ans);
	}
	return 0;
}