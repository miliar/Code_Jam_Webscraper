#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;
int main()
{
  int T;
  scanf("%d", &T);
  
  for (int i = 0; i < T; i++) {
    int s_max;
    string num;
    int sum = 0;
    int ans = 0;
    scanf("%d\n", &s_max);
    cin >> num;
    for (int j = 0; j <= s_max; j++) {
      int n = num.at(j) - '0';
      if (sum >= j) {
        sum += n;
      } else {
        int add = j - sum;
        sum += add;
        sum += n;
        ans += add;
      }
    }
    printf("Case #%d: %d\n", (i+1), ans);
  }
}
