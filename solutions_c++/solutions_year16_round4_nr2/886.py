										/* in the name of Allah */
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <list>
#include <map>
#include <set>

using namespace std;

#define uint unsigned int
#define int64 long long
#define P pair<int, int>
#define Pss pair<string, string>
#define PLL pair<int64, int64>
#define Inf 1000000
#define Mod 1000000007LL

int n, m, k;
vector <double> p;
double in[210];
double dp[210][210];
bool mark[210][210];

double mem(int idx, int rem){
	if(rem < 0 || k - idx < rem)
		return 0;
	if(idx == k)
		return 1;
	
	if(mark[idx][rem])
		return dp[idx][rem];
	mark[idx][rem] = true;

	double v1 = p[idx] * mem(idx + 1, rem - 1);
	double v2 = (1 - p[idx]) * mem(idx + 1, rem);
	return dp[idx][rem] = v1 + v2;
}

int main(){
	freopen("B-Red Tape Committee.in", "r", stdin);
	freopen("B-Red Tape Committee.out", "w", stdout);
	int T, test = 0;
	for(cin >> T; T--; ){
		cin >> n >> k;
		for(int i = 0; i < n; i++)
			cin >> in[i];

		double res = 0;
		for(int mask = 0; mask < (1 << n); mask++){
			p.clear();
			for(int i = 0; i < n; i++)
				if(mask & (1 << i))
					p.push_back(in[i]);
			if(k != p.size())
				continue;

			memset(mark, false, sizeof mark);
			res = max(res, mem(0, k / 2));
		}
		cout << "Case #" << ++test << ": " << fixed << setprecision(6) << res << endl;
	}
	return 0;
}
