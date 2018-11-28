// Lupus Nocawy 2016
// Code Jam 2016
// https://code.google.com/codejam
// https://code.google.com/codejam/contest/6254486/dashboard
// Problem A. Counting Sheep

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
bool d[10];

bool sawAll(void){
  REP(i,10)
    if(d[i]==0) 
      return 0;
  return 1;
}

void solve(int c){
	int N;
	scanf("%d ", &N);

	if(N==0) {
    printf("Case #%d: INSOMNIA\n", c);
    return;
	}

	REP(i,10)
    d[i]=0;

	int i=0;
	do{
		++i;
		int x=i*N;
		//printf("%d\n", x);
		while (x>0){
			d[x%10]=1;
			x/=10;
		}
	} while(!sawAll());

	printf("Case #%d: %d\n", c, i*N);
	return;
}

int main(void){
	int t;
	scanf("%d ", &t);
	for(int c=1; c<=t; ++c)
		solve(c);
	return 0;
}
