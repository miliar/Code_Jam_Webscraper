#include <iostream>
#include <string>
#include <vector>

using namespace std;

string doit() {
  long long N;
  cin >> N;

  vector<int> seen(10);

  for (long long i = 1; i <= 1000000; ++i) {
    long long nn = i*N;
    long long tmp = nn;
    while (tmp) {
      seen[tmp%10] = 1;
      tmp /= 10;
    }
    bool nseen = false;
    for (int i = 0; i < 10; ++i) {
      if (!seen[i]) {
        nseen = true;
        break;
      }
    }
    if (nseen)
      continue;
    return to_string(nn);
  }
  
  return "INSOMNIA";
}

int main() {
  ios::sync_with_stdio(false);

  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #"<<t << ": " << doit() << endl;
  }

}
