//Pham Huu Canh
//Problem D. Ominous Omino
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

#define fii "d.inp"
#define foo "d.out"
#define MOD 1000000007

using namespace std;

typedef pair<int, int> II;
typedef vector<int> VI;

void input()
{
	int itest, ntest;
	int x, r, c;
	
	scanf("%d", &ntest);
	repi(itest, 1, ntest){
		scanf("%d %d %d", &x, &r, &c);
		if (r > c)	swap(r, c);
		if (x == 1)	printf("Case #%d: GABRIEL\n", itest);
		else if (x == 2){
			if ((r * c)&1)	printf("Case #%d: RICHARD\n", itest);
			else printf("Case #%d: GABRIEL\n", itest);
		}
		else if (x == 3){
			if (r == 1)	printf("Case #%d: RICHARD\n", itest);
			else if (r == 2){
				if (c == 2 || c == 4)	printf("Case #%d: RICHARD\n", itest);
				else printf("Case #%d: GABRIEL\n", itest);
			}
			else if (r == 3)	printf("Case #%d: GABRIEL\n", itest);
			else printf("Case #%d: RICHARD\n", itest);
		}
		else{
			if (r == 1 || r == 2)	printf("Case #%d: RICHARD\n", itest);
			else if (r == 3){
				if (c == 3)	printf("Case #%d: RICHARD\n", itest);
				else printf("Case #%d: GABRIEL\n", itest);
			}
			else printf("Case #%d: GABRIEL\n", itest);
		}
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



