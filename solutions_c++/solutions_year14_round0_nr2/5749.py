#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<math.h>
#include<queue>
#include<stack>
#include<stdio.h>
#include<map>
#include<set>
#include<memory.h>
#include<algorithm>
#include<vector>
#include<stdlib.h>
#include<sstream>
using namespace std;
typedef long long ll;
ll ABS(ll x){
	if (x<0)return -x;
	return x;
}
ll gcd(ll a, ll b){
	if (!b)
		return a;
	return gcd(b, a%b);
}
ll lcm(ll a, ll b){
	return b / gcd(a, b)*a;
}
#define FOR(I,N) for(int(i)=0;i<int(N);++i)
#define FORK(I,N,K) for(int(i)=0;i<int(N);i+=int(K))
double calc(int mid, double x, double f, double c){
	double cost = 0;
	double prod = 2;
	for (int i = 0; i < mid; ++i){
		double nxt = c / prod;
		cost += nxt;
		prod += f;
	}
	return cost + x / prod;
}
int t;
double c, f, x;
int main(){
	freopen("B-small-attempt2.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	for (int k = 1; k <= t;++k){
		scanf("%lf", &c);
		scanf("%lf", &f);
		scanf("%lf", &x);
		int l = 0, h = 10000;
		double res = h;
		res*=res;
		for (int it = 1; it <= 128; ++it){
			double nl = calc((2 * l + h) / 3, x, f, c);
			double nh = calc((2 * h + l) / 3, x, f, c);
			res = min(res, min(nl, nh));
			if (nl > nh)
				l = (2 * l + h) / 3 + 1;
			else 
				h = (2 * h + l) / 3 - 1;
		}
		printf("Case #%d: %0.7lf\n", k, res);
	}
}