#include <stdio.h>
#include <iostream>
#include <cstring>
#include <vector>
#include <stack>
#include <queue>
#include <math.h>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>
#include <limits>

#define maxN(a,b) ((a>b)?(a):(b))
#define minN(a,b) ((a<b)?(a):(b))
#define INF (int)10e9
#define ABS(n)	((n>0)? n:(-1*n))
#define NINF -(int)10e9
#define eps 10e-9
#define WORDSIZE 31

using namespace std;

typedef vector<int> V;
typedef pair<int,int> PII;
typedef long long ll;
typedef vector<string> VS;
typedef vector<pair<int, int> > VPII;


double days = 0;
double c, f, x;
double solve(double prev, double count, double rate){
	if( prev > days) return days;	
	else if( x-count <= eps ){
		return days;
	}
	else{
		
		if( (prev+(x/rate)) - days < eps) days = prev+(x/rate);
		double temp = prev + c/rate;
		//printf("%lf %lf %lf %lf\n", temp, prev, rate, days);
		solve(temp, count, rate+f);
		 
	}
}
int main() {
	int tc;
	scanf("%d", &tc);
	for(int i = 1; i <= tc; i++){
	scanf("%lf %lf %lf", &c, &f, &x);
	double minn = x/2;
	days = minn;
	minn = fmin( solve(0,0,2), minn);
	printf("Case #%d: %.7lf\n", i, minn);

	}
	return 0;
}

