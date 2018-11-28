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
  int N, y, z;
  //double e = 0.000001;

  for (int nc = 1; nc <= num_case; ++nc) {
    // Init members
    y = 0;
    z = 0;
    cin >> N;
    double naomi[N];
    double ken[N];
    
    for (int i = 0; i < N; ++i) {
      cin >> naomi[i];
    }
    
    for (int i = 0; i < N; ++i) {
      cin >> ken[i];
    }
    
    std::sort(naomi, naomi + N);
    std::sort(ken, ken + N);
    
    //for (int i = 0; i < N; ++i) {
    //  cout << naomi[i] << " " << ken[i] << endl;
    //}
    
    int i = 0;
    int j = 0;

    while (i < N) {
      while (j < N && ken[j] < naomi[i]) {
        ++j;
      }
      if (j == N) {
        z = N - i;
        break;
      }
      ++i;
      ++j;
    }
    
    i = 0;
    j = 0;
    
    while (i < N) {
      if (naomi[i] > ken[j]) {
        ++y;
        ++i;
        ++j;
      } else {
        ++i;
      }
    }
    
    
    // Print output for case j
    cout << "Case #" << nc << ": " << y << " " << z << endl;
  }


  return 0;
}
