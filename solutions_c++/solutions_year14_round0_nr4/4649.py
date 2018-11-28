#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <utility>
#include <vector>
#include <map>
#include <set>

#define REP(a,b) for (int a = 0; a < b; a++)
#define FOR(a,b,c) for (int a = b; a <= c; a++)
#define RESET(a,b) memset(a,b,sizeof a)

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define PII pair<int,int>
#define INF 2123123123

#define LL long long
using namespace std;

int T;
int aa[1001],bb[1001];
int dp[1<<10][1<<10];
int N;

int normal(){
	set<int> him;
	him.clear();
	REP(i,N){
		him.insert(bb[i]);
	}	
	
	int ret = 0;
	REP(i,N){
		set<int>::iterator it = him.upper_bound(aa[i]);
		if (it == him.end()){
			// buang
			him.erase(him.begin());
			ret++;
		}else{
			him.erase(it);
		}
	}
	
	return ret;
}	

int rek(int a, int b){
	if ((a == N) || (b == N)){
		return 0;
	}else if (dp[a][b] != -1){
		return dp[a][b];
	}else{
		dp[a][b] = max(rek(a+1,b), rek(a,b+1));
		if (aa[a] > bb[b]){
			dp[a][b] = max(dp[a][b], 1 + rek(a+1, b+1));
		}
		return dp[a][b];
	}
}

int main(){		
	scanf("%d", &T);
	REP(jt,T){
		scanf("%d", &N);
		REP(i,N){
			double a;
			scanf("%lf", &a);
			aa[i] = (int)(a * 1000000);
		}	
		REP(i,N){
			double a;
			scanf("%lf", &a);
			bb[i] = (int)(a * 1000000);
		}	
	
		sort(aa, aa + N);
		sort(bb, bb + N);	
			
		RESET(dp,-1);
		printf("Case #%d: %d %d\n", jt+1, rek(0,0), normal());
	}
	return 0;
}
