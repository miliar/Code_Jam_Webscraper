#include <cstdio>

#define MAXN 105
#define forn(i,n) for(int i = 0; i < n; i++)
#define forn2(i,j,n) for(int i = j; i <= n; i++)

using namespace std;

int main(){
	int T,t;
	scanf("%d",&T);
	forn2(t,1,T){
		double C,F,X,f = 2, res = 0;
		scanf("%lf %lf %lf",&C,&F,&X);
		double nextFarm = C/f;
		double goal = X/f;
		double goalWithFarm = nextFarm + X/(f+F);
		while(goalWithFarm < goal){
			f += F;
			res += nextFarm;
			nextFarm = C/f;
			goal = X/f;
			goalWithFarm = nextFarm + X/(f+F);
		}
		res += goal;
		printf("Case #%d: %.7f\n",t,res);
	}
}