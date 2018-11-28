// Lupus Nocawy 2016
// Code Jam 2016
// https://code.google.com/codejam
// https://code.google.com/codejam/contest/6254486/dashboard
// Problem B. Revenge of the Pancakes

#include <cstdio>
#include <iostream>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <cmath>
using namespace std;
#define REP(i,n) for(int i=0, _n=n; i<_n; ++i)
#define FOR(i,a,b) for(int i=(a), _b=(b); i<=_b; ++i)
#define FORD(i,a,b) for(int i=(a), _b=(b); i>=_b; --i)
#define IT(i,x) __typeof__(x) i=x
#define FOREACH(it,x) for(__typeof__((x).begin()) it=(x).begin(); it!=(x).end(); ++it)
#define ALL(x) x.begin(),x.end()
#define MP make_pair
#define PB push_back
#define DEBUG(x) if(debug) cout << x << endl;
typedef long long int lli;
typedef unsigned long long int llu;
typedef pair<int,int> pii;
const int debug=0;

const int INF = 2147483647;
const int max_n = 2147483647;

char S[102];

int solve(int c){
	scanf("%s ", S);
	
	int l = strlen(S);
	int r = 0;
	
	for(int i=1; i<l; ++i){
		if(S[i-1]!=S[i])
			r++;
	}
	if(S[l-1]=='-')
		r++;
	
	return r;
}

int main(void){
	int t;
	scanf("%d ", &t);
	for(int c=1; c<=t; ++c)
		printf("Case #%d: %d\n", c, solve(c));
	return 0;
}
