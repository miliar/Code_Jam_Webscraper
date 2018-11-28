#include <cstdio>
#include <cstdlib>

using namespace std;

auto main(int argc, char *argv[]) -> int {
  int TC, maxShy, audience[1010], currStanding, toAdd, currTC=0;
  char str[1010];
  scanf("%d", &TC);

  while(TC--) {
    scanf("%d %s", &maxShy, str);
    for (int i = 0; i <= maxShy; i++) {
      audience[i] = str[i] - 48;
    }

    currStanding = audience[0];
    toAdd = 0;
    for(int i = 1; i <= maxShy; i++) {
      if (currStanding < i) {
        toAdd += i - currStanding;
        currStanding = i;
      }
      currStanding += audience[i];
    }
    printf("Case #%d: %d\n", ++currTC, toAdd);
  }

  return 0;
}
