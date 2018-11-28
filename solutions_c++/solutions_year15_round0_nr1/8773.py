#include <iostream>
#include <string>

using namespace std;

int main() {
  int test_cases;
  int num_people;
  string applause;

  cin >> test_cases;

  for (int i = 0; i < test_cases; ++i) {
    cin >> num_people;
    cin >> applause;
    int friends = 0;
    int clappers = 0;

    for (int j = 0; j < applause.size(); ++j) {
      clappers += applause[j] - '0';
      while (clappers < j + 1) {
        friends++;
        clappers++;
      }
    }
    cout << "Case #" << i + 1 << ": " << friends << endl;
  }

  return 0;
}