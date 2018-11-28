#include "stdio.h"
#include "string"
#include "algorithm"
#include "math.h"
#include "vector"
#include "set"
#include "queue"
#include "map"
using namespace std;

typedef long long LL;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii > vii;
typedef queue<int> qi;
typedef set<int> si;

#define RE(i,b) for(int i=0; i<(int)(b); i++)
#define REP(i,a,b) for(int i=(int)(a); i<(int)(b); i++)
#define BREP(i,a,b) for(int i=(int)(a)-1; i>=(int)(b); i--)

#define INF 2000000000
#define MP make_pair
#define FI first
#define SE second

double C,F,X;

double visit(double R){
	double x=X/R;
	double y=C/R+X/(R+F);
	if(x<y)
		return x;
	else
		return C/R+visit(R+F);
}

int main(){
	int TC;scanf("%d ",&TC);
	RE(tc,TC){
		printf("Case #%d: ",tc+1);
		scanf("%lf %lf %lf ",&C,&F,&X);
		printf("%.7lf\n",visit(2));
	}
	return 0;
}