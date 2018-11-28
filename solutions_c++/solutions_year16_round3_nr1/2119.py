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
#define U unsigned int
#define LU long unsigned
#define LLU long long unsigned

int main() {
  // Declare members
  int num_case;
  cin >> num_case;
  
  int N;
  
  for (int nc = 1; nc <= num_case; ++nc) {
    // Init members
    cin >> N;
    vector<int> P(N);
    
    int sum = 0;
    for (int i = 0; i < N; ++i) {
      cin >> P[i];
      sum += P[i];
    }


    cout << "Case #" << nc << ":";
    if (N > 2) {
      while ((N > 2 && sum > 2)) {
        int max = -1;
        int ind = -1;
        for (int i = 0; i < N; ++i) {
          if (P[i] >= max) {
            max = P[i];
            ind = i;
          }
        }
        char temp = 'A' + ind;
        cout << " " << temp;
        P[ind]--;
        sum--;
      }
      cout << " AB";
    }
    
    if (N == 2) {
      while (sum > 0) {
        cout << " AB";
        sum -= 2;
      }
    }
    cout << endl;
    // Print output for case j
  }


  return 0;
}
