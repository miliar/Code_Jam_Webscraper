#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <utility>
#include <stack>
#include <queue>
#include <map>

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define pi 2*acos(0.0)
#define eps 1e-8
#define PII pair<int,int> 
#define PDD pair<double,double>
#define LL long long

using namespace std;

double R, C, X, F, T;
int N;

int main()
{
	scanf("%d", &N);
	for(int n = 1; n <= N; n++) 
	{
		scanf("%lf %lf %lf", &C, &F, &X);
		R = 2.0;
		
		T = 0;
		while((X / R) -  (C / R + X / (R + F)) > eps) {
			T += C / R;
			R += F;
		}
		
		T += X / R;
		
		printf("Case #%d: %.7lf\n", n, T);
	}
	return 0;
}

