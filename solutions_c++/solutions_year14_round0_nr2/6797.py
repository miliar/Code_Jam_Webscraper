#include<cstdio>

using namespace std;

double C, F, X , akt;

double calc() {
	double out = 0.0;
	akt = 2.0;
	scanf("%lf %lf %lf", &C, &F, &X);
	while(true) {
		if(X/akt <= (X/(akt+F) + C/akt))
			return out+X/akt;
		out+=C/akt;
		akt+=F;
	}
}


int main()
{
	int T;
	scanf("%d", &T);
	for(int i = 1; i<=T; i++)
		printf("Case #%d: %lf\n", i, calc());
	return 0;
}
