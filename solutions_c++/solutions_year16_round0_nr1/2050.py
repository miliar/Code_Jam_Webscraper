#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <cmath>
#include <stack>
#include <queue>
#include <exception>
#include <numeric>

using namespace std;

typedef long long lo;
typedef vector< vector<long long> > vvl;
typedef vector< long long> vl;
typedef pair<lo, lo> ll;
typedef vector< ll > vll;
typedef vector< vll > vvll;
typedef pair<long, pair<long, long>> lll;
typedef vector<lll> vlll;
typedef vector<vvl> vvvl;
typedef vector<set<long>> vs;

void addDigits(set<lo>& seen, lo x){
	do seen.insert(x%10);
	while (x/=10);
}

void solve(lo n){
	if (n==0){
		printf("INSOMNIA\n");
		return;
	}
	lo c=0;
	set<lo> seen;
	while (seen.size()<10)
		addDigits(seen, c+=n);
	printf("%I64d\n", c);
}
int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	lo t, n;
	scanf("%I64d", &t);
	for (lo i=0;i<t;i++){
		scanf("%I64d", &n);
		printf("Case #%I64d: ", i+1);
		solve(n);
	}
	return 0;
}