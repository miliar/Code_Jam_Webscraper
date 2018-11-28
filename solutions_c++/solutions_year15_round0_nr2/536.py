#include <stdio.h>
#include <algorithm>
#include <assert.h>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <queue>
#include <cmath>
#include <ctime>
#include <climits>
#include <iomanip>
#include <sstream>
using namespace std;

typedef long long LL;
#define tr(container, it)for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (int i = (a); i < (int)(b); i++)

int GCD (int a, int b) { if (!a) return b; return GCD(b%a, a);}

int main() {
  clock_t startTime = clock();
  ios_base::sync_with_stdio(false);

  int t; cin>>t;
  for (int test = 1; test <= t; test++) {
  	cout<<"Case #"<<test<<": ";
  	int d; cin>>d;
  	std::vector<int> p;
  	REP(i, 0, d) {
  		int z; cin>>z;
  		p.push_back(z);
  	}
  	int mx = *max_element(p.begin(), p.end());
  	int ans = INT_MAX;
  	REP(eat, 1, mx + 1) {
  		int breaks = 0;
  		REP(i, 0, p.size()) {
  			if (p[i] > eat) {
  				breaks += max(p[i]/ eat - !(p[i] % eat), 1);
  			}
  		}
  		// cout<<eat<<" "<<breaks<<"\n";
  		ans = min(ans, breaks + eat);
  	}
  	cout<<ans<<"\n";
  }

  clock_t endTime = clock();
  cerr<<"\nTime:"<< double(endTime - startTime) / CLOCKS_PER_SEC <<" seconds\n" ;
  return 0;
}