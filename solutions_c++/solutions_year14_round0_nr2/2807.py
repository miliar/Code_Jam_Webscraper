#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;

int main(){
	freopen("B-large.in","r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	scanf("%d",&t);
	for(int casenum = 0;casenum < t;++casenum){
		printf("Case #%d: ",casenum+1);
		double C, F, X;
		double rate = 2.0;
		cin >> C >> F >>X;
		if (X <=C){
			printf("%.7lf\n",X/rate);
			continue;
		}
		double ans = X/rate;
		double t = 0;
		while(1){
			double temp = C/rate;
			rate = rate+F;
			double t2 = X / rate;
			if (ans > t + temp + t2){
				ans = t + temp + t2;
				t = t + temp;
			}else break;

		}
		printf("%.7lf\n",ans);

	}
	return 0;
}