#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main() {
  int T, N;
  int h1, h2, t1, t2, s1, s2;
  vector<double> v1, v2;
  double tmp;
  cin >> T;
  for (int ti = 1; ti <= T; ti++) {
    cin >> N;
    v1 = vector<double>();
    v2 = vector<double>();
    for (int i = 0; i < N; i++) {
      cin >> tmp;
      v1.push_back(tmp);
    }
    for (int i = 0; i < N; i++) {
      cin >> tmp;
      v2.push_back(tmp);
    }
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());
    h1 = 0; h2 = 0; t1 = N - 1; t2 = N - 1; s1 = 0; s2 = 0;
    for (int i = 0; i < N; i++) {
      if (v1[t1] > v2[t2]) {
        s1++;
        t1--;
        t2--;
      } else {
        h1++;
        t2--;
      }
    }
    h1 = 0; h2 = 0; t1 = N - 1; t2 = N - 1;
    for (int i = 0; i < N; i++) {
      if (v2[t2] > v1[t1]) {
        t1--;
        t2--;
      } else {
        s2++;
        h2++;
        t1--;
      }
    }
    cout << "Case #" << ti << ": " << s1 << ' ' << s2 << endl;
  }
  return 0;
}
