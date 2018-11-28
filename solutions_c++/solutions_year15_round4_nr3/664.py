#include <cstdio>
#include <cstring>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <vector>

#define Nmax 4100

using namespace std;

int n, m, t;
bool Viz[Nmax];
int Q[Nmax], T[Nmax], Cap[Nmax][Nmax];
vector< vector<string> > V;
map<string, int> Words;

bool bfs(int Src, int Dest) {
  memset(Viz, 0, sizeof(Viz));
  memset(T, 0, sizeof(T));
  Viz[Src] = 1;
  Q[Q[0] = 1] = Src;

  for (int i = 1; i <= Q[0]; ++i) {
    int nod = Q[i];

    for (int next = 1; next <= n + m; ++next) {
      if (!Cap[nod][next] || Viz[next])
        continue;

      //printf("%d -> %d\n", nod, next);
      Viz[next] = true;
      T[next] = nod;
      Q[++Q[0]] = next;
    }
  }
  return Viz[Dest];
}

int flow(int Src, int Dest) {
  int res = 0;
  while(bfs(Src, Dest)) {
    int cnt = 99999;
    for (int nod = Dest; T[nod]; cnt = min(cnt, Cap[T[nod]][nod]), nod = T[nod]);
    res += cnt;
    for (int nod = Dest; T[nod]; Cap[T[nod]][nod] -= cnt, Cap[nod][T[nod]] += cnt, nod = T[nod]);
  }
  return res;
}

int main() {
  scanf("%d", &t);

  for (int ti = 1; ti <= t; ++ti) {
    m = 0;
    memset(Cap, 0, sizeof(Cap));
    Words.clear();
    V.clear();

    scanf("%d%d\n", &n, &t);
    V.resize(n + 1);
    for (int j = 1; j <= n; ++j) {
      char buffer[15000];
      fgets(buffer, 15000, stdin);
      
      int k = 0;
      while (k < strlen(buffer)) {
        string ws;
        for (;buffer[k] == ' ';++k);
        for (;(buffer[k] >= 'a' && buffer[k] <= 'z') || (buffer[k] >= 'A' && buffer[k] <= 'Z');++k)
          ws.push_back(buffer[k]);

        if (!ws.size())
          break;
        V[j].push_back(ws);
      } 
    }

    for (int j1 = 1; j1 <= n; ++j1) {
      set<string> S;
      for (int k = 0; k < V[j1].size(); ++k)
        S.insert(V[j1][k]);

      for (int j2 = j1 + 1; j2 <= n; ++j2) {
        int count = 0;
        for (int k = 0; k < V[j2].size(); ++k) {
          if (S.find(V[j2][k]) == S.end())
            continue;

          if (Words.find(V[j2][k]) == Words.end()) {
            ++m;
            Words[V[j2][k]] = n + m;
          }
          
          ++count;
          int wid = Words[V[j2][k]];
          Cap[j1][wid] = 1;
          Cap[wid][j2] = 1;
          Cap[wid][j1] = 1;
          Cap[j2][wid] = 1;
        }
        //printf("%d %d %d\n", j1, j2, count);
      }
    }

    printf("Case #%d: %d\n", ti, flow(1, 2)); 
  }

  return 0;
}
