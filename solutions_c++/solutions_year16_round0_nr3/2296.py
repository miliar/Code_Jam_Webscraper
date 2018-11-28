#include <stdlib.h>
#include <iostream>
#include <vector>

using namespace std;

vector<long long> test(vector<int> bit)
{
  vector<long long> ans;
  for (int b = 2; b <= 10; b++) {
    long long val = 0;
    for (size_t i = 0; i < bit.size(); i++) {
      val *= b;
      val += bit[i];
    }

    for (long long i = 2; i * i <= val; i++) {
      if (val % i == 0) {
        ans.push_back(i);
        break;
      }
    }
    if (ans.size() != b - 1) {
      return vector<long long>();
    }
  }
  return ans;
}

long long solve(int N, int J)
{
  long long i = 0;
  int j = 0;
  while (j < J) {
    vector<int> bit;
    bit.push_back(1);
    long long t = i;
    for (int k = 0; k < N - 2; k++) {
      bit.push_back(t % 2);
      t /= 2;
    }
    bit.push_back(1);

    vector<long long> s = test(bit);
    if (!s.empty()) {
      for (int k = 0; k < N; k++) {
        cout << bit[k];
      }
      for (int k = 0; k < s.size(); k++) {
        cout << " " << s[k];
      }
      cout << "\n";
      j++;
    }

    i++;
  }
}

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int N, J;
    cin >> N >> J;
    cout << "Case #" << t << ":\n";
    solve(N, J);
  }
}

