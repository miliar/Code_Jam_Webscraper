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

long long t, p, q, ans;

set<long long> potencias;
set<long long>::iterator itr;

int main() {
	
	for (p=0; p<55; p++)
		potencias.insert(2<<p);
	
	scanf("%lld", &t);
	
	for (int it=1; it<=t; it++) {
		
		scanf("%lld/%lld", &p, &q);
		
		itr = potencias.find(q);
		if ((itr != potencias.end()) && (p % 2 == 1)) {
			ans = 1;
			while (p < (q>>1)) {
				q >>= 1;
				ans++;
			}
		} else ans = -1;
		
		if (ans != -1) cout<<"Case #"<<it<<": "<<ans<<endl;
		else cout<<"Case #"<<it<<": impossible"<<endl;
		
	}
	
	return 0;
} 