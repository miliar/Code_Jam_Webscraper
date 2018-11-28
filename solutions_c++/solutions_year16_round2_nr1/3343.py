#include <iostream>
#include <set>
#include <map>
#include <cassert>

using namespace std;

int main()
{
  int cases;
  cin >> cases;

  for (auto curCase = 1; curCase <= cases; curCase++) {

    string s;
    cin >> s;
    string result;

    multiset<char> symbols(s.begin(), s.end());
    multiset<char> digits;

    auto removeWord = [&] (string word, char symbol, char digit) {
      auto it = symbols.find(symbol);
      while (it != symbols.end()) {
        for (auto ws: word) {
          auto wsit = symbols.find(ws);
          assert(wsit != symbols.end());
          symbols.erase(wsit);
        }
        digits.insert(digit);
        it = symbols.find(symbol);
      }
    };

    removeWord("ZERO", 'Z', '0');
    removeWord("SIX", 'X', '6');
    removeWord("EIGHT", 'G', '8');
    removeWord("TWO", 'W', '2');
    removeWord("FOUR", 'U', '4');
    removeWord("ONE", 'O', '1');
    removeWord("THREE", 'R', '3');
    removeWord("FIVE", 'F', '5');
    removeWord("SEVEN", 'S', '7');
    removeWord("NINE", 'N', '9');

    assert(symbols.empty());
    for (auto digit: digits) {
      result += digit;
    }

    cout << "Case #" << curCase << ": " << result << endl;
  }
}
