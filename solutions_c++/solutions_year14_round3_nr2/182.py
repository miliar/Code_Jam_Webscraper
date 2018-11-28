#include <cstdio>
#include <memory.h>

using namespace std;

char buffer[1000];
char groomed[1000];

const long long PRIME = 1000000007;

int main() {
  int nCase;
  scanf("%d", &nCase);

  for (int iCase = 0; iCase < nCase; ++iCase) {
    int n;
    int pures[26];
    int middles[26];
    int graph[26];
    bool referenced[26];
    bool visited[26];
    bool impossible = false;

    memset(pures, 0, sizeof(pures));
    memset(middles, 0, sizeof(middles));
    memset(graph, -1, sizeof(graph));
    memset(referenced, 0, sizeof(referenced));
    memset(visited, 0, sizeof(visited));

    scanf("%d", &n);
    
    for (int i = 0; i < n; ++i) {
      scanf("%s", buffer);
      int len = strlen(buffer);
      int glen = 0;

      for (int j = 0; j < len; ++j) {
        if (glen == 0 || buffer[j] != groomed[glen - 1]) {
          groomed[glen++] = buffer[j];
        }
      }

      if (glen == 1) {
        ++pures[groomed[0] - 'a'];
      }
      else {
        for (int j = 1; j < glen - 1; ++j) {
          if (++middles[groomed[j] - 'a'] > 1) {
            impossible = true;
          }
        }

        if (graph[groomed[0] - 'a'] != -1) {
          impossible = true;
        }
        graph[groomed[0] - 'a'] = groomed[glen - 1] - 'a';
        referenced[groomed[glen - 1] - 'a'] = true;
      }
    }

    printf("Case #%d: ", iCase + 1);

    int nPerm = 0;
    long long sol = 1;

    if (impossible) {
      goto impossibleEnd;
    }

    // for (int i = 0; i < 26; ++i) {
    //   printf("%d ", graph[i]);
    // }
    // printf("\n");
    
    for (int i = 0; i < 26; ++i) {
      if (!referenced[i] && graph[i] != -1) {
        ++nPerm;
        for (int ptr = i; ptr != -1; ptr = graph[ptr]) {
          if (middles[ptr] > 0) {
            goto impossibleEnd;
          }
          if (visited[ptr]) {
            goto impossibleEnd;
          }
          visited[ptr] = true;
        }
      }
    }

    for (int i = 0; i < 26; ++i) {
      if (graph[i] != -1 && !visited[i]) {
        goto impossibleEnd;
      }
      if (pures[i] > 0) {
        if (middles[i] > 0) {
          goto impossibleEnd;
        }
        if (!visited[i]) {
          ++nPerm;
        }
        while (pures[i] > 0) {
          sol = (sol * pures[i]) % PRIME;
          --pures[i];
        }
      }
    }

    while (nPerm > 0) {
      sol = (sol * nPerm) % PRIME;
      --nPerm;
    }

    printf("%lld\n", sol);
    continue;

  impossibleEnd:
    printf("0\n");
  }
}
