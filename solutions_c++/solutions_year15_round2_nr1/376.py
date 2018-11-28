#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<math.h>
#include<queue>
#include<stack>
#include<sstream>
#include<stdio.h>
#include<map>
#include<set>
#include<memory.h>
#include<algorithm>
#include<vector>
using namespace std;
typedef long long ll;
ll gcd(ll a, ll b){
	if (!b)
		return a;
	return gcd(b, a%b);
}
ll lcm(ll a, ll b){
	return b / gcd(a, b)*a;
}
#define FOR(I,N) for(int(i)=0;i<int(N);++i)
#define FORK(I,N,K) for(int(i)=0;i<int(N);i+=int(K))


int oo = 1000001;
int dp[1000005];
int rev(int x){
	int ret = 0;
	while (x){
		ret = ret * 10 + x % 10;
		x /= 10;
	}
	return ret;
}
void BFS(){
	memset(dp, -1, sizeof(dp));
	queue<int>q;
	q.push(1);
	dp[1] = 1;
	while (q.size()){
		int r = q.front(); q.pop();
		if (r + 1 <= oo && dp[r + 1] == -1){
			dp[r + 1] = dp[r] + 1;
			q.push(r + 1);
		}
		int e = rev(r);
		if (e <= oo && dp[e] == -1){
			dp[e] = dp[r] + 1;
			q.push(e);
		}
	}
}
int main(){
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, n;
	BFS();
	cin >> t;
	FOR(0, t){
		cin >> n;
		printf("Case #%d: %d\n", i + 1, dp[n]);
	}
}