#include<vector>
#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include <set>
using namespace std;

double C, F, X;
double tt;

bool check(double s) {
	if(X/s <= C/s + X/(s+F))
		return false;
	return true;
}

int main() {
//	freopen ("B-large.in","r",stdin);
//	freopen ("out_large.txt","w",stdout);
	
	
	int t;
	scanf("%d", &t);
	while (t--) {
		tt=0.0;
		scanf("%lf", &C);
		scanf("%lf", &F);
		scanf("%lf", &X);
		
		if(X<=C){
			tt=X/2.0;
		}
		else {
			double ff=2.0;
			double remain_t=X/ff;
			bool flag=check(ff);
			while (flag){
				tt += C/ff;
				ff += F;
				remain_t=X/ff;
				flag=check(ff);
			}
			
			tt += remain_t;
		}
		
		static int id = 0;
		printf("Case #%d: %.7f\n", ++id, tt);
		
		
	}
	return 0;
}
