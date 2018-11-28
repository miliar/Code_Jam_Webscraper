#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX = 105;

char p[MAX][MAX];
int valja[4][MAX][MAX];
int pr[4] = {1, 0, -1, 0}, ps[4] = {0, 1, 0, -1};
int brred, brstup;
char inds[5] = "v>^<";

int Vani(int r, int s)
{
  return r < 0 || s < 0 || r >= brred || s >= brstup;
}

int Dokle(int r, int s, int smjer)
{
  r += pr[smjer];
  s += ps[smjer];

  for (;; r += pr[smjer], s += ps[smjer]) {
    if (Vani(r, s))
      return 0;

    if (p[r][s] != '.')
      return 1;
  }
}

int main()
{
  int brt;

  scanf("%d", &brt);

  for (int tt=1; tt<=brt; tt++) {
    printf("Case #%d: ", tt);

    scanf("%d%d", &brred, &brstup);

    for (int i=0; i<brred; i++)
      scanf("%s", p[i]);

    for (int i=0; i<brred; i++)
      for (int j=0; j<brstup; j++)
        for (int k=0; k<4; k++)
          valja[k][i][j] = Dokle(i, j, k);

    int rez = 0, ne = 0;

    for (int i=0; i<brred; i++) {
      for (int j=0; j<brstup; j++) {
        int ind = -1;
        for (int k=0; k<4; k++)
          if (inds[k] == p[i][j])
            ind = k;
        
        if (ind == -1)
          continue;

        if (!valja[ind][i][j]) {
          int ima = 0;
          for (int k=0; k<4; k++)
            if (valja[k][i][j])
              ima = 1;

          if (!ima)
            ne = 1;
          else
            rez++;
        }
      }
    }

    if (ne)
      printf("IMPOSSIBLE\n");
    else
      printf("%d\n", rez);
  }

  return 0;
}
