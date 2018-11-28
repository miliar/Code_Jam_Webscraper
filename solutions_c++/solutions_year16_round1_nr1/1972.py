#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

const int maxl = 1000;
char str[maxl+5];

int main() {
  int tc;
  scanf("%d\n", &tc);
  for(int kase = 1; kase <= tc; kase++) {
    scanf("%s\n", str);
    int l = strlen(str);
    string ans;
    char prev = 0;
    for(int i = 0; i < l; i++) {
      if(ans.empty()) {
	ans = ans + str[i];
      } else if(str[i] > ans[0]) {
	prev = ans[0];
	ans = str[i] + ans;
      } else if(str[i] < ans[0]) {
	ans = ans + str[i];
      } else if(str[i] > prev) {
	ans = str[i] + ans;
      } else {
	ans = ans + str[i];
      }
    }
    printf("Case #%d: %s\n", kase, ans.c_str());
  }
  return 0;
}
