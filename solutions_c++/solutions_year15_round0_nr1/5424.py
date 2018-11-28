#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main() {
  int T, Smax;
  string a;
  int S[1005];
  cin >> T;
  for (int curT = 1; curT <= T; ++curT) {
    memset(S, 0, sizeof(S));
    cout << "Case #" << curT << ": ";
    cin >> Smax >> a;
    for (int i=0; i<=Smax; ++i) 
      S[i] = a[i] - '0';

    int num_so_far = 0;
    int num_need = 0;
    for (int i=0; i<=Smax; ++i) {
      if(S[i] > 0 && num_so_far < i) {
        num_need += i - num_so_far;
        num_so_far = i;
      }
      num_so_far += S[i];
    }
    cout << num_need << endl;
  }
}
