#include <iostream>
#include <set>
#include <vector>
using namespace std;
int n;
vector<int> a;

auto calc(int cnt) {
  int ans = 0;
  for (auto i: a) {
    ans += (i-1) / cnt;
  }
  return ans;
}

auto calc() {
    int m = 1010;
    for (int i = 1; i < 1010; i++) {
        m = min(m, i + calc(i));
    }
    return m;
}

auto work() {
    cin >> n;
    a.clear();
    for (auto i = 0; i < n; i++) {
        int k;
        cin >> k;
        a.push_back(k);
    }
    return calc();
}

int main() {
    int kase = 0;
    cin >> kase;
    for (auto i = 1; i <= kase; i++) {
        cout << "Case #" << i << ": " << work() << endl;
    }
}
