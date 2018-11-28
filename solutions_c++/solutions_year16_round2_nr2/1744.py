#include <bits/stdc++.h>

using namespace std;
string mas[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int main() {
    //ios_base::sync_with_stdio(0);
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T, sum = 0;
  cin >> T;
  string s, s1;
  for (int q = 0; q < T; q++) {
    cin >> s >> s1;
    cout << "Case #" << q + 1 << ": ";
    int ans;
    int ans1;
    int mn = 1e9;
    int S = s.size();
    int S1 = s1.size();
    if (s.size() < 3) {
        while(s.size() < 3) {
            s = '0' + s;
        }
    }
     if (s1.size() < 3) {
        while(s1.size() < 3) {
            s1 = '0' + s1;
        }
    }
    int sum = 0;
    int sum1 = 0;
    for (int i = 0; i < 10; i++) {

        for (int j = 0; j < 10; j++) {
            for(int k = 0; k < 10; k++) {sum1 = 0;
              if (s1[0] == '?') {
                sum1 += i * 100;
            } else {
              sum1 += (s1[0] - '0') * 100;
            }
         if (s1[1] == '?') {
                sum1 += j * 10;
            } else {
              sum1 += (s1[1] - '0') * 10;
            }
            if (s1[2] == '?') {
                sum1 += k;
            } else {
              sum1 += (s1[2] - '0');
            }
            for (int i1 = 0; i1 < 10; i1++) {
                for(int j1 = 0; j1 < 10; j1++) {
                    for (int k1 = 0; k1 < 10; k1++) {sum = 0;
                       if (s[0] == '?') {
                sum += i1 * 100;
            } else {
              sum += (s[0] - '0') * 100;
            }
         if (s[1] == '?') {
                sum += j1 * 10;
            } else {
              sum += (s[1] - '0') * 10;
            }
            if (s[2] == '?') {
                sum += k1;
            } else {
              sum += (s[2] - '0');
            }
            if (abs(sum - sum1) < mn) {
                mn = abs(sum - sum1);
                ans = sum;
                ans1 = sum1;
            }
        }

            }

            }

        }
        }
    }
    vector<int> v, v1;
    while(ans) {
        v.push_back(ans % 10);
        ans /= 10;
    }
    while(ans1) {
        v1.push_back(ans1 % 10);
        ans1 /= 10;
    }
    while(v.size() < S) {
        v.push_back(0);
    }
    while(v1.size() < S1) {
        v1.push_back(0);
    }
    for (int t = v.size() - 1; t >= 0; t--) {
        cout << v[t];
    }
    cout << " ";
    for (int t = v1.size() - 1; t >= 0; t--) {
        cout << v1[t];
    }
    cout << endl;
  }








  return 0;
}
