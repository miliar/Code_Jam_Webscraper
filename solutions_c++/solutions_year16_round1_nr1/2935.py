#include <cstdio>
#include <cstdlib>
#include <string>
#include <iostream>

using namespace std;

int main() {
  int T;
  scanf("%d", &T);

  for (int t = 0; t < T; t++) {
    string result = "";
    char S[1100];
    scanf("%s", S);

    for (int i = 0; i < strlen(S); i++) {
      if (result.size() == 0 || S[i] >= result[0]) {
        result = S[i] + result;
      } else {
        result += S[i];
      }
    }
    cout << "Case #" << (t + 1) << ": " << result << "\n";
  }

  return 0;
}
