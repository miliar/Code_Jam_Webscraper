#include <iostream>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <tuple>
#include <list>
#include <iomanip>

#define FOR(i, n) for(long i = 0; i < n; ++i)

using namespace std;

float A[1000];
float B[1000];

pair<long, long> solve(){
  long n; cin >> n;
  FOR(i, n) cin >> A[i];
  FOR(i, n) cin >> B[i];

  long y = 0;
  long z = 0;
  long la = 0, lb = 0, hb = n-1;
  long lz = 0;
  sort(A, A + n);
  sort(B, B + n);
  FOR(i, n){
    // y
    if(A[la] < B[lb]){
      hb -= 1;
    }else{
      y += 1;
      lb += 1;
    }

    // z
    while(lz < n && A[la] > B[lz]){
      lz += 1;
    }
    if(lz != n){
      lz += 1;
    }else{
      z += 1;
    }

    // inc
    la += 1;
  }

  return make_pair(y, z);
}

int main(int, char**){
  ios_base::sync_with_stdio(false);
  long ts; cin >> ts;
  FOR(t, ts){
    auto solution = solve();
    cout << "Case #" << t+1 << ": " << solution.first << " " << solution.second << endl;
  }
  return 0;
}