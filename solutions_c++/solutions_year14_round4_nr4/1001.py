#include<cstdio>
#include<cstring>

char s[10][20];
int assign[10];
int nodes[100][30];
int numnodes;

void buildtree(int index, int node, int dep, int maxdep) {
  if (dep >= maxdep) {
    return;
  }
  int child = s[index][dep] - 'A';
  if (nodes[node][child] == -1) {
    //make new node
    for(int i=0;i<26;i++) {
      nodes[numnodes][i] = -1;
    }
    nodes[node][child] = numnodes;
    numnodes++;
  }
  buildtree(index, nodes[node][child], dep+1, maxdep);
}

int getsize(int m, int n) {
  int size = 0;
  for (int z=0; z<n; z++) {
    // reset tree
    numnodes = 1;
    int any = 0;
    for(int i=0;i<26;i++) {
      nodes[0][i] = -1;
    }
    for (int i=0; i<m; i++) {
      if (assign[i] == z) {
        buildtree(i, 0, 0, strlen(s[i]));
        any = 1;
      }
    }
    if (any == 1) {
      size += numnodes;
    }
  }
  /*printf("ARRANGE ");
  for(int i=0;i<m;i++) {printf("%d ",assign[i]);}
  printf("RESULT %d\n", size);*/
  return size;
}

int main() {
  int m, n, p, x, y;
  int tt, uu;
  scanf("%d", &tt);
  for (int t=1; t<=tt; t++) {
    scanf("%d", &m);
    scanf("%d", &n);
    for (int i = 0; i < m; i++) {
      scanf("%s", s[i]);
    }
    for (int i = 0; i <= m; i++) {
      assign[i] = 0;
    }
    x = -1;
    y = 1;
    while (assign[m] == 0) {
      p = getsize(m, n);
      if (p > x) {
        x = p;
        y = 1;
      } else if (p == x) {
        y++;
      }
      uu = 0;
      if (n <= 1) {
        break;
      }
      while (true) {
        assign[uu]++;
        if (assign[uu] >= n) {
          assign[uu] = 0;
          uu++;
        } else {
          break;
        }
      }
    }
    y %= 1000000007;
    printf("Case #%d: %d %d\n", t, x, y);
  }
}
