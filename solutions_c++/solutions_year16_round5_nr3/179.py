#include <bits/stdc++.h>

#define MOD 1000000007

using namespace std;

typedef long long int lld;
typedef pair<int, int> pii;
typedef pair<double, int> pdi;
typedef pair<double, pii> triple;

#define F first
#define S second

double dist[1100][1100];
int px[1100], py[1100], pz[1100];
vector<int> nei[1100];
priority_queue<triple> pq;
int p[1100], rank[1100];

void init(int N){ for(int i = 0; i < N; i ++) p[i] = i, rank[i] = 0; }
int findSet(int i){ return ((p[i] == i) ? i : (p[i] = findSet(p[i]))); }
bool isSameSet(int i, int j){ return (findSet(i) == findSet(j)); }
void unionSet(int i, int j)
{
  if (!isSameSet(i, j))
  {
    int x = findSet(i), y = findSet(j);
    if (rank[x] > rank[y]) p[y] = x;
    else
    {
      p[x] = y;
      if (rank[x] == rank[y]) rank[y]++;
    }
  }
}

double dfs(int cur, int prev, double wlk)
{
  if (cur == 1)
    return wlk;

  int i;
  double mx = 1000000000;
  for (i = 0; i < (int)nei[cur].size(); i++)
    if (nei[cur][i] != prev)
      mx = min(mx, dfs(nei[cur][i], cur, max(wlk, dist[cur][nei[cur][i]])));
  return mx;
}

int main()
{
  int i, j;
  int n;
  int t, T;
  scanf("%d", &T);
  
  for (t = 1; t <= T; t++)
  {
    scanf("%d %*d", &n);

    for (i = 0; i < n; i++)
    {
      scanf("%d %d %d %*d %*d %*d", &px[i], &py[i], &pz[i]);
      nei[i].clear();
    }

    for (i = 0; i < n; i++)
      for (j = i + 1; j < n; j++)
      {
        dist[j][i] = dist[i][j] = sqrt((px[i] - px[j]) * (px[i] - px[j]) + 
                                       (py[i] - py[j]) * (py[i] - py[j]) + 
                                       (pz[i] - pz[j]) * (pz[i] - pz[j]));
        pq.push(triple(-dist[i][j], pii(i, j)));
      }

    init(n);
    while (!pq.empty())
    {
      triple nx = pq.top();
      pq.pop();

      if (isSameSet(nx.S.F, nx.S.S))
        continue;

      unionSet(nx.S.F, nx.S.S);
      nei[nx.S.F].push_back(nx.S.S);
      nei[nx.S.S].push_back(nx.S.F);
    }

    double ans = dfs(0, -1, 0);

    printf("Case #%d: %0.9lf\n", t, ans);
  }

  return 0;
}
