#include <string>
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <cstdlib>
#include <cstring>
//#include "ttmath/ttmath.h"

using namespace std;

long long cost(long long n, long long d) {
  return (2*n-d+1)*d/2;
}

int main() {
  int T;
  cin >> T;
  for (int t=1;t<=T;t++) {
    long long N;
    long long ans=0;
    cin >> N;
    int M;
    cin >> M;
    vector<pair<long long,long long> > list;
    for (int i=0;i<M;i++) {
      long long o, e, p;
      cin >> o >> e >> p;
      list.push_back(make_pair(o,-p));
      list.push_back(make_pair(e,p));
      ans += cost(N,e-o)*p;
    }
    sort(list.begin(),list.end());
    vector<pair<long long,long long> > stk;
    for (int i=0;i<list.size();i++) {
      if (list[i].second<0) {
	stk.push_back(make_pair(list[i].first,-list[i].second));
      }
      else {
	long long num = list[i].second;
	while (num>0) {
	  int n = min(num,stk.rbegin()->second);
	  ans -= cost(N,list[i].first - stk.rbegin()->first)*n;
	  if ((stk.rbegin()->second-=n)==0) {
	    stk.pop_back();
	  }
	  num -= n;
	}
      }
    }

    printf("Case #%d: %lld\n", t, ans);
  }
  return 0;
}


