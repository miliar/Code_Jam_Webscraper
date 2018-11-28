// Yen-Ming Lee <leeym@leeym.com>
// http://code.google.com/codejam/contest/dashboard?c=2270488#s=p1
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;
int verbose = 0, debug = 0;
int main(int argc, char *argv[])
{
  int ch;
  while ((ch = getopt(argc, argv, "vd")) != -1) {
    switch (ch) {
    case 'v':
      verbose = 1;
      break;
    case 'd':
      debug = 1;
      break;
    }
  }
  argc -= optind;
  argv += optind;

  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    fprintf(stderr, "Case #%d/%d\n", t, T);
    int N, M, maxH = 0;
    cin >> N >> M;
    vector< vector <int> > G;
    map< int, vector<pair<int, int> > > H;
    for (int n = 0; n < N; n++) {
      for (int m = 0; m < M; m++) {
        if (m == 0) {
          vector<int>r;
          G.push_back(r);
        }
        int h;
        cin >> h;
        G[n].push_back(h);
        maxH = max(h, maxH);
        if (H.find(h) == H.end()) {
          vector< pair<int, int> >v;
          H[h] = v;
        }
        pair<int, int>p = make_pair(n, m);
        H[h].push_back(p);
      }
    }
    H.erase(maxH);
    bool ok = true;
    set<pair<int, int> > checked;
    for (map< int, vector<pair<int, int> > >::iterator it = H.begin(); it != H.end(); it++) {
      int h = it->first;
      vector< pair<int, int> >v = it->second;
      for (int i = 0; i < v.size(); i++) {
        pair<int, int>p = v[i];
        int r = p.first;
        int c = p.second;
        if (checked.find(make_pair(r, c)) != checked.end())
          continue;
        if (verbose)
          fprintf(stderr, "checking height %d at [%d,%d]\n", h, r, c);
        int okC = true;
        for (int p = 0; p < N; p++) {
          if (checked.find(make_pair(p, c)) != checked.end())
            continue;
          if (G[p][c] > G[r][c]) {
            okC = false;
            break;
          }
        }
        int okR = true;
        for (int q = 0; q < M; q++) {
          if (checked.find(make_pair(r, q)) != checked.end())
            continue;
          if (G[r][q] > G[r][c]) {
            okR = false;
            break;
          }
        }
        if (okC) {
          for (int p = 0; p < N; p++) {
            if (checked.find(make_pair(p, c)) == checked.end()) {
              checked.insert(make_pair(p, c));
            }
          }
        }
        if (okR) {
          for (int q = 0; q < M; q++) {
            if (checked.find(make_pair(r, q)) == checked.end()) {
              checked.insert(make_pair(r, q));
            }
          }
        }
        if (!okC && !okR) {
          ok = 0;
          break;
        }
      }
      if (!ok) {
        break;
      }
    }
    printf("Case #%d: %s\n", t, ok ? "YES" : "NO");
  }
}
