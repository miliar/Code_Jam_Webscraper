#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <list>
#include <set>
#include <algorithm>
#include <climits>
#include <cmath>
#include <string>
using namespace std;

int v[10000];
int n, x;

void solve(int test) {
  int i, j;
  
  cin >> n >> x;
  for(i=0; i<n; i++) cin >> v[i];
  
  sort(v, v+n);
  
  int tot = 0;
  
  i=0, j=n-1;
  while(i <= j) {
    if(i==j) {
      tot++;
      break;
    }
    
    if(v[i]+v[j] > x) {
      tot++;
      j--;
    } else {
      tot++;
      i++;
      j--;
    }
  }

  cout << "Case #" << (test+1) << ": " << tot << endl;
}


int main() {
  int t, T;
  cin >> T;
  for(t=0; t<T; t++) solve(t);
  return 0;
}

