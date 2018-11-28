#include<cstdio>
#include<iostream>
#include<iomanip>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<string>
#include<sstream>
#include<vector>
#include<map>
#include<set>
#include<bitset>
#include<algorithm>
#include<cassert>
#include<ctime>
#include<queue>
using namespace std;

//#define SMALL
#define LARGE

double solve(double& C, double& F, double& X){
	double vt = (X - C)*F/C;
	double result = 0.0;
	double v = 2.0;
	while(v < vt){
		result += C/v;
		v += F;
	}
	result += X/v;
	return result;
}

int main()
{
#ifdef SMALL
	freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-small-attempt0.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","rt",stdin);
	freopen("B-large-attempt0.out","wt",stdout);
#endif
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		double C,F,X;
		cin >> C >> F >> X;
		printf("Case #%d: ", t);
		printf("%0.7f\n",solve(C,F,X) );
	}
}