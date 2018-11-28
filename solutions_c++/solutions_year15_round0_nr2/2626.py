//------------------------------------------------------------------------------
//  Problem : 
//  User    : 
//  Date    : 
//------------------------------------------------------------------------------


#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

int a[1111], b[1111];
int ans, ct, ta;
int n, T;

int main( int argc , char *argv[] )
{
	freopen("b3.in", "r", stdin);
	freopen("b2.out", "w", stdout);
	scanf("%d", &T);
	for(int testcase = 1; testcase <= T; testcase++) {
		scanf("%d", &n);
		memset(a, 0, sizeof(a));
		for(int i = 0; i < n; ++i) {
			int x;
			scanf("%d", &x);
			a[x]++;
		}
		ans = 100000;
		ct = 0;
		for(int i = 1000; i >= 1; --i)
		if(a[i] > 0) {
			ans = min(ans, ct+i);
			ct += a[i];
			a[i>>1] += a[i];
			a[(i+1)>>1] += a[i];
		}
		printf("Case #%d: %d\n", testcase, ans);
	}
			
			
		
			
	return 0;
}
