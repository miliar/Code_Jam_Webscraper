#include <iostream>
#include <string>

using namespace std;

void solve_test_case(int test_case_no) {
  int max_shyness = 0;
  string numbers;
  cin >> max_shyness >> numbers;
  int additional = 0;
  int clapping = 0;
  for (int i = 0; i <= max_shyness; ++i) {
    if (clapping < i) {
      additional += i - clapping;
      clapping = i;
    }
    clapping += numbers[i] - '0';
  }
  cout << "Case #" << test_case_no << ": " << additional << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  int numof_test_cases = 0;
  cin >> numof_test_cases;
  for (int i = 1; i <= numof_test_cases; ++i) {
    solve_test_case(i);
  }
}
