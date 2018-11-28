/* Opgave: B */
// 7+8+7=22 includes
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>
#include <cassert>

#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <string>

#include <iostream>
#include <sstream>
#include <utility>
#include <functional>
#include <limits>
#include <numeric>
#include <algorithm>

using namespace std;
/*void slowdoit(int N, int P) {
  vector<bool> guarantueed(1 << N, true);
  vector<bool> possible(1 << N);
  vector<int> l(1 << N);
  for(int i = 0; i < l.size(); ++i)
    l[i] = i;
  do {
    vector<pair<int, int> > ll;
    for(int i = 0; i < l.size(); ++i)
      ll.push_back(make_pair(0, i));
    for(int i = 0; i < N; ++i) {
      for(unsigned j = 0; j < l.size(); j += 2) {
	if(l[ll[j].second] < l[ll[j+1].second]) {
	  ll[j].first = ll[j].first * 2;
	  ll[j+1].first = ll[j+1].first * 2 + 1;
	} else {
	  ll[j].first = ll[j].first * 2 + 1;
	  ll[j+1].first = ll[j+1].first * 2;
	}
      }
      sort(ll.begin(), ll.end());
    }
    for(int i = 0; i < ll.size(); ++i)
      if(i < P)
	possible[l[ll[i].second]] = true;
      else
	guarantueed[l[ll[i].second]] = false;
  } while(next_permutation(l.begin(), l.end()));
  int a = -1;
  int b = -1;
  for(int i = 0; i < l.size(); ++i) {
    if(possible[i]) b = i;
    if(guarantueed[i]) a = i;
  }
  cout << a << " " << b << endl;
  }*/
void doit (int t) {
  unsigned long long N,P;
  cin >> N >> P;
  // slowdoit(N,P);
  unsigned long long count = 1ull << N;
  unsigned long long last = 0;
  for(int i = 0; i <= N; ++i) {
    unsigned long long r = ((1ull << (N-i))-1) + 1;
    if(r <= P) {
      last = count - (1ull << i);
      break;
    }
  }

  unsigned long long first = count - 1;
  for(int i = 0; i <= N; ++i) {
    unsigned long long r = (((1ull << (N-i)) - 1) ^ (count - 1)) + 1;
    //cout << i << " loses " << r << endl;
    if(r > P) {
      first = (1ull << i) - 2;
      break;
    }
  }
  cout << "Case #" << t <<": " << first << " " << last << endl;
}



int main () {
	int t;
	cin >> t; //scanf ("%d ", &t);
	for (int i = 0; i < t; i++) {
		doit (i+1);
	}
	return 0;
}
/* Opgave: B */
