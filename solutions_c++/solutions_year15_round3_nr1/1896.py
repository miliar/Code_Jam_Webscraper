#include <cstdio>
#include <string>
#include <algorithm>
#include <cmath>


bool board[400];

long long int moves1(long long int C,long long int W) {

	//if (C<=3) return C;

	long long int F = C/W;
	bool divisible = (C%W)==0;
	long long int S = divisible ? F + W -1 : F + W;

	//fprintf(stderr, "F=%lld and %lld is divisible by %lld:%d\n",F,C,W,divisible);

	return S;

}


int main() {

	long long int T;
	scanf("%lld",&T);

	fprintf(stderr,"%lld\n",T);

	long long int R,C,W;
	for(long long int TC = 1; TC <= T; TC++) {
		
		scanf("%lld %lld %lld",&R,&C,&W);
		if (R>C) std::swap(R,C);
		if (R==1) printf("Case #%lld: %lld\n",TC,moves1(C,W));
		else printf("Case #%lld: %lld\n",TC,moves1(C,W));

	}

}
