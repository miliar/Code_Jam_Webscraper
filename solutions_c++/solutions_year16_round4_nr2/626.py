#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <stack>
#include <map>
#include <set>
#include <deque>
#include <cstring>
#include <functional>
#include <climits>
#include <list>
#include <ctime>
#include <complex>

#define F1(x,y,z) for(int x=y;x<z;x++)
#define F2(x,y,z) for(int x=y;x<=z;x++)
#define F3(x,y,z) for(int x=y;x>z;x--)
#define F4(x,y,z) for(int x=y;x>=z;x--)
#define mp make_pair
#define pb push_back
#define LL long long
#define co complex<double>

#define MAX 100005
#define AMAX 1500
#define MOD 1000000007

#define f(c,d) ((1<<(c))*(d))

using namespace std;

int t,n,k,y[205];
double ta;
long double x[205],ans,dp[205][205];

void go(){
	dp[0][0]=1;
	F2(a,1,k){
		F2(b,0,a)dp[a][b]=0;
		F1(b,0,a){
			dp[a][b]+=dp[a-1][b]*x[y[a-1]];
			dp[a][b+1]+=dp[a-1][b]*(1-x[y[a-1]]);
		}
	}
	//F2(a,0,k)F2(b,0,a)printf("%.4lf%c",(double)dp[a][b],b==a?'\n':' ');
	ans=max(ans,dp[k][k/2]);
}

int main(){
	scanf("%d",&t);
	F2(a,1,t){		
		scanf("%d%d",&n,&k);
		F1(b,0,n){
			scanf("%lf",&ta);
			x[b]=ta;
		}
		sort(x,x+n);
		ans=0;
		F2(b,0,k){
			F1(c,0,b)y[c]=c;
			F1(c,b,k)y[c]=(n-1)-(c-b);
			//F1(c,0,k)printf("%d%c",y[c],c==k-1?'\n':' ');
			go();
		}
		printf("Case #%d: ",a);
		printf("%.10lf",(double)ans);
		printf("\n");
	}
	//system("pause");
	return 0;
}
