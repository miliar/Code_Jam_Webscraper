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
  	int smax; cin>>smax;
  	string s; cin>>s;
  	int cur = s[0] - '0', add = 0;
  	REP(i, 1, s.size()) {
  		// cout<<cur<<" "<<i<<" "<<s[i]<<" | "<<add<<"\n";
  		if (s[i] == '0') continue;
  		if (cur < i) {
  			add += i - cur;
  			cur += i - cur;
  		}
  		cur += s[i] - '0';
  	}
  	cout<<add<<"\n";
  }

  clock_t endTime = clock();
  cerr<<"\nTime:"<< double(endTime - startTime) / CLOCKS_PER_SEC <<" seconds\n" ;
  return 0;
}