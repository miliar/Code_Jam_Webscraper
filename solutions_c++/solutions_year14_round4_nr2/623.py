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

int v[1000];
int n;

void solve(int test) {
  int i, j, k;
  int start, end;
  
  cin >> n;
  for(i=0; i<n; i++) cin >> v[i];
  
  int tot = 0;
  
  start = 0;
  end = n-1;
  for(i=0; i<n; i++) {
    int maxi = INT_MAX;
    int maxipos = -1;
    for(j=start; j<=end; j++) {
      if(v[j] < maxi) {
        maxi = v[j];
        maxipos = j;
      }
    }
    
    // cout << maxi << endl;
    
    if(maxipos-start < end-maxipos) {
      for(j=maxipos; j>start; j--) {
        v[j] = v[j-1];
        tot++;
      }
      v[start] = maxi;
      start++;
    } else {
      for(j=maxipos; j<end; j++) {
        v[j] = v[j+1];
        tot++;
      }
      v[end] = maxi;
      end--;
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

