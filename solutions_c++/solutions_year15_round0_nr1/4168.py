#include <cstdlib>
#include <string>
#include <iostream>
#include <set>

using namespace std;

#define SMAX 1001

int main() {
  // Number of cases.
  int N;
  cin >> N;
  int *shyness = new int[SMAX];

  // For each test case.
  for (int i=1; i<=N; i++) {
    int Smax;
    cin >> Smax;
    string shy;
    cin >> shy;
    for (int j=0; j<=Smax; j++) {
      shyness[j] = shy[j] - '0';
    }

    int over = 0;
    int count = 0;
    for (int j=0; j<=Smax; j++) {
      if (count < j) {
        over += j - count;
        count = j;
      }
      count += shyness[j];
    }

    cout << "Case #" << i << ": " << over << endl;
  }

  return 0;
}