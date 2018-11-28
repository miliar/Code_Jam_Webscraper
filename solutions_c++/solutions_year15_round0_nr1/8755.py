#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
  int T;
  cin >> T;

  for ( int t = 1; t <= T; ++t ) {
    int S_max; // max shyness
    cin >> S_max;

    string S;
    cin >> S;
    // S[k] = number of people with shyness k

    vector<int> total_upto;
    // total_upto[k] = number of people with shyness <= k

    int people = 0;
    // total number of non-friends in the audience

    int friends = 0;
    // number of friends in the audience

    for ( int k = 0; k <= S_max; ++k ) {
      if ( (people + friends) >= S_max ) {
        break;
      }
      if ( ( people + friends ) < k ) {
        friends += k - (people + friends);
      }
      people += S[k] - '0';
    }

    cout << "Case #" << t << ": " << friends << '\n';
  }
  return 0;
}
