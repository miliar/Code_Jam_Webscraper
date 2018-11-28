#pragma warning(disable:4996)
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
#include<vector>
#include<cmath>
#include<cstdio>
using namespace std;

double C, F, X;
double I;

double cal(int n)
{
	double res = 0;
	for (int i = 0; i < n; i++){
		res += C / (I + (i + .0)*F);
	}
	res += X / (I+n*F);
	return res;
}

int main()
{
	freopen("B-large.in.txt", "r", stdin);
	freopen("B-large.out.txt", "w", stdout);
	int T; cin >> T; int ca = 0;
	while (T--)
	{
		cin >> C >> F >> X;
		I = 2.0;
		double ans = 1e9;
		int i = 0;
		while (1){
			double tmp = cal(i);
			if (tmp < ans) ans = tmp;
			if (tmp>ans) break;
			i++;
		}
		printf("Case #%d: %.8lf\n", ++ca, ans);
	}
	return 0;
}