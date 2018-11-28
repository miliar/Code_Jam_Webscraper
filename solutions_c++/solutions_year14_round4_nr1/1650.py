#include <iostream>
#include <algorithm>
using namespace std;

int T, t, i, N, X, S[10240];

int main() {
  cin >> T;
  for (t=1; t<=T; t++) {
    cout << "Case #" << t << ": ";
    cin >> N >> X;
    for (i=0; i<N; i++)
      cin >> S[i];

    sort(S, S+N);
    int beg = 0, end = N-1, cnt = 0;
    while (beg < end) {
      if (S[beg] + S[end] <= X)
        cnt++, beg++, end--;
      else 
        cnt++, end--;
    }
    if (beg == end) cnt++;
    cout << cnt << endl;
 }
}                              
