#include <bits/stdc++.h>

using namespace std;

int main()
{
  int T;
  scanf("%d", &T);
  for (int i = 1; i <= T; i++){
    printf("Case #%d: ", i);
    int Smax;
    string S;
    cin >> Smax >> S;
    int total = 0;
    int ans = 0;
    for (int j = 0; j <= Smax; j++){
      int s = S[j] - '0';
      if (total >= j){
        total += s;
      }
      else {
        ans += j - total;
        total = j + s;
      }
    }
    printf("%d\n", ans);
  }
  return 0;
}

