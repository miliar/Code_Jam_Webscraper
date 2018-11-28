#include <iostream>
using namespace std;

int main() {
  int cases = 0;
  cin >> cases;
  for (int k = 1; k <= cases; k++) {
    int shy = 0;
    cin >> shy;
    string counts = "";
    cin >> counts;
    int sum = 0, need = 0;
    for (int i = 0; i <= shy; i++) {
      if (sum < i) {
        need += i-sum;
        sum = i;
      }
      sum += counts[i]-'0';
    }
    cout << "Case #" << k<< ": " << need << endl;
  }
  return 0;
}
