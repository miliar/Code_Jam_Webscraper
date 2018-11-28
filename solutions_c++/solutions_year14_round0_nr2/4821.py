#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <utility>
#include <vector>
#include <map>
#include <set>

#define REP(a,b) for (int a = 0; a < b; a++)
#define FOR(a,b,c) for (int a = b; a <= c; a++)
#define RESET(a,b) memset(a,b,sizeof a)

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define PII pair<int,int>
#define INF 2123123123

#define LL long long
using namespace std;

int T;
double C,F,X;
double EPS = 1e-12;

double lesseq(double a, double b){
	if (fabs(a-b) < EPS) return 1;
	return a < b;
}

double cookie(int nf){
	nf = max(nf, 0);
	
	double v = 2;
	double tot = 0;
	REP(i,nf){
		tot += (C/v);
		v += F;
	}
	
	return tot + X/v;
}

int main(){		
	scanf("%d", &T);
	REP(jt,T){
		scanf("%lf%lf%lf", &C, &F, &X);
	
	
		int ki = 0;
		int ka = (int)(X+2);
		double ans = min(cookie(ki), cookie(ka));
		while (ki <= ka){
			int tgh = (ki + ka) >> 1;
			
			double t1 = cookie(tgh-1);
			double t2 = cookie(tgh);
			double t3 = cookie(tgh+1);
			
			if (lesseq(t1, t2) && lesseq(t2, t3)){
				ka = tgh - 1;
			}else if (lesseq(t3, t2) && lesseq(t2, t1)){
				ki = tgh + 1;
			}else{
				ans = min(ans, t2);
				break;
			}
		}
		
		printf("Case #%d: %.7lf\n", jt+1, ans);
	}
	return 0;
}
