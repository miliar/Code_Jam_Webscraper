#include <cstdio>
#include <iostream>

using namespace std;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int nTest;
  scanf("%d", &nTest);
  for (int i = 1; i <= nTest; i++) {
    int s_max;
    char shyness[1111];
    scanf("%d %s", &s_max, shyness);
    
    int result = 0;
    int invited_friend = 0;
    for (; invited_friend <= 1000; invited_friend++) {
      // Check if it is enough
      int curr_clapping_people = invited_friend;
      for (int i = 0; i <= s_max; i++) {
        if (curr_clapping_people >= i)
          curr_clapping_people += (shyness[i] - '0');
        else goto exits;
      }

      // If it is enough
      result = invited_friend;
      break;

      // If it is not enough
      exits: ;
    }

    printf("Case #%d: %d\n", i, result);
  }

  return 0;
}
