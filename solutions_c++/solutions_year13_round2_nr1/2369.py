#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int
solve(vector<long> mote, int b, int e, long A) {
  int result = 0;
  
  if(b <= e) {
    while((mote[b] < A) && (b <= e)) {
      A += mote[b];
      b++;
    }
    
    if(b <= e) {
      if((A-1) > 0) {
        result = 1+min(solve(mote, b, e, 2*A-1) , solve(mote, b, e-1, A));
      } else {
        result = 1+solve(mote, b, e-1, A);
      }
    }
  }
  
  return result;
}

int
main() {
  int T;
  
  cin >> T;
  
  for(int i = 1; i <= T; i++) {
    long A;
    int N;
    vector<long> mote;
    
    cin >> A >> N;
    
    for(int j = 0; j < N; j++) {
      long m;
      cin >> m;
      mote.push_back(m);
    }
    
    sort(mote.begin(), mote.end());
    cout << "Case #"<< i << ": " << solve(mote, 0, mote.size()-1, A) << endl;
  }
  
  return 0;
}
