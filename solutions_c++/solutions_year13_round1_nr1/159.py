#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <utility>
#include <algorithm>
#include <cmath>
#include <map>
#include <cctype>
#include <climits>
#include <cassert>
#include <sstream>
using namespace std;

#define MOD 1000000007

#define all(C) (C).begin(),(C).end()
#define tr(C, it) for(typeof((C).begin()) it = (C).begin(); it != (C).end(); it++)

 #define present(c,x) ((c).find(x) != (c).end()) 
 #define cpresent(c,x) (find(all(c),x) != (c).end()) 

typedef long long LL;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;

bool compare(int a, int b) {
	return a > b;
}
LL r,t;

bool check(LL n) {
	return (n*(2*r + 2*n - 1) <= t);
}

LL process() {
	cin>>r>>t;
	LL ll = 1, rr = 10000000000000000LL;
	//cout<<rr<<" testing\n";
	LL mid;
	
	//while (ll <= rr) {
	//	mid = (ll+rr)/2;
	//	cout<<mid<<" testing\n";
		
	while (check(ll)) {
		ll *= 2;
		//cout<<ll<<endl;
		if (ll == 0) return 0;
	}
	
	
	
	ll /= 2;
	rr = ll;
	//cout<<"step "<<ll<<endl;
	
	while (rr > 0) {
		if (check(ll + rr)) {
			ll += rr;
		}
		rr /= 2;
	}
	
	
	return ll;
}

int main() {
  int i, t=1;
  cin >>t;
  for (i = 0; i <t; i++) {
    LL x = process();
	cout<<"Case #"<<i+1<<": "<<x<<endl;
	assert (x != 0);
		
  }
}
