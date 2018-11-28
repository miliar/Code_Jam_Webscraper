#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t=1; t<=T; t++) {
    int N; 
    double V, X;
    cin >> N >> V >> X;
    vector<double> R(N), C(N);
    for (int i=0; i<N; i++) 
      cin >> R[i] >> C[i];
    double minC = C[0], maxC = C[0];
    for (int i=1; i<N; i++)
      minC = min(minC,C[i]), maxC = max(maxC, C[i]);
    if (X<minC || X >maxC) 
      cout << "Case #" << t << ": IMPOSSIBLE" << endl;
    else {
      double answer = -1.0; 
      // only N=2
      if (N==1) answer = V / R[0];
      if (N==2) {
	if (C[0] == C[1]) answer = V / (R[0] + R[1]);
	else {
	  double alpha = (X - C[1]) / ( C[0] - C[1]);
	  answer = max ( alpha * V / R[0], (1-alpha) * V / R[1]);
	};
      };
      cout << setprecision(10) << "Case #" << t << ": " << answer << endl;
    }
  };
  return 0;
};
