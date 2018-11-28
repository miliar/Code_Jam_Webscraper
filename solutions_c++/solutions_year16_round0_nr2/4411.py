#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main() {
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++) {
    vector<char> pancake;
    char input[101];

    scanf("%s", input);
    int len = strlen(input);
    pancake.insert(pancake.end(), input, input + len);
    pancake.erase(unique(pancake.begin(), pancake.end()), pancake.end());

    /*
    for (int i = 0; i < pancake.size(); i++) {
      printf("%c", pancake[i]);
    }puts("");
    */

    int yeah = pancake[pancake.size() -1] == '+';
    printf("Case #%d: %lu", t, pancake.size() - yeah);
    puts("");
  }
  
  return 0;
}
