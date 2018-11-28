#include <map>
#include <unordered_set>
#include <unordered_map>
#include <set>
#include <list>
#include <cmath>
#include <stack>
#include <queue>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <cstdlib>
#include <numeric>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <assert.h>
#include <functional>
using namespace std;
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define FOR(i,j,k) for(int (i)=(j);(i)<=(int)(k);++(i))
#define ll long long
#define ld long double
#define pii pair<int,int> 
#define mp make_pair

#define N 1001

char level[N];

int main(void) {
	int t, n;
	cin >> t;
	FOR(casenr, 1, t)
	{
		cin >> n >> level;
		int res = 0;
		int cnt = 0;
		rep(i,n+1)
		{
			res = max(res, i - cnt);
			cnt += level[i] - '0';
		}
		cout << "Case #" << casenr << ": " << res << endl;
	}
	
	return 0;
}