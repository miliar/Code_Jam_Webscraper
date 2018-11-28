#include <iostream>
#include <string>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int cases;
  cin >>cases;
  for (int c = 0; c < cases; c++) {
    int max;
    string shyness;
    cin >> max >> shyness;
    int total = 0;
    int num_persons_to_add = 0;
    for (int i = 0; i < shyness.length(); i++) {
      if (i != 0 && total < i) {
        num_persons_to_add += (i - total);
        total += (i - total);
      }
      total += (shyness[i] - '0');
    }
    cout << "Case #" << (c + 1) << ": " << num_persons_to_add << endl;
  }
  return 0;
}
