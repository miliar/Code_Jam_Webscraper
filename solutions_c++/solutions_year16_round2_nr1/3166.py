#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>
using namespace std;


int main() {
  int T;
  char buf[2020];

  scanf("%d", &T);
  for (int tc = 1; tc <= T; ++tc) {
    scanf("%s", buf);
    vector<int> v(26, 0);
    int l = strlen(buf);
    for (int i = 0; i < l; ++i) {
      v[buf[i] - 'A'] += 1;
    }
    string result = "";
    string numbers[] = {"ZERO", "SIX", "EIGHT", "TWO", "FOUR",
                        "FIVE", "NINE", "SEVEN", "THREE", "ONE"};
    int values[] = {0, 6, 8, 2, 4, 5, 9, 7, 3, 1};
    for (int i = 0; i < 10; ++i) {
      vector<int> x(26, 0);
      for (int j = 0; j < (int)numbers[i].size(); ++j) {
        ++x[numbers[i][j] - 'A'];
      }
       
      while (true) {
       bool can = true; 
       for (int j = 0; j < 26; ++j) {
          if (v[j] < x[j]) {
            can = false;
            break;
          }
        }
       if (!can) {
         break;
       }
        result += (char)('0' + values[i]);
        for (int j = 0; j < 26; ++j) {
          v[j] -= x[j];
        }
      }      
    }
    sort(result.begin(), result.end());
    printf("Case #%d: %s\n", tc, result.c_str());
  }
  return 0;
}
