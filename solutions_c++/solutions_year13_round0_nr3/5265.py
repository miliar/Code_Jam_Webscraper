/*
Author : SRIRAM S
*/
// Libs 
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,A,n) for(i=A;i<n;i++)
#define sz(c) (signed int) c.size()
#define pb(c) push_back(c)
#define INF (int) 1e9
#define all(c) c.begin(),c.end()
#define GI(t) scanf("%d",&t)
#define VI vector<int>
#define PII pair <int,int>
typedef long long LL;

using namespace std;

bool checkPalin(int N);

int main() {
	int t;
	GI(t);
	REP(i,t) {
		int A,B;
		GI(A);GI(B);
		int start = sqrt(A);
		if(start*start <A) start++;
		int ans = 0;
		for(int j=start;j*j<=B;j++) {
			if(checkPalin(j) && checkPalin(j*j)) ans++;
		}
		printf("Case #%d: %d\n",i+1,ans);
	}	
}

bool checkPalin(int N) {
	string s = "";
	while(N>0) {
		s.pb(N%10+'0');
		N /= 10;
	}
	int n = sz(s);
	for(int i=0;i<n;i++) if(s[i]!=s[n-i-1]) return false;
	return true;
}
