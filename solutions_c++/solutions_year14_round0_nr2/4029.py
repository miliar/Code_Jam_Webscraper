#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
#include <sstream>

using namespace std;

#define REP(i,a,b) 	for(int i=a;i<(int)b;i++)
#define FOR(it,A)	for(typeof A.begin() it=A.begin();it!=A.end();it++)
#define all(x) 		(x).begin(),(x).end()
#define pb 			push_back
#define clr(x,y)	memset(x,y,sizeof x)
#define oo 			(1<<30)
#define inf 		(1LL<<40)
#define bit(x)		__builtin_popcount(x)
#define mp			make_pair
#define fst			first
#define snd			second
#define maxN		100005
#define mod			1000000007
#define eps			1e-9
typedef long long     ll;
typedef vector<int>   vi;
typedef pair<int,int> pii;
typedef long double   ld;

double C, F, X;
double times[100000000];

int main(){
	
	int casos;
	scanf("%d",&casos);
	REP(caso,1,casos+1){
		scanf("%lf %lf %lf", &C, &F, &X);
		double ans = X/2;
		times[0] = ans;
		for(int n=1;n<=100000000;n++){
			double d1 = 2.0 + (n-1)*F;
			double d2 = 2.0 + n*F;
			times[n] = times[n-1] + (C-X)/d1 + X/d2;
			if(times[n] > times[n-1]){
				//cout << n << endl;
				break;
			}
			ans = min(ans,times[n]);
		}
		printf("Case #%d: %.7lf\n", caso, ans);
	}
	
	
    return 0;
}






