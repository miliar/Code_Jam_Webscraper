#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
#define MAX (101+10)

int main() {
  int TCn;
  scanf("%d", &TCn);

  for (int TC = 1; TC <= TCn; ++TC) {
    printf("Case #%d: ", TC);

    int n, m;
    scanf("%d%d", &n, &m);

    int tab[MAX][MAX];
    int i, j;

    // O(n2)
    for (i = 0; i < n; ++i) {
      int maior = -1;
      for (j = 0; j < m; ++j) {
	scanf("%d", &tab[i][j]);
	maior = max(maior,tab[i][j]);
      }
      tab[i][m] = maior;
    }

    //O(n2)
    for (i = 0; i < m; ++i) {
      int maior = -1;
      for (j = 0; j < n; ++j) {
	maior = max(maior, tab[j][i]);
      }
      tab[n][i] = maior;
    }

    bool ok = true;
    for (i = 0; i < n; ++i) {
      for (j = 0; j < m; ++j) {
	if ( !(tab[i][j] >= tab[n][j] || tab[i][j] >= tab[i][m]) ) {
	  ok = false;
	  break;
	}
      }
    }

    ok ? puts("YES") : puts("NO");
  }
  
  return 0;
}

/*
  4
  3 3
  2 1 2
  1 1 1
  2 1 2
  5 5
  2 2 2 2 2
  2 1 1 1 2
  2 1 2 1 2
  2 1 1 1 2
  2 2 2 2 2
  1 3
  1 2 1
  3 3
  2 3 1
  2 3 1
  2 4 1
*/
