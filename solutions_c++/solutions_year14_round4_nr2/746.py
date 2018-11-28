#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

typedef pair<int,int> pii;

pii vals[1010];
pii svals[1010];
int cpy[1010];
int ans;

void bsort(int start, int end) {
  for (int i=start+1; i<= end; ++i) {
    int x = i;
    while (x > start && cpy[x] < cpy[x-1]) {
      ++ans;
      swap(cpy[x], cpy[x-1]);
      --x;
    }
  }
}

void nbsort(int start, int end) {
  for (int i=start+1; i<= end; ++i) {
    int x = i;
    while (x > start && cpy[x] > cpy[x-1]) {
      ++ans;
      swap(cpy[x], cpy[x-1]);
      --x;
    }
  }
}


void solve() {
  int n;
  cin >> n;
  int mx = -1, mxi = -1;
  for (int i=0; i<n; ++i){
    int tmp;
    cin >> tmp;
    svals[i] = vals[i] = make_pair(tmp, i);
    
    if (vals[i].first > mx) {
      mx = vals[i].first;
      mxi = i;
    }
  }
  sort(svals, svals+n);
  int left = 0;
  int right = n-1;
  int ans = 0;
  for (int i=0; i<n; ++i) {
    int current = svals[i].first;
    for (int j=left; j<=right; ++j) {
      if (vals[j].first == current) {
	if (j - left < right -j) {
	  while (j != left) {
	    swap(vals[j], vals[j-1]);
	    --j;
	    ++ans;
	  }
	  ++left;
	} else {
	  while (j != right) {
	    swap(vals[j], vals[j+1]);
	    ++ans;
	    ++j;
	  }
	  --right;
	}
	break;
      }
    }
  }
  cout << ans << endl;
}

int main() {
  int c;
  cin >> c;
  for (int i=1; i<=c; ++i) {
    cout << "Case #" << i << ": ";
    solve();
  }
  return 0;
}

