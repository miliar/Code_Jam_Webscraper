#include <deque>
#include <queue>
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
#include <set>
#include <cstdlib>
#include <hash_map>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;

#define rep(i,s,e) for(int i=s;i<e;i++)
#define sz(X) ((int)(X.size()))
#define tr(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define all(x) x.begin(),x.end()
#define clr(x,c) memset(x,c,sizeof(x))
//---------------------------------------------------------------



LL badest(LL N, LL R) {
	if(R == 1) return 1;
	return N/2 + badest(N/2, (R-2)/2 + 1);
}
LL best(LL N, LL R) {
	if(R==N) return N;
	return best(N/2, N/2 - (N-R-1)/2);
}


LL get_sure(LL N, LL P){
	LL a1 = 1, a2 = N;
	if(badest(N, a2) <= P) return a2;
	while(a1+1 < a2){
		LL mid = (a1+a2)/2;
		if(badest(N, mid) <= P){
			a1 = mid;
		} else {
			a2 = mid;
		}
	}
	return a1;
}
LL get_largest(LL N, LL P){
	LL a1 = 1, a2 = N;
	if(best(N, a2) <= P) return a2;
	while(a1+1 < a2){
		LL mid = (a1+a2)/2;
		if(best(N, mid) <= P)
			a1 = mid;
		else 
			a2 = mid;
	}
	return a1;
}

int main() {
	freopen("F:/TDDOWNLOAD/B-large.in", "r", stdin);
	freopen("F:/TDDOWNLOAD/B-large.out", "w", stdout);

	int T;
	cin>>T;
	rep(te, 1, T+1) {
		LL n, P;
		cin>>n>>P;

		printf("Case #%d: %lld %lld\n", te, get_sure(1LL<<n, P)-1, get_largest(1LL<<n, P)-1);
	}
}