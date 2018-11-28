#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<algorithm>
#include<sstream>
#include<iomanip>
#include<cstring>
#include<bitset>
#include<fstream>
#include<cmath>
#include<cassert>
#include <stdio.h>
#include<ctype.h>
using namespace std ;
#define LL long long
int N,
	E,
	R;
int v[10];
int dp[11][5];
int rec(int i, int e)
{
	if(i == N)
		return 0;
	if(dp[i][e] != -1)
		return dp[i][e];
	int ans = 0;
	for(int t = 0; t <= e; ++t)
		ans = max(ans, rec(i + 1, min(E, e - t + R)) + v[i] * t);
	return dp[i][e] = ans;
}
int main()
{
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int T;
	cin >> T;
	for(int ti = 1; ti <= T; ++ti)
	{
		cin >> E >> R >> N;
		for(int i = 0; i < N; ++i)
			cin >> v[i];
		memset(dp, -1, sizeof dp);
		cout << "Case #" << ti << ": " << rec(0, E) << endl;
	}

}