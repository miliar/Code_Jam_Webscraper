#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <assert.h>
#include <stdio.h>
#include <ctime>
#include <cstdlib>
#include <string>
#include <utility>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <complex>

#define inf 1000000007
#define pii pair<int,int>
#define pip pair<int,pii>
#define pll pair<long long,long long>
#define pif pair<int,double>
#define pfi pair<double,int>
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

#define pb push_back
#define maxn 210
#define max3(a,b,c) max(max(a,b),c)
#define mod 754754

#define put PutInt
#define send Send
#define get GetInt
#define receive Receive

typedef long long ll;
using namespace std;

double dp[maxn][maxn];
double p[maxn];
double at[maxn];

#define last fousbf

int last[maxn][maxn];
int cur;

int k;

double get(int pos,int win){

	if(last[pos][win] == cur)
		return dp[pos][win];

	last[pos][win] = cur;

	double ret;

	if(pos == k){
		if(win == 0)
			ret = 1;
		else
			ret = 0;
		//debug("!dp %d %d = %lf\n",pos,win,ret);
		return dp[pos][win] = ret;;
	}


	if(win == 0)
		ret = dp[pos][win] = (1.0-at[pos]) * get(pos+1,win);
	else
		ret = dp[pos][win] = (1.0-at[pos]) * get(pos+1,win) + at[pos] * get(pos+1,win-1);

	//debug("dp %d %d = %lf\n",pos,win,ret);
	return ret;
}

main(){

	int nt;
	scanf("%d",&nt);

	for(int t=1;t<=nt;t++){

		int n;
		scanf("%d%d",&n,&k);

		for(int i=0;i<n;i++)
			cin >> p[i];

		sort(p,p+n);

		double ans = 0;

		for(int i=-1;i<k;i++){

			cur++;
			for(int j=0;j<=i;j++)
				at[j] = p[j];
			int u = n-1;
			for(int j=i+1;j<k;j++){
				at[j] = p[u];
				u--;
			}
			sort(at,at+k);
			//for(int j=0;j<k;j++)
				//debug("%lf ",at[j]);
			//debug("\n");
			ans = max(ans, get(0,k/2));

		}

		printf("Case #%d: %.10lf\n",t,ans);

	}

}
