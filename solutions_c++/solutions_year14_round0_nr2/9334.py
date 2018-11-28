#include <cstdio>
using namespace std;

double C, F, X;

double solve(int i)
{
	double ret = X / (2 + F * i);
	for(int j = 0; j < i; j++)
		ret += C / (2 + F * j);
	return ret;
}

double solve()
{
	double ret = solve(0), nret;
	int i = 1;
	while(true){
		nret = solve(i++);
		if(ret < nret) break;
		ret = nret;
	}
	return ret;
}

int main() 
{
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++)
	{
		scanf("%lf %lf %lf", &C, &F, &X);
		printf("Case #%d: %.7f\n",i,solve());
	}
	return 0;
}