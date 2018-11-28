

#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[]) {
  int numtests = 0;
  cin >> numtests;
  for (int i = 0; i < numtests; ++i) {
    int smax = 0; string s;
    cin >> smax >> s;
    int n = 0, running_sum = 0;
    for (int j = 0; j <= smax; ++j) {
      //cout << "rsum:" << running_sum << " j:" << j << endl;
      if (running_sum < j) {
        n += (j - running_sum);
	running_sum = j;
      }
      running_sum += (s.at(j) - '0');
    }
    cout << "Case #" << i+1 << ": " << n << endl;
  }
  return 0;
}

