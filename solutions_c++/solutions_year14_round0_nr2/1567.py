#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>
#include <climits>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <utility>
#include <algorithm>

#define PB push_back

#define PP pair<int, int>
#define MP make_pair
#define F first
#define S second

using namespace std;

typedef long long ll;

int main(){
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++){
		printf("Case #%d: ", i);

		double C, F, X;
		scanf("%lf %lf %lf", &C, &F, &X);
		
		int K = (X*F - 2*C)/(F*C);
		if (K < 0) K = 0;
		else K = floor(K);

		double time = 0.0;
		for (int i = 0; i < K; i++) time += C/(2+i*F);
		time += X/(2+K*F);

		printf("%0.7f\n", time);
	}
	return 0;
}
