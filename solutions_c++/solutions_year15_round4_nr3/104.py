#include <cassert>
#include <cstdio>
#include <cstring>

#include <map>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

struct Edge {
  int t, f, c, r;
  Edge ( int _t, int _f, int _c, int _r ) : t(_t), f(_f), c(_c), r(_r) {}
};

vector <vector <Edge> > *g;
map <string, int> *m;
int *c, T;

void edge ( int u, int v, int c ) {
  // fprintf (stderr, "edge: %d -> %d (%d)\n", u, v, c);
  (*g)[u].push_back (Edge (v, 0, c, (*g)[v].size ()));
  (*g)[v].push_back (Edge (u, 0, 0, (*g)[u].size () - 1));
}

void word ( const string &w ) {
  if (m->count (w))
    return;
  (*m)[w] = g->size ();
  g->push_back (vector <Edge> ());
  g->push_back (vector <Edge> ());
  edge ((*m)[w], (*m)[w] + 1, 1);
}

bool dfs ( int u, int it ) {
  if (u == T)
    return true;
  c[u] = it;
  for (int i = 0; i < (int)(*g)[u].size (); i++) {
     if (c[(*g)[u][i].t] == it || (*g)[u][i].f >= (*g)[u][i].c)
       continue;
     if (!dfs ((*g)[u][i].t, it))
       continue;
     (*g)[u][i].f++;
     (*g)[(*g)[u][i].t][(*g)[u][i].r].f--;
     return true;
  }
  return false;
}

void solve ( int tt ) {
  int n;
  assert (scanf ("%d ", &n) == 1);

  vector <string> data[n];
  for (int i = 0; i < n; i++) {
    char s[200000];
    assert (fgets (s, 19999, stdin));
    stringstream ss (s);
    string w;
    while (ss >> w) {
      data[i].push_back (w);
      // fprintf (stderr, "s #%d word: '%s'\n", i, w.c_str ());
    }
  }
  int S = 0;
  int T = 1;
  vector <vector <Edge> > g (2);
  map <string, int> m;
  ::g = &g;
  ::m = &m;

  for (int i = 0; i < (int)data[0].size (); i++) {
    word (data[0][i]);
    edge (S, m[data[0][i]], 1000000);
  }
  for (int i = 0; i < (int)data[1].size (); i++) {
    word (data[1][i]);
    edge (m[data[1][i]] + 1, T, 1000000);
  }
  for (int i = 2; i < n; i++) {
    int x = g.size ();
    g.push_back (vector <Edge> ());
    for (int j = 0; j < (int)data[i].size (); j++) {
      string &w = data[i][j];
      word (w);
      edge (m[w] + 1, x, 1000000);
      edge (x, m[w], 1000000);
    }
  }

  int c[g.size ()];
  memset (c, 0, sizeof (c[0]) * g.size ());
  ::c = c, ::T = T;
  
  int ans = 0, it = 1;
  while (dfs (S, it)) {
    ans++, it++;
  }
  printf ("Case #%d: %d\n", tt, ans);
}

int main () {
  int tn;
  assert (scanf ("%d", &tn) == 1);
  for (int t = 1; t <= tn; t++)
    solve (t);
  return 0;
}

