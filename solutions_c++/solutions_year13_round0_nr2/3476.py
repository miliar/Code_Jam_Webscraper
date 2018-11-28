#include <iostream>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <map>
#include <vector>
#include <set>


using namespace std;

#define PI acos(-1.)
#define EPS 1e-7
#define LL long long
#define UI unsigned int
#define SPC << " " <<


int main() {
  // Declare members
  int num_case;
  cin >> num_case;

  vector<int> minr, maxr, minc, maxc;
  int N, M;
  int val;
  bool result = true;
  for (int nc = 1; nc <= num_case; ++nc) {
    // Init members
    cin >> N; cin >> M;
    //minr.resize(N, 101);
    maxr.clear();
    maxr.resize(N, -1);
    //minc.resize(M, 101);
    maxc.clear();
    maxc.resize(M, -1);
    result = true;
    int lawn[N][M];

    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < M; ++j) {
        cin >> val;
        lawn[i][j] = val;
//        if (val < minr[i]) minr[i] = val;
//        if (val < minc[j]) minc[j] = val;
        if (val > maxr[i]) maxr[i] = val;
        if (val > maxc[j]) maxc[j] = val;
      }
    }


    for (int i = 0; i < N && result; ++i) {
      for (int j = 0; j < M && result; ++j) {
        if (lawn[i][j] < maxr[i] && lawn[i][j] < maxc[j]) {
          result = false;
        }
      }
    }

    // Print output for case j
    cout << "Case #" << nc << ": " << (result?"YES":"NO") << endl;
  }


  return 0;
}
