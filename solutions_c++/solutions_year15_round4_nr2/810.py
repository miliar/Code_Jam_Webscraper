#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <queue>
#include <math.h>
#include <bitset>
#include <climits>
#define MP make_pair

using namespace std;
typedef long long LL;
typedef unsigned int uint;
const double pi = atan (1.0) * 4;

int N;
double V, X;
double R[10], C[10];

int main (){
	int T; scanf ("%d",&T);
	for (int cas=1;cas<=T;cas++){
		scanf ("%d%lf%lf",&N,&V,&X);
		for (int i=0;i<N;i++)	scanf ("%lf%lf",&R[i],&C[i]);
		printf ("Case #%d: ",cas);
		if (N == 1){
			if (X != C[0])	printf ("IMPOSSIBLE\n");
			else {
				printf ("%f\n", V/R[0]);
			}
			continue;
		}
		if (C[0] == C[1]){
			if (C[0] == X){
				printf ("%f\n",V/(R[0] + R[1]));
			}
			else 
				printf ("IMPOSSIBLE\n");
			continue;
		}
		double at = (V*X - V*C[1]) / (C[0] - C[1]);
		if (at < 0 || at > V){
			printf ("IMPOSSIBLE\n");
		}
		else {
			double at2 = V - at;
			double _t = max (at/R[0], at2/R[1]);
			printf ("%f\n", _t);
		}
	}
	return 0;
}