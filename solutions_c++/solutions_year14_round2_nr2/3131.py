/*
	By: facug91
	From: 
	Name: 
	Number: 
*/

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <iterator>
#include <utility>
#include <list>
#include <stack>
#include <iomanip>
//#include <bitset>

#define MAX_INT 2147483647
#define MAX_LONG 9223372036854775807ll
#define MAX_ULONG 18446744073709551615ull
#define MAX_DBL 1.7976931348623158e+308
#define EPS 1e-9

#define INF 1000000000
//
using namespace std;

int t, a, b, k;

int main() {
	
	scanf("%d", &t);
	
	for (int ti=1; ti<=t; ti++) {
		
		scanf("%d %d %d", &a, &b, &k);
		
		int ans = 0;
		for (int ai=0; ai<a; ai++) {
			for (int bi=0; bi<b; bi++) {
				if ((ai&bi) < k) ans++;
			}
		}
		
		printf("Case #%d: %d\n", ti, ans);
		
	}
	
	return 0;
} 