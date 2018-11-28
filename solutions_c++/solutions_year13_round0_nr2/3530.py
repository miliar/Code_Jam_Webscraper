#include<iostream>
#include<cstdio>

using namespace std;

int main() {
  int probs;
  cin >> probs;

  for (int p = 1; p<= probs; p++) {
    int n,m;
    cin >> n >> m;
    int h[n][m];
    
    for (int x = 0; x < n; x++)
      for (int y = 0; y < m; y++)
        cin >> h[x][y];

    int rMin[m];
    int cMin[n];

    for (int i = 0; i < m; i++) rMin[i] = 0;
    for (int i = 0; i < n; i++) cMin[i] = 0;

    for (int x = 0; x < n; x++)
    {
      for (int y = 0; y < m; y++) {
        if (h[x][y] > rMin[y]) rMin[y] = h[x][y];
        if (h[x][y] > cMin[x]) cMin[x] = h[x][y];
      }
    }

    bool impossible = false;
    for (int x = 0; x < n; x++)
    {
      for (int y = 0; y < m; y++) {
        if (h[x][y] < rMin[y] && h[x][y] < cMin[x]) {
          impossible = true;
          break;
        }
      }

      if (impossible) break;
    }

    /*
    for (int y = 0; y < m; y++) printf("%i ", rMin[y]);
    printf("\n");
    for (int x = 0; x < n; x++) printf("%i\n", cMin[x]);
    */

    printf("Case #%i: ", p);

    if (!impossible) printf("YES\n");
    else printf("NO\n");
  }
}
