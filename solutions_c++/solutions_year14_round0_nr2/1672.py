#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<cmath>
using namespace std;

int Case;
double C, F, X;
double ans;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &Case);
	for (int tt = 1; tt <= Case; ++tt){
		scanf("%lf %lf %lf", &C, &F, &X);
		double now = 2.0;
		ans = X / now;
		double t = 0;
		while (t < ans){
			t += C / now;
			now += F;
			ans = min(ans, t + X / now);
			}
		printf("Case #%d: %.7lf\n", tt, ans);
		}
	return 0;
	}
