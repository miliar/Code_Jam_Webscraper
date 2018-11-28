//
//  15b.cpp
//  
//
//  Created by Ritish Goyal on 11/04/15.
//
//

#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

#define rep(i, n) for(int i=0; i<n; i++)

int maxi;

int maxe(vector<int> a) {
  maxi = 0;
  int ma = a[0];
  rep(i, a.size()) {
    if(a[i] > ma) {
      ma = a[i];
      maxi = i;
    }
  }
  return ma;
}

int opt(vector<int> a) {
  int m = maxe(a);
  if(m <= 3) {
    return m;
  }
  else if(m == 9) {
    vector<int> b;
    rep(i, a.size()) {
      b.push_back(a[i]);
    }
    rep(i, a.size()) {
      a[i] -= 1;
    }
    m -= 1;
    a[maxi] = a[maxi]/2;
    a.push_back(m/2);
    b[maxi] = b[maxi]/3;
    b.push_back(6);
    return min(1+opt(b), min(m+1, 2+opt(a)));
  }
  else if(m%2 != 0) {
    rep(i, a.size()) {
      a[i] -= 1;
    }
    m -= 1;
    a[maxi] = a[maxi]/2;
    a.push_back(m/2);
    return min(m+1, 2+opt(a));
  }
  else {
    a[maxi] = a[maxi]/2;
    a.push_back(m/2);
    return min(m, 1+opt(a));
  }
} 

int main() {
    int test; cin>> test;
    rep(z, test) {
      int ans;
      int d; cin>>d;
      vector<int> a(d);
      rep(i, d) {
	cin>>a[i];
      }
      ans = opt(a);
      printf("Case #%d: %d\n", z+1, ans);
    }
}
