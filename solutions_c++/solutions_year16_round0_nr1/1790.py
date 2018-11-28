#include <iostream>
#include <set>

using namespace std;

int main()
{
  int cases;
  cin >> cases;

  for (auto curCase = 1; curCase <= cases; curCase++) {

    int64_t n;
    cin >> n;
    set<char> digits;

    string result = "INSOMNIA";
    if (n > 0) {
      int attempt = 0;
      while (++attempt < 100) {
        int64_t num = n * attempt;
        auto curDigits = to_string(num);
        for (auto digit: curDigits) {
          digits.insert(digit);
        }
        if (digits.size() >= 10) {
          result = curDigits;
          break;
        }
      }
    }
    cout << "Case #" << curCase << ": " << result << endl;
  }
}
