#include <cstdio>
#include <cstring>
#include <string>

int T;
std::string s[105];

int doit() {
  int result = 0;
  int at[105];
  memset(at, 0, sizeof(at));
  for (;;) {
    bool done = true;
    for (int i = 0; i < T; ++i) {
      if (at[i] != s[i].size()) {
        done = false;
      }
    }
    if (done) return result;

    if (at[0] >= s[0].size()) return -1;
    char c = s[0][at[0]];
    for (int i = 1; i < T; ++i) {
      if (at[i] >= s[i].size() || s[i][at[i]] != c) return -1;
    }

    int lengthmax = 0, lengthmin = 1000;
    for (int i = 0; i < T; ++i) {
      int cnt = 0;
      while (at[i] < s[i].size() && s[i][at[i]] == c) { cnt++; at[i]++; }
      lengthmax = std::max(lengthmax, cnt);
      lengthmin = std::min(lengthmin, cnt);
    }

    result += lengthmax-lengthmin; 
  }
}

void prob(int caseNum) {
  scanf("%d", &T);
  for (int i = 0; i < T; ++i) {
    char ts[105];
    scanf("%s", ts);
    s[i] = ts;
  }

  int result = doit();
  printf("Case #%d: ", caseNum);
  if (result == -1) {
    printf("Fegla Won\n");
  } else {
    printf("%d\n", result);
  }
}
int main() {
  int N;
  scanf("%d", &N);
  for (int i =0 ; i < N; ++i) {
    prob(i+1);
  }
}

