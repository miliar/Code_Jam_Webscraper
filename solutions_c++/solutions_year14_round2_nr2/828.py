#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <string.h>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define REP(it,v,cont) for(cont::iterator (it)=(v).begin();(it)!=(v).end();++(it)) 
#define FR(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int (i)=(c);(i)<(n);(i)++)
#define MOD 1000003 
#define INF 1000000000
typedef long long  ll;
typedef unsigned long long  ull;
typedef pair<int,int> pii;

int main()
{
	// freopen("input.txt", "r", stdin);
	
	int test;
	int A, B, K;
	
	cin >> test;
	for(int cas = 1; cas <= test; cas ++)
	{
		cin >> A >> B >> K;
		int res = 0;
		for(int i = 0; i < A; i ++)
			for(int j = 0; j < B; j ++)
				if( (i & j) < K )
					res ++;
		
		printf("Case #%d: %d\n", cas, res);
	}
	
	return 0;
}














