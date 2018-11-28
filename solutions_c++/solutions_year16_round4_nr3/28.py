#include <bits/stdc++.h>

using namespace std;
#define MP make_pair
#define PB push_back
#define st first
#define nd second
#define FI st
#define SE nd
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define RE(i,n) FOR(i,1,n)
#define REP(i, n) FOR(i, 0, (int)(n)-1)
#define R(i,n) REP(i,n)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define PII pair<int,int>
#define VI vector<int>
template<class C> void mini(C&a, C b){a=min(a,b);}
template<class C> void maxi(C&a, C b){a=max(a,b);}

template<class TH> void _dbg(const char* sdbg, TH h){cerr<<sdbg<<"="<<h<<"\n";}
template<class TH, class... TA> void _dbg(const char* sdbg, TH h, TA... t){
  while(*sdbg!=',')cerr<<*sdbg++; cerr<<"="<<h<<","; _dbg(sdbg+1, t...);
}

template<class T> ostream& operator<<(ostream& os, vector<T> V) {
  os << "["; for(auto vv : V) os << vv << ","; return os << "]";
}
template<class T> ostream& operator<<(ostream& os, set<T> V) {
  os << "{"; for(auto vv : V) os << vv << ","; return os << "}";
}
template<class LL, class RR> ostream& operator<<(ostream& os, pair<LL,RR> V) {
  return os << "(" << V.first << ", " << V.second << ")";
}

#ifdef LOCAL
#define debug(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#else
#define debug(...) (__VA_ARGS__)
#endif


struct Test {
  int R, C, N;
  vector<int> from, to;
  vector<string> result;
  vector<bool> still;
  vector<int> StartY, StartX;
  set<pair<int, int>> isInside, visited, possible, inpath;
  vector<pair<int, int>> paths;
  map<PII, pair<PII, PII>> mapping;
  int MinX[100], MaxX[100];

  vector<pair<int, int>> neighbors(pair<int, int> P, int d = 2) {
    vector<PII> res;
    for (int di = -1; di <= 1; di++) {
      for (int dj = -1; dj <= 1; dj++) {
        if (d == 1 && abs(di) + abs(dj) == 2) { continue; }
        PII Q{P.first + di, P.second + dj};
        if (isInside.count(Q)) {
          res.PB(Q);
        }
      }
    }
    return res;
  }

  void run(int testid) {
    cin >> R >> C;
    result = vector<string>(R, string(C, '.'));
    N = R + C;
    still = vector<bool>(2 * N, true);

    {
    int y = 0, x = R;
    for (int i = 0; i < C; i++) {
      StartY.PB(y); StartX.PB(x); y++; x++;
    }
    x--;
    for (int i = 0; i < R; i++) {
      StartY.PB(y); StartX.PB(x); y++; x--;
    }
    y--;
    for (int i = 0; i < C; i++) {
      StartY.PB(y); StartX.PB(x); y--; x--;
    }
    x++;
    for (int i = 0; i < R; i++) {
      StartY.PB(y); StartX.PB(x); y--; x++;
    }

    for (int row = 0; row < R; row++) {
      y = StartY[2 * N - row - 1];
      x = StartX[2 * N - row - 1];
      mapping[MP(y, x)] = MP(MP(row, -1), MP(row, 0));
      for (int j = 0; j <= C; j++) {
        y++; x++;
        mapping[MP(y, x)] = MP(MP(row, j), MP(row, j + 1));
      }
    }

    for (int col = 0; col < C; col++) {
      y = StartY[col]; x = StartX[col];
      mapping[MP(y, x)] = MP(MP(-1, col), MP(0, col));
      for (int j = 0; j <= R; j++) {
        y++; x--;
        mapping[MP(y, x)] = MP(MP(j, col), MP(j + 1, col));
      }
    }

    }
    for (int i = 0; i < N; i++) {
      int minX = 1e9, maxX = -1e9;
      for (int j = 0; j < 2 * N; j++) {
        if (StartY[j] == i) {
          mini(minX, StartX[j]);
          maxi(maxX, StartX[j]);
        }
      }
      MinX[i] = minX;
      MaxX[i] = maxX;

      for (int x = minX; x <= maxX; x++) {
        isInside.insert(make_pair(i, x));
      }
    }


    for (int i = 0; i < N; i++) {
      int a, b;
      cin >> a >> b;
      a--; b--;
      if (a > b) { swap(a, b); }
      from.PB(a);
      to.PB(b);
    }

    cout << "Case #" << testid << ": " << endl;

    for (int iter = 0; iter < N; iter++) {
      int chosen = -1;

      for (int i = 0; i < N; i++) {
        if (!still[from[i]]) { continue; }

        int F = from[i], T = to[i];
        bool fail = false;
        for (int j = F + 1; j < T; j++) {
          if (still[j]) { fail = true; }
        }

        if (!fail) { chosen = i; break; }
      }
      debug("", chosen);

      if (chosen == -1) {
        cout << "IMPOSSIBLE\n";
        return;
      }

      int F = from[chosen], T = to[chosen];
      debug(F, T);

      possible.clear();
      inpath.clear();
      for (int i = 0; i < N; i++) {
        if (from[i] > F && from[i] < T) {
          possible.insert(make_pair(StartY[from[i]], StartX[from[i]]));
          possible.insert(make_pair(StartY[to[i]], StartX[to[i]]));
        }
      }

      debug(possible);

      bool chg;
      do {
        chg = false;
        auto PP = possible;
        for (auto P : PP) {
          for (auto Q : neighbors(P)) {
            if (visited.count(Q) && !possible.count(Q)) {
              chg = true;
              possible.insert(Q);
            }
          }
        }
      } while (chg);

      auto PP = possible;
      auto FF = MP(StartY[F], StartX[F]),
           TT = MP(StartY[T], StartX[T]);

      for (auto P : PP) {
        for (auto Q : neighbors(P)) {
          if (!visited.count(Q)) { inpath.insert(Q); }
        }
      }
      for (auto A : neighbors(FF, 1)) {
        for (auto B : neighbors(TT, 1)) {
          if (A == B && !visited.count(A)) { inpath.insert(A); }
        }
      }
      inpath.insert(FF); inpath.insert(TT);
      debug(inpath);

      map<PII, int> dist;
      map<PII, PII> prevGood;
      map<PII, tuple<int,int,char>> prevChg;
      queue<PII> Q;
      Q.push(FF);

      while (!Q.empty()) {
        auto cur = Q.front(); Q.pop();
        for (auto I : inpath) {
          if (abs(I.first - cur.first) + abs(I.second - cur.second) != 1) { continue; }
          if (visited.count(I)) { continue; }
          if (dist[I] || I == FF) { continue; }

          char ch = (I.first != cur.first) ? '\\' : '/';

          auto P = MP(-1, -1);
          for (auto A : {mapping[cur].first, mapping[cur].second}) {
            for (auto B : {mapping[I].first, mapping[I].second}) {
              if (A == B) {
                P = A;
              }
            }
          }

          debug(P, ch, I, cur);
          /*if (result[P.first][P.second] != '.' && result[P.first][P.second] != ch) {
            cout << "IMPOSSIBLE\n";
            return;
          }
          result[P.first][P.second] = ch; */

          dist[I] = dist[cur] + 1;
          prevGood[I] = cur;
          prevChg[I] = make_tuple(P.first, P.second, ch);
          Q.push(I);
        }
      }

      debug(FF, TT);
      if (!dist[TT]) {
        cout << "IMPOSSIBLE\n";
        return;
      }

      auto cur = TT;
      while (cur != FF) {
        int r, c;
        char ch;
        tie(r, c, ch) = prevChg[cur];
        if (result[r][c] != '.' && result[r][c] != ch) { cout << "IMPOSSIBLE\n"; return; }
        result[r][c] = ch;
        cur = prevGood[cur];
        visited.insert(cur);
      }
      
      visited.insert(MP(StartY[T], StartX[T]));
      debug(chosen);
      still[from[chosen]] = still[to[chosen]] = false;

      for (auto S : result) {
        debug(S);
      }
    }

    for (auto S : result) {
      for (char &ch : S) { if (ch == '.') { ch = '/'; } }
      cout << S << "\n";
    }
  }

};


int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout << fixed << setprecision(11);
  cerr << fixed << setprecision(6);

  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cerr << i << "\n";
    Test test;
    test.run(i);
  }

  return 0;
}
