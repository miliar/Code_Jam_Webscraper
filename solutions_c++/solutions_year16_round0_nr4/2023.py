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


void solve(lo k, lo c, lo s){
	vl unknown,ans;
	for (lo i=0;i<k;i++)
		unknown.push_back(i);
	for (lo i=0;i<s && !unknown.empty();i++){
		lo acc=0;
		for (lo j=0;j<c;j++){
			acc*=k;
			lo ind=0;
			if (!unknown.empty()) {
				ind=unknown.back();
				unknown.pop_back();
			}
			acc+=ind;
		}
		acc++;
		ans.push_back(acc);
	}
	if (!unknown.empty()) {
		printf("IMPOSSIBLE\n");
		return;
	}
	for (vl::iterator it=ans.begin();it!=ans.end();it++)
		printf("%I64d ", *it);
	printf("\n");
}
int main() {
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	lo t;
	scanf("%I64d", &t);
	for (lo i=0;i<t;i++){
		lo k, c, s;
		scanf("%I64d%I64d%I64d", &k, &c, &s);
		printf("Case #%I64d: ", i+1);
		solve(k, c, s);
	}
	return 0;
}