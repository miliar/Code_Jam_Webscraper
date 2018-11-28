#include <bits/stdc++.h>
using namespace std;

int m, n, a[222], v;
vector <int> edge[222];

int getHor(int x, int y)
{
  return x * n + y;
}

int getVer(int x, int y)
{
  return (m + 1) * n + y * m + x;
}

void addEdge(int u, int v)
{
  edge[u].push_back(v);
  edge[v].push_back(u);
}

int conv(int x)
{
  if (x <= n) return getHor(0, x - 1);
  x -= n;
  if (x <= m) return getVer(x - 1, n);
  x -= m;
  if (x <= n) return getHor(m, n - x);
  x -= n;
  return getVer(m - x, 0);
}

int canVisit(int s, int t)
{
  int from = conv(s), to = conv(t);
  queue <int> q;
  vector <int> visited(v, 0);
  q.push(from);
  visited[from] = 1;
  while (!q.empty())
  {
    int x = q.front();
    q.pop();
    for (auto y : edge[x])
      if (!visited[y])
      {
        q.push(y);
        visited[y] = 1;
      }
  }
  return visited[to];
}

int ok(int mask)
{
  for (int i = 0; i < v; i++)
    edge[i].clear();

  for (int i = 0; i < m; i++)
    for (int j = 0; j < n; j++)
      if (mask >> (i * n + j) & 1)
      {
        addEdge(getHor(i, j), getVer(i, j));
        addEdge(getHor(i + 1, j), getVer(i, j + 1));
      }
      else
      {
        addEdge(getHor(i, j), getVer(i, j + 1));
        addEdge(getHor(i + 1, j), getVer(i, j));
      }

  for (int i = 0; i < 2 * (m + n); i += 2)
    if (!canVisit(a[i], a[i + 1]))
      return 0;
  return 1;
}

int main()
{
  int test;
  cin >> test;
  for (int iTest = 1; iTest <= test; iTest++)
  {
    cerr << "Running test " << iTest << "..." << endl;
    cin >> m >> n;
    v = m * (n + 1) + n * (m + 1);
    for (int i = 0; i < 2 * (m + n); i++)
      cin >> a[i];

    int ans = -1;
    for (int mask = 0; mask < 1 << (m * n); mask++)
      if (ok(mask))
      {
        ans = mask;
        break;
      }

    cout << "Case #" << iTest << ":\n";
    if (ans < 0) cout << "IMPOSSIBLE" << endl;
    else
      for (int i = 0; i < m; i++)
      {
        for (int j = 0; j < n; j++)
          cout << (ans >> (i * n + j) & 1 ? '/' : '\\');
        cout << endl;
      }
  }
}