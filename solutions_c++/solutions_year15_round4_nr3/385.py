#include <bits/stdc++.h>
using namespace std;

int t,n,i;
char s[100005];
vector <int> words[500];
int mask[2005];
int maskori[2005];
map <string, int> dict;

int cs =0;
int main() {
  scanf("%d", &t);
  while (t--) {
    memset(maskori, 0, sizeof(maskori));
    dict.clear();
    ++cs;
    scanf("%d\n", &n);
    for (int i = 0; i < n; i++) {
      words[i].clear();
      gets(s);
      char* tok = strtok(s, " ");
      while (tok != NULL) {
        string tmps = tok;
        if (dict.count(tmps) == 0) {
          int sz = dict.size();
          dict[tmps] = sz;
        }
        words[i].push_back(dict[tmps]);
        tok = strtok(NULL, " ");
      }
    }
    for (int i = 0; i < int(words[0].size()); i++) {
      maskori[words[0][i]] |= 1;
    }
    for (int i = 0; i < int(words[1].size()); i++) { 
      maskori[words[1][i]] |= 2;
    }
    int res = 1000000000;
    for (int i = 0; i < (1 <<(n-2)); i++) {
      memset(mask, 0, sizeof(mask));
      for (int j = 2; j < n; j++) {
        if (i & (1<<(j-2))) {
          for (int k = 0; k < words[j].size(); k++) {
            mask[words[j][k]] |= 2;
          }
        } else {
          for (int k = 0; k < words[j].size(); k++) {
            mask[words[j][k]] |= 1;
          }
        }
      }
      int now = 0;
      for (int i = 0; i < (int)dict.size(); i++) {
        if ((mask[i] | maskori[i]) == 3) {
          ++now;
        }
      }
      res = min(res, now);
    }
    printf("Case #%d: %d\n", cs, res);
  }
}
