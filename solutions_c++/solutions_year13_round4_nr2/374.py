#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>

using namespace std;

#define all(x) x.begin(),x.end()
#define bits(x) __builtin_popcount(x)
#define FOR(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)

int n;
long long N;
long long p;

long long best(long long val) {
		int w=0;
		long long pot=1;
		while ((pot*2)<=N-val) {
			pot*=2;
			w++;
		}
		return 1LL<<(n-w);
}

long long worst(long long val) {
	return N + 1 - best(N-1-val);
}

int main() {
	int casos;

	cin>>casos;
	for (int caso = 1; caso <= casos; caso++) {
		cin>>n>>p;
		N=1LL<<n;
		
		//for (int i=0;i<N;i++) cerr<<i<<": "<<best(i)<<" "<<worst(i)<<endl;
		long long left=0, right=N;
		while (left + 1< right) {
			long long med=(left+right)/2;
			
			if (best(med) <= p) left = med;
			else right = med;
		}
		long long sec = left;
		
		left=0, right=N;
		while (left + 1< right) {
			long long med=(left+right)/2;
			
			if (worst(med) <= p) left = med;
			else right = med;
		}
		
		cout << "Case #" << caso << ": " << left << " " << sec << endl;
	}
	return 0;
}
