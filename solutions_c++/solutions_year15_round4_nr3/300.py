#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <string>
#include <vector>

using namespace std;

const int MAX = 100005;

int kol = 1;
int n;
char s[MAX];
int p[MAX];
int rez;
vector <int> V[MAX];
map <string, int> M;

int Eval(int x)
{
  int ret = 0;

  for (int i=0; i<kol; i++)
    p[i] = 0;

  for (int i=0; i<n; i++) {
    int ind;
    if (i < 2)
      ind = i;
    else
      ind = ((1<<(i-2)) & x) / (1<<(i-2));

    for (int j=0; j<(int) V[i].size(); j++) {
      int tmp = V[i][j];
      if (!p[tmp])
        p[tmp] = ind + 1;
      else if (p[tmp] != ind + 1 && p[tmp] != -1) {
        ret++;
        p[tmp] = -1;
        if (ret >= rez)
          return ret;
      }
    }
  }

  return ret;
}

int main()
{
  int brt;

  scanf("%d", &brt);

  for (int tt=1; tt<=brt; tt++) {
    rez = 1e9;

    for (int i=0; i<MAX; i++)
      V[i].clear();
    M.clear();

    scanf("%d", &n);
    for (int i=0; i<n; i++) {
      scanf(" %[^\n]", s);
      int l = strlen(s);
      s[l] = ' ';
      s[l+1] = 0;

      string tmp = "";
      for (char *p = s; *p; p++) {
        if (*p == ' ') {
          if (!M[tmp]) {
            V[i].push_back(kol);
            M[tmp] = kol++;
          }
          else
            V[i].push_back(M[tmp]);

          tmp = "";
        }
        else
          tmp += *p;
      }
    }
    for (int i=0; i<(int) (1<<(n-2)); i++)
      rez = min(rez, Eval(i));      

    fprintf(stderr, "%d\n", tt);
    printf("Case #%d: %d\n", tt, rez);
  }

  return 0;
}
