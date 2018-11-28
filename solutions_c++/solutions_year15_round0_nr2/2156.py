//Pham Huu Canh
//Problem B. Infinite House of Pancakes
//Algorithm:
//Complexity:
//AC:

#include <iostream>
#include <fstream>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

#define max64 9223372036854775807LL
#define max32 2147483647
#define maxty 1001001001
#define max16 32767
#define EPS 1e-8
#define ll long long
#define ull unsigned long long
#define pb push_back
#define MP make_pair
#define PQ priority_queue
#define LB lower_bound
#define UB upper_bound
#define fi first
#define se second
#define timmax(x, y)    ((x) > (y) ? (x) : (y))
#define timmin(x, y)    ((x) < (y) ? (x) : (y))
#define fori(i, n)      for((i) = 0; (i) < (n); (i)++)
#define ford(i, n)      for((i) = (n-1); (i) >= 0; (i)--)
#define fore(i, v)		for(typeof(v.begin()) i = v.begin(); i != v.end(); i++)
#define repi(i, a, b)   for((i) = (a); (i) <= (b); (i)++)
#define repd(i, a, b)   for((i) = (a); (i) >= (b); (i)--)
#define all(tmpv)      tmpv.begin(), tmpv.end()

#define fii "b.inp"
#define foo "b.out"
#define MOD 1000000007

using namespace std;

typedef pair<int, int> II;
typedef vector<int> VI;

int n;
int a[1005];

int solve(int val){
	int cnt = 0, i;
	repi(i, 1, n)	if (a[i] > val)
		cnt += (a[i]-1) / val;
	return cnt;
}

void input()
{
	int itest, ntest, res, val, xmax, i;
	
	scanf("%d", &ntest);
	repi(itest, 1, ntest){
		scanf("%d", &n);
		xmax = 0;
		repi(i, 1, n)	scanf("%d", &a[i]), xmax = timmax(xmax, a[i]);
		
		res = maxty;
		repi(i, 1, xmax){
			val = solve(i) + i;
			res = timmin(res, val);
		}
		
		printf("Case #%d: %d\n", itest, res);
	}
}

int main()
{
    #ifndef ONLINE_JUDGE
    	freopen(fii,"r",stdin);
    	freopen(foo,"w",stdout);
    #endif

    input();

    return 0;
}



