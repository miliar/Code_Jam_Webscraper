#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int CASE = 1; CASE <= T; CASE++) {
    int N, X;
    cin >> N >> X;
    int s[N];
    for (int i = 0; i < N; i++)
      cin >> s[i];
    sort(s, s+N);
    int res = 0;
    for (; N >= 1 && s[N-1] >= X; N--)
      res++;
    for (int i = 0, j = N-1; i <= j; ) {
      if (i == j) {
        res++;
        break;
      }
      if (s[i] + s[j] <= X) {
        i++, j--;
        res++;
      } else {
        j--;
        res++;
      }
    }
    cout << "Case #" << CASE << ": " << res << endl;
  }
}