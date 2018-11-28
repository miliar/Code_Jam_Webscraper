#include <iostream>
#include <fstream>

using namespace std;

void process_case() {
  int K, C, S;
  cin >> K >> C >> S;

  if (C == 1 && S == K) {
    for (int i = 1; i <= K; ++i) {
      cout << " " << i;
    }
  } else if (C >= 2) {
    if (K == 1) {
      cout << " " << 1;
    } else if (S >= K - 1) {
      for (int i = 2; i <= K; ++i) {
        cout << " " << i;
      }
    }
  } else {
    cout << " IMPOSSIBLE";
  }
}

int main()
{
  std::ifstream in("D-small-attempt0.in");
  std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
  std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

  std::ofstream out("D-small-attempt0.out");
  std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
  std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

  int t;
  cin >> t;

  for (int i = 0; i < t; ++i) {
    cout << "Case #" << (i + 1) << ":";
    process_case();
    cout << endl;
  }

  return 0;
}