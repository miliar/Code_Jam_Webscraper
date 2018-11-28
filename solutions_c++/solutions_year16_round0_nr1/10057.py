#include <iostream>
#include <string>
#include <sstream>

using namespace std;

bool test[256] = {};

void print_sleep(long N) {
  if (N == 0) {
    cout << "INSOMNIA";
  } else {
    test['0'] = test['1'] = test['2'] = test['3'] = test['4'] = test['5'] = test['6'] = test['7'] = test['8'] = test['9'] = false;
    long i = 1;
    int ctr = 10;
    while (true) {
      stringstream strstream;
      string number;
      long long ll = N*i;
      strstream << ll;
      strstream >> number;
//      cout << "*" << i << "|" << number << endl;
      for (auto it = number.cbegin(); it != number.cend();) {
        auto ch = *it;
        if (!test[ch]) {
          test[ch] = true;
          ctr--;
//          cout << "chr:" << ch << " " << i << '='<< ctr << endl;
        }
        ++it;
      }
      if (ctr == 0) {
        cout << ll;
        return;
      }
      i++;
    }
  }
}

int main(int argc, char **argv) {
  int T;
  long N;
  string line;
  string::size_type sz;
  getline(cin, line);
  T = stoi(line, &sz);
  for (int t = 1; t <= T; ++t) {
    getline(cin, line);
    N = stol(line, &sz);
    cout << "Case #" << t << ": ";
    print_sleep(N);
    cout << endl;
  }
  return 0;
}

