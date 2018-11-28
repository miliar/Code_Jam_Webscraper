// Lupus Nocawy 2016
// Google Code Jam 2016
// Round 1C 2016
// https://code.google.com/codejam
// https://code.google.com/codejam/contest/4314486/dashboard
// Problem Problem A. Senate Evacuation

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

struct classcomp {
  bool operator() (const pair<int,char> &A, const pair<int,char> &B) const {
	if(A.first == B.first)
		return A.second < B.second;
	else
		return A.first > B.first;
	}
};

//bool cmp (const pair<int,char> &A, const pair<int,char> &B){
//	if(A.first == B.first)
//		return A.second < B.second;
//	else
//		return A.first > B.first;
//}

void solve(int c){
	int N, sump=0;
	set<pair<int, char>, classcomp > S;
	scanf("%d ", &N);
	REP(i,N){
		int p;
		scanf("%d ", &p);
		sump += p;
		S.insert(MP(p,'A'+i));
	}
	
	//FOREACH(it, S){
	//	printf("(%d %c) ", it->first, it->second);
	//} printf("\n");
	
	while(S.size() > 0){
		int p;
		char c;
		bool do2 = false;

		if(S.size() == 2){
			if(S.begin()->first == (++(S.begin()))->first){
				do2 = true;
			}
		}

		p = S.begin()->first;
		c = S.begin()->second;
		printf("%c", c);
		S.erase(S.begin());
		if(p>1)
			S.insert(MP(p-1,c));

		if(do2){
			p = S.begin()->first;
			c = S.begin()->second;
			printf("%c", c);
			S.erase(S.begin());
			if(p>1)
				S.insert(MP(p-1,c));
		}
		
		printf(" ");
	}
	printf("\n");
	
	return;
}

int main(void){
	int t;
	scanf("%d ", &t);
	for(int c=1; c<=t; ++c){
		printf("Case #%d: ", c);
		solve(c);
	}
	return 0;
}
