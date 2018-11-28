#include <algorithm>
#include <cstdio>
#include <cmath>
using namespace std;

typedef long double ld;

int T;
ld C, F, X;
int opt;

int main()
{
	scanf("%d", &T);

	for(int q=1; q<=T; q++) {
		scanf("%Lf%Lf%Lf", &C, &F, &X);
		ld s=0.0;
		opt=max(0, (int)ceil(X/C-2.0/F-1.0));
		for(int i=1; i<=opt; i++) {
			s+=C/(2.0+(i-1)*F);
		}
		s+=X/(2.0+opt*F);
		printf("Case #%d: %.7Lf\n", q, s);
	}

	return 0;
}
