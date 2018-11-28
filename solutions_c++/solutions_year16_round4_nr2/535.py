#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

double f[222][222];
double a[222];
double p[444];
int n,k;
double work(int s){
	for (int i = 1; i <= k; ++i){
		a[i]=p[s+i-1];
		f[0][i]=0;
	}
	f[0][0]=1;
	for (int i = 1; i <= k; ++i){
		f[i][0] = f[i-1][0] * (1-a[i]);
		for (int j = 1; j <= i; ++j){
			f[i][j] = f[i-1][j]*(1-a[i])+f[i-1][j-1]*a[i];
		}
	}
	return f[k][k/2];
}
int main(int argc, char const *argv[])
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int T;
	cin>>T;
	for (int i = 1; i <= T; ++i){
		double ans =0;
		printf("Case #%d: ", i);
		cin>> n>>k;
		for (int j = 0; j < n; ++j){
			cin>>p[j];
		}
		sort(p,p+n);
		for (int j = 0; j < n; ++j){
			p[j+n]=p[j];
		}

		for (int start = 0; start < n; ++start){
			double x = work(start);
			if (x>ans) ans =x;
		}
		printf("%.7f\n", ans);
	}
	return 0;
}