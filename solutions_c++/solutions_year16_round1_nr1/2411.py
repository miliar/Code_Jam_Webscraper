#include <bits/stdc++.h>
using namespace std;

char S[1005];
int T;

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w+", stdout);
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    scanf("%s", S);
    deque<char> R;
    R.push_back(S[0]);
    for (int i = 1; S[i]; i++) {
      if (S[i] < R.front()) R.push_back(S[i]);
      else R.push_front(S[i]);
    }
    printf("Case #%d: ", t);
    while (R.size()) {
      printf("%c", R.front());
      R.pop_front();
    }
    printf("\n");
  }
  return 0;
}

