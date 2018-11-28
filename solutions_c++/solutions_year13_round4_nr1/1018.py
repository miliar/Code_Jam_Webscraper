#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <complex>
#include <cstdio>
#include <vector>
#include <cctype>
#include <string>
#include <ctime>
#include <cmath>
#include <set>
#include <map>

typedef long double LD;
typedef long long LL;

using namespace std;

#define sz(A) (int)(A).size()
#define mp make_pair
#define pb push_back

const int N = int(1e7), MOD = int(1e9 + 2013);

LL n;
int m, o[N], p[N], e[N];

LL calc(int a) {
	LL dist = e[a] - o[a];
	return n * dist - dist * (dist - 1) / 2;
}

LL better(int a, int b) {
	LL cost = calc(a) + calc(b);
	swap(e[a], e[b]);
	LL cost2 = calc(a) + calc(b);
	swap(e[b], e[a]);
	return cost - cost2;
}

int main() {
	int t;
	cin >> t;

	for (int test = 0; test < t; test++) {			    	
		LL ans = 0;
    	cin >> n >> m;
    	for (int i = 0; i < m; i++) 
    		cin >> o[i] >> e[i] >> p[i];

		bool ch = 1;		
		while (ch) {
			ch = 0;			
    		for (int i = 0; i < m; i++)
    			for (int j = 0; j < m; j++) {
    				if (e[i] >= o[j] && e[i] <= e[j]) {
    					LL val = better(i, j);
    					if (val > 0) {
    						int p_min = min(p[i], p[j]), p_max = max(p[i], p[j]), e_mem, o_mem;											
    						if (p_max == p[i]) {
    							e_mem = e[i];
    							o_mem = o[i];
    						}
    						else {
    							e_mem = e[j];
    							o_mem = o[j];
    						}
    							
    						swap(e[i], e[j]);
    						p[i] = p[j] = p_min;

    						if (p_max != p_min) {
								p[m] = p_max - p_min;
								e[m] = e_mem;
								o[m] = o_mem;
								m++;
							}

    						ch = 1;    						
    						ans = (ans + (val % MOD) * p_min) % MOD;
    					}
    				}				
    			}
		}

    	printf("Case #%d: %I64d\n", test + 1, ans);
	}

	return 0;
}
