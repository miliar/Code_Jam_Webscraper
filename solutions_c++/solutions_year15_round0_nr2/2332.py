#include <iostream>
#include <vector>

using namespace std;

const int maxP = 1000;

main () { 
  int T;
  cin >> T;
  for (int t=1; t<=T; t++) {
    int D;
    cin >> D;
    vector<int> P(D+maxP);
    for (int i=0; i<D; i++) cin >> P[i];
    int m = P[0];
    for (int i=1; i<D; i++)
      m = max(m, P[i]);
    int best = m;
    for (int eat=1; eat<=m; eat++) {
      int moves = 0;
      for (int i=0; i<D; i++) 
	moves += max(0,P[i]-1)/eat;
      best = min(best, moves+eat);
      //      for (int i=0; i<D; i++) cout << P[i] << " ";
      //      cout << " : " << best << endl;
    }
    cout << "Case #" << t << ": " << best << endl;
  };
};
