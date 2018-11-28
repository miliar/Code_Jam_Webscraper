#include<iostream>
#include<vector>
using namespace std;

int T, D, x;
vector<int> ar;

int main() {
  cin >> T;
  for (int tc = 1; tc <= T; tc++) {
    cin >> D;
    ar.clear();
    int maks = 0;

    for (int i = 0; i < D; i++) {
      cin>>x;
      if (x>maks) maks = x;
      ar.push_back(x);
    }

    int ans = 2000000000;
    for (int i = 1; i<=maks; i++) {
      int temp = i;
      for (int j = 0; j<D; j++) {
        int sisa = 0;
        if ((ar[j]%i) != 0) sisa = 1;
        temp += ar[j]/i + sisa - 1;
      }
      if (temp < ans) {
        ans = temp;
      }
    }

    cout << "Case #" << tc << ": " << ans << endl;
  }
}
