#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <sstream>
#include <numeric>
#include <bitset>
#define REP(i, a, b) for ( int i = int(a); i <= int(b); i++ )
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define all(a) (a).begin(), (a).end()
#define for_each(it, X) for (__typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)
#define DFS_WHITE -1
#define DFS_BLACK 1
#define MAXN 10010
using namespace std;

unsigned long long int A, B, K;
int T;

int main()
{
    scanf("%d", &T);
    REP(tt, 1, T) {
    	scanf("%llu", &A);
    	scanf("%llu", &B);
    	scanf("%llu", &K);
    	unsigned long long int cnt = 0, n;
    	REP(i, 0, A-1) REP(j, 0, B-1) {
    		n = (i&j);
    		if(n >= 0 && n < K) {
    			cnt++;
    		}
    	}
    	printf("Case #%d: %llu\n", tt, cnt);
    }
    return 0;
}
