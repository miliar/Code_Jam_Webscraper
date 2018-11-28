#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#define ST first
#define ND second
#define MP(a,b) make_pair(a,b)
#define FOR(i,m,n) for(long long i=(long long)(m);i<(long long)(n);++i)
#define REP(i,n) for(long long i=0;i<(long long)(n);++i)
#define DREP(i,n) for(int i=(long long)(n)-1;i>=0;--i)
#define SGN(x) (x<0?-1:(x>0?1:0))
#define ABS(x) (x<0?-x:x)

using namespace std;


void test(int t) {
	cout << "Case #" << t+1 << ": ";
	long long N, m[11111], x=0,y=0, max=0;
	cin >> N;
	REP (i, N) {
		cin >> m[i];
		if (i==0) continue;
		if (m[i-1]>m[i]) x+= m[i-1]-m[i];
		if (max<m[i-1]-m[i]) max = m[i-1]-m[i];
	}
	REP (i, N-1) {
		if (m[i] > max) y+= max;
		else y+= m[i];
	}
	
	cout << x << " " << y << /*": " << max<<*/ endl;
}


int main() {
	int T; cin >> T;
	REP (i, T) 
		test(i);

	return 0;
}

















