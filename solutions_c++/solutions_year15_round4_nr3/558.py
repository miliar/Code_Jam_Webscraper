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

char es[1100][20];
char fs[1100][20];
int ecounter = 0;
int fcounter = 0;
int record[100][2];

bool gete(char *s) {
  for (int i = 0; i < ecounter; ++i) {
    if (strcmp(s, es[i]) == 0) {
      return true;
    }
  }
  return false;
}

bool getf(char *s) {
  for (int i = 0; i < fcounter; ++i) {
    if (strcmp(s, fs[i]) == 0) {
      return true;
    }
  }
  return false;
}

int main(int argc, char *argv[]) {
#ifdef PRETEST
  freopen("C-small.in", "r", stdin);
#endif
  int T;
  scanf("%d", &T);
  for (int cas = 1; cas <= T; ++cas) {
    int n;
    scanf("%d", &n);
    memset(es, '\0', sizeof(es));
    memset(fs, '\0', sizeof(fs));
    memset(record, 0, sizeof(record));
    ecounter = 0;
    fcounter = 0;
    char s[100000];
    gets(s);
    gets(s);
    int length = strlen(s);
    s[length] = ' ';
    for (int j = 0; j <= length; ++j) {
      if (s[j] != ' ') {
        es[ecounter][strlen(es[ecounter])] = s[j];
      } else {
        ++ecounter;
      }
    }
    gets(s);
    length = strlen(s);
    s[length] = ' ';
    for (int j = 0; j <= length; ++j) {
      if (s[j] != ' ') {
        fs[fcounter][strlen(fs[fcounter])] = s[j];
      } else {
        ++fcounter;
      }
    }
    int ans = 0;
    for (int i = 0; i < fcounter; ++i) {
      if (gete(fs[i])) {
        ++ans;
      }
    }
    for (int i = 2; i < n; ++i) {
      gets(s);
      length = strlen(s);
      s[length] = ' ';
      char ss[100];
      memset(ss, '\0', sizeof(ss));
      for (int j = 0; j <= length; ++j) {
        if (s[j] != ' ') {
          ss[strlen(ss)] = s[j];
        } else {
          if (gete(ss)) {
            ++record[i][0];
          }
          if (getf(ss)) {
            ++record[i][1];
          }
          memset(ss, '\0', sizeof(ss));
        }
      }
    }
    int maxx = 1 << n;
    int minn = INF;
    for (int i = 0; i < maxx; ++i) {
      int tmp = 0;
      for (int j = 2; j < n; ++j) {
        if (i & (1 << j)) {
          tmp += record[j][1];
        } else {
          tmp += record[j][0];
        }
      }
      minn = min(minn, tmp);
    }
    printf("Case #%d: %d\n", cas, ans + minn);
  }
  return 0;
}
