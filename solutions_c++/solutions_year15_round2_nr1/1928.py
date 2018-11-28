/*	In the name of God	*/
#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cctype>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include <sstream>
#include <bitset>
#include <map>
#include <set>
#include <queue>
#include <stack>

#define rep(i,n) for((i)=0;(i)<(n);(i)++)
typedef long long ll;

using namespace std;
char s[101];
int dp[10001 * 1001];
queue<pair<int,int> > q;
int rev(int x){
	sprintf(s, "%d", x);
	_strrev(s);
	sscanf(s, "%d", &x);
	return x;
}

int main(){
	int c, k, r, n;

	memset(dp, 63, sizeof dp);
	dp[1] = 1;
	for (int i = 1; i < 10000*1000; i++)
	{
		r = rev(i);
		dp[i + 1] = min(dp[i + 1], dp[i] + 1);
		if (r < 10000 * 1000 && dp[i] + 1 < dp[r]){
			dp[r] = dp[i] + 1;
			if (r < i)
				i = r - 1;
		}
	}
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("program1.out", "w", stdout);
	int tc;
	cin >> tc;
	for (int ti = 1; ti <= tc; ti++)
	{
		cin >> n;
		printf("Case #%d: %d\n", ti, dp[n]); 

		/*while (!q.empty())
			q.pop();
		cin >> n;
		q.push(make_pair(1,1));
		while (!q.empty()){
			pair<int, int> p = q.front();
			q.pop();
			k = p.first;
			if (k == n){
				printf("Case #%d: %d\n", ti, p.second);
				break;
			}
			r = rev(k);
			p.second++;
			q.push(make_pair(k + 1, p.second));
			if (r>k || k>n)
				q.push(make_pair(r, p.second));
		}*/
		/*c,k = 1,r;
		for (c = 1; k < n; c++)
		{
			r = rev(k);
			if (r <= n && r>k)
				k = r;
			else
				k++;
		}
		printf("Case #%d: %d\n", ti,c);*/
	}

	return 0;
}