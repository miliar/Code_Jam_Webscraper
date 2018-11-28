#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <fstream>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

vector<int> divisors[1001];

int ceil(int num, int denom) {
  if (num%denom == 0) return num/denom;
  return (num/denom) + 1;
}

int solve(const vector<int> &v) {
  int best = v.back();
  for (int eat=1; eat<=best; eat++) {
    int cur = eat;
    for (int i=(int)(v.size())-1; i>=0 && v[i]>eat && cur < best; i--) {
      cur += ceil(v[i], eat) - 1;
    }
    best = min(best, cur);
  }
  return best;
}

int main() {
  int tc, d, tmp;
  cin >> tc;
  for (int t=1; t<=tc; t++) {
    cin >> d;
    vector<int> v;
    for (int i=0; i<d; i++) {
      cin >> tmp;
      v.push_back(tmp);
    }
    sort(v.begin(), v.end());
    cout << "Case #"<<t<<": "<< solve(v) << endl;
  }

  return 0;
}
