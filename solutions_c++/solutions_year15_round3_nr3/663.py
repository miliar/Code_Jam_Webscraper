#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <sstream>
#include <functional>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <list>
#include <numeric>
using namespace std;
const double PI = 3.14159265358979323846;
const double EPS = 1e-12;
const int INF = 1<<25;
typedef pair<int,int> P;
typedef long long ll;
typedef unsigned long long ull;
#define N 100
int d[N], dp[N], dp2[N];

int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		memset(dp, 0, sizeof(dp));
		int C, D, V;
		cin>>C>>D>>V;
		for(int i = 0; i < D; i++) cin>>d[i];
		dp[0] = 1;
		for(int i = 0; i < D; i++){
			for(int j = V; j >= d[i]; j--){
				dp[j] |= dp[j-d[i]];
			}
		}
		int res = 0;
		/*
		for(int i = 1; i <= 2; i++){
			if(!dp[i]) res++;
			for(int j = V; j >= i; j--) dp[j] |= dp[j-i];
		}*/
		vector<int> v;
		for(int i = 1; i <= 16; i++) v.push_back(i);
		int m = v.size();
		int rr = INF;
		for(int i = 0; i < 1<<m; i++){
			memcpy(dp2, dp, sizeof(dp2));
			int r = __builtin_popcount(i);
			if(r>=rr) continue;
			for(int j = 0; j < m; j++){
				if((1&(i>>j))==0) continue;
				for(int k = V; k >= v[j]; k--){
					dp2[k] |= dp2[k-v[j]];
				}
			}
			bool ok = true;
			for(int j = 0; j <= V; j++){
				if(dp2[j]==0) ok = false;
			}
			if(ok) rr = r;
		}
		printf("Case #%d: %d\n", Case, res+rr);
	}
	return 0;
}

