#include<vector>
#include<string>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<cstdio>
#include<iostream>
#include<sstream>
#include<cstring>
#include<cstdlib>
#define MOD
#define ADD(X,Y) ((X) = ((X) + (Y)%MOD) % MOD)
using namespace std;
typedef long long i64; typedef vector<int> ivec; typedef vector<string> svec;

int T, N;
char in[500];
double dp[1<<20];

double solve(int v)
{
	if(dp[v] != -1) return dp[v];

	if(dp[v] == -1){
		if(v == 0) return dp[v] = 0;
		
		int oc = 0;
		int cons = 0;
		for(int i=0;i<N;i++) if(v&(1<<i)){ //not occupied
			cons = 0;
		}else{
			oc++;
			cons++;
		}

		for(int i=0;i<N;i++) if(v&(1<<i)) solve(v ^ (1<<i));

		dp[v] = 0.0;
		for(int i=0;i<N;i++){
			if(v&(1<<i)){
				//printf("a%d %d ", i, cons);
				dp[v] += (N - cons / 2.0) * (cons+1) / (double)N;
				dp[v] += (cons+1) / (double)N * solve(v ^ (1<<i));
				//printf("%d %d ", i, cons);
				cons = 0;
			}else{
				cons++;
			}
		}
		//puts("");
	}
	
	return dp[v];
}

int main()
{
	scanf("%d", &T);

	for(int t=0;t++<T;){
		scanf("%s", in); N = strlen(in);

		for(int i=0;i<(1<<N);i++) dp[i] = -1;

		int v = 0;
		for(int i=0;i<N;i++) if(in[i] == '.') v |= 1<<i;

		double sol = solve(v);

		printf("Case #%d: %.10f\n", t, sol);
	}

	return 0;
}
