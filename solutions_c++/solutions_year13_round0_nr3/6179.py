#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

bool is_palin(int n) {
  stringstream ss;
  ss << n;
  string str = ss.str();

  for (int i = 0; i < str.size() / 2; i++) {
    if (str[i] != str[str.size() - i - 1]) {
      return false;
    }
  }

  return true;
}

int main() {
  vector<int> fair;

  for (int i = 1; ; i++) {
    if (i * i > 10000) {
      break;
    }

    if (is_palin(i) && is_palin(i * i)) {
      fair.push_back(i * i);
    }
  }

  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    int A, B;
    cin >> A >> B;

    int cnt = 0;
    for (int j = 0; j < fair.size(); j++) {
      if (fair[j] >= A && fair[j] <= B) {
        cnt++;
      }
    }

    cout << "Case #" << (i + 1) << ": " << cnt << endl;
  }
}
