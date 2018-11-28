#include <iostream>
#include <vector>

using namespace std;

int ans;
int k;

int main() {
  int T, N;
  cin >> T;
  char c;

  for (int i=1; i<=T; i++) {
    cin >> N;
    ans = k = 0;
    for (int j=0; j<=N; j++) {
      cin >> c;
      if (c-'0'!=0) {
        if (j > k) {
          ans += j-k;
          k=j;
        }
        k += c-'0';
      }
    }
    cout << "Case #" << i << ": " << ans << endl;
  }

  return 0;
}
