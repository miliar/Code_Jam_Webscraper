#include <cstdio>

const int MAXN = 50;
const int MAXC = 30;

int trie[MAXN][MAXN][MAXC];

int T;
int N, M;

char str[MAXN][MAXN];
int assn[MAXN];
int size[MAXN];

void insert(char *s, int t) {
  int cur = 0;
  int &z = size[t];
  for(int i = 0; s[i]; ++i) {
    int &nxt = trie[t][cur][s[i] - 'A'];
    if (!nxt) nxt = ++z;
    cur = nxt;
  }
}

int comp() {
  for(int i = 0; i < N; ++i) {
    for(int j = 0; j <= size[i]; ++j) {
      for(int k = 0; k < MAXC; ++k) {
        trie[i][j][k] = 0;
      }
    }
    size[i] = 0;
  }
  for(int i = 0; i < M; ++i) {
    insert(str[i], assn[i]);
  }

  int ans = 0;
  for(int i = 0; i < N; ++i) {
    if (size[i] == 0) return -1;
    ans += size[i] + 1;
  }
  return ans;
}

int ans, ways;
void rec(int cur = 0) {
  if (cur == M) {
    int val = comp();
    if (val > ans) {
      ans = val;
      ways = 0;
    }
    if (val == ans) {
      ++ways;
    }
  } else {
    for(int i = 0; i < N; ++i) {
      assn[cur] = i;
      rec(cur + 1);
    }
  }
}

int main() {
  scanf("%d", &T);

  for(int t = 1; t <= T; ++t) {
    scanf("%d %d", &M, &N);
    for(int i = 0; i < M; ++i) {
      scanf("%s", str[i]);
    }

    ans = 0;
    ways = 0;
    rec();
    printf("Case #%d: %d %d\n", t, ans, ways);
  }
}


