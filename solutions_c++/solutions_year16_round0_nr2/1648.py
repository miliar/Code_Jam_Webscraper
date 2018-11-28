//Pham Huu Canh
//
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
#define mp make_pair
#define PQ priority_queue
#define LB lower_bound
#define UB upper_bound
#define fi first
#define se second
#define timmax(x, y)    ((x) > (y) ? (x) : (y))
#define timmin(x, y)    ((x) < (y) ? (x) : (y))
#define fori(i, n)      for((i) = 0; (i) < (n); (i)++)
#define ford(i, n)      for((i) = (n-1); (i) >= 0; (i)--)
#define fore(i, v)      for(typeof(v.begin()) i = v.begin(); i != v.end(); i++)
#define repi(i, a, b)   for((i) = (a); (i) <= (b); (i)++)
#define repd(i, a, b)   for((i) = (a); (i) >= (b); (i)--)
#define all(tmpv)      tmpv.begin(), tmpv.end()

#define fii "b_large.inp"
#define foo "b_large.out"
#define MOD 1000000007
#define inf 1000111000111000111LL

using namespace std;

typedef pair<int, int> II;
typedef vector<int> VI;

char s[105];

int solve(int len, char c){
	if (len == 0)	return 0;
	if (len == 1)	return s[0] != c;
	if (s[len-1] == c)	return solve(len-1, c);
	char rc = (c == '+' ? '-' : '+');
	
	int lf = 0, i;
	fori(i, len)	
		if (s[i] == c)	break;
		else lf++;
	
	if (lf == 0)	return solve(len-1, rc) + 1;
	else{
		reverse(s, s + len);
		fori(i, len)	s[i] = (s[i] == '-' ? '+' : '-');
		return solve(len, c) + 1;
	}
}

void input(){
	int itest, ntest;
	
	scanf("%d", &ntest);
	repi(itest, 1, ntest){
		scanf("%s", &s);
		int len = strlen(s);
		printf("Case #%d: %d\n", itest, solve(len, '+'));
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

