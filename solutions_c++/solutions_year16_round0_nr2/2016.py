#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void process_once(){
  string S;
  cin >> S;

  if (S.length() == 0) {
    cout << 0;
  } else if (S.length() == 1) {
    cout << (S[0] == '+' ? 0 : 1);
  } else {
    char prev;
    char curr;
    int count = 0;
    for (int i = 1; i < S.length(); ++i) {
      prev = S[i - 1];
      curr = S[i];

      if (curr != prev) {
        ++count;
      }
    }

    if (curr == '-') {
      ++count;
    }

    cout << count;
  }
}

int main() {
  std::ifstream in("B-large.in");
  std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
  std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

  std::ofstream out("B-large.out");
  std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
  std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

  int T;
  cin >> T;

  for (int i = 0; i < T; ++i) {
    cout << "Case #" << (i + 1) << ": ";
    process_once();
    cout << endl;
  }
}
