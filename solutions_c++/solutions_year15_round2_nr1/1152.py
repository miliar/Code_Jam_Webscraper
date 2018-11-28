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
#define N 10000000
ll *dp;
map<ll, bool> used;

ll rev(ll A){
	ll B = 0;
	while(A){
		B *= 10;
		B += A%10;
		A /= 10;
	}
	return B;
}

void calc(){
	queue<ll> q;
	q.push(1);
	while(!q.empty()){
		ll a = q.front(); q.pop();
		ll b = rev(a);
		if(b<N && dp[b]<0){
			dp[b] = dp[a]+1;
			q.push(b);
		}
		b = a+1;
		if(b<N && dp[b]<0){
			dp[b] = dp[a]+1;
			q.push(b);
		}
	}
}

ll solve(ll A){
	ll res = 0;
	queue<ll> q;
	q.push(A);
	while(!q.empty()){
		ll a = q.front(); q.pop();
		if(a<N) return dp[a];
		ll b = rev(a);
		if(a%10 && !used[b]){
			used[b] = true;
			q.push(b);
		}
		b = a-1;
		if(!used[b]){
			used[b] = true;
			q.push(b);
		}
	}
	return INF;
}

int main(){
	dp = (ll*)malloc(N*sizeof(ll));
	memset(dp, -1, N*sizeof(ll));
	dp[0] = INF;
	dp[1] = 1;
	calc();
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		used.clear();
		ll A;
		cin>>A;
		printf("Case #%d: %lld\n", Case, solve(A));
	}
	free(dp);
	return 0;
}

