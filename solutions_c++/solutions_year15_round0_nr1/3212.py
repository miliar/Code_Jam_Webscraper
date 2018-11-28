#define PRETEST
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <math.h>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <iomanip>
#include <sstream>
using namespace std;

#define INF 0x4f4f4f4f
#define FILL(a,b) memset(a,b,sizeof(a))
#define SQR(a) ((a) * (a))

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<string, int> psi;
typedef map<string, int> msi;
typedef map<int, int> mii;

int main(int argc, char *argv[]) {
#ifdef PRETEST
  freopen("A-large.in", "r", stdin);
  freopen("out.txt", "w+", stdout);
#endif
  int T;
  scanf("%d", &T);
  for (int C = 1; C <= T; ++C) {
    int n;
    char s[1010];
    scanf("%d", &n);
    scanf("%s", s);
    int length = strlen(s);
    int ans = 0;
    int sum = 0;
    for (int i = 0; i < length; ++i) {
      if (s[i] == '0') {
        continue;
      }
      int num = s[i] - '0';
      if (sum >= i) {
        sum += num;
      } else {
        int tmp = i - sum;
        ans += tmp;
        sum += num + tmp;
      }
    }
    printf("Case #%d: %d\n", C, ans);
  }
  
  return 0;
}
