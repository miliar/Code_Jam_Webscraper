#include <algorithm>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define DEBUG(x) cout << ">>> " << #x << " : " << x << endl;
#define REP(i,a) for (int i = 0; i < (a); ++i)
#define FOR(i,a,b) for (int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for (int i = (a); i >= (b); --i)
#define FOREACH(it, a) for (__typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)
#define  pb push_back
#define  pu push
#define SA(a,x) memset(a,x,sizeof(a))

inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

const int INF = 1<<29;
typedef long long ll;
typedef pair<int ,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
///////////////////////////////////////////////////////////////////////////

int T,N,P;
double C,F,X;
double ans;


int main()
{
P = 1;
scanf("%d",&T);
while(T--){
	scanf("%lf %lf %lf",&C,&F,&X);
	N = 0;
	ans = 0;
	while(X/(2+N*F)>(X/(2+(N+1)*F)+C/(2+N*F))){
		ans+=C/(2+N*F);
		N++;
	}
	ans+=X/(2+N*F);
	printf("Case #%d: %.7lf\n",P++,ans);
	
}
return 0;
}
