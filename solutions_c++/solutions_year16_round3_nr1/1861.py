#include <bits/stdc++.h>

using namespace std;
vector<char> let;
int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  int T, n;
  cin >> T;
  for (int i = 0; i < 27; i++) {
    let.push_back(char('A' + i));
  }
  for (int i = 0; i < T; i++) {
    cin >> n;
    vector<int> mas(n);
    long long sum = 0;
    for (int j = 0; j < n; j++) {
        cin >> mas[j];
        sum += mas[j];
    }
    cout << "Case #" <<  i + 1 << ": ";
    while(sum > 0) {int f  = 1;
    int ind[2];
    int j = 0;

        while(j < n) {if (j >= n) {break;}
        if (f == 3) {break;}
            if ((sum - f) >= 0 && mas[j] > (sum - f) / 2) {
                f++;
                ind[f - 2] = j;
                mas[j]--;
            } else {j++;}
        }
        if (f == 1) {int j = 0;
            while(j < n && mas[j] == 0) {j++;}
          ind[0] = j;
          mas[j]--;
          f++;
        }
        f--;
        sum -= f;
                if (f == 2) {
        cout << let[ind[0]] << let[ind[1]];
        }
        if (f == 1) {
            cout << let[ind[0]];
        }
        cout << " ";
    }
    cout << endl;
  }


  return 0;
}
