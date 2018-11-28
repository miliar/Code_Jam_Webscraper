#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define TRACE(x) cerr << "TRACE(" #x ")" << endl;
#define DEBUG(x) cerr << #x << " = " << (x) << endl;

typedef long long LL;
typedef unsigned long long ULL;
const int INF = 1000000000; const LL INFLL = LL(INF) * LL(INF);
template<class T> inline int size(const T&c) { return c.size(); }

int SY,SX;
vector<int> colors;

void ReadInput() {
  cin >> SY >> SX;
  colors.assign(2*(SY+SX), -1);
  REP(col, SY+SX) {
    REP(i,2) {
      int a; cin >> a;
      --a;
      colors[a] = col;
    }
  }
}

vector<string> board;

struct Edge {
  int x1,y1,x2,y2;
};

void PickPair(int &start, int &end) {
  start = -1;
  int col = -1;
  REP(i,size(colors)) {
    if(colors[i]==-1) continue;
    if(colors[i]==col) {
      end = i;
      return;
    }
    col = colors[i];
    start = i;
  }
  throw 0;
}

Edge MakeEdge(int idx) {
  assert(idx>=0);
  if(idx<SX) return {idx,0,idx+1,0};
  idx-=SX;
  if(idx<SY) return {SX,idx,SX,idx+1};
  idx-=SY;
  if(idx<SX) return {SX-idx, SY, SX-idx-1, SY};
  idx -= SX;
  assert(idx<SY);
  return {0, SY-idx, 0, SY-idx-1};
}

void FixOneColor() {
  int start;
  int end;
  PickPair(start, end);
  Edge e = MakeEdge(start);
  Edge goal = MakeEdge(end);
  for(;;) {
    assert(abs(e.x1-e.x2) + abs(e.y1-e.y2) == 1);
    if(e.x2 > e.x1) {
      if(e.y1 == SY) break;
      char &c = board[e.y1][e.x1];
      if(c=='?') c='\\';
      if(c=='\\') {
        e.x1++;
        e.y1++;
      } else {
        e.x2--;
        e.y2++;
      }
    } else if (e.y2 < e.y1) {
      if(e.x1==SX) break;
      char &c = board[e.y2][e.x1];
      if(c=='?') c='/';
      if(c=='/') {
        ++e.x1;
        --e.y1;
      } else {
        ++e.x2;
        ++e.y2;
      }
    } else if (e.x2 < e.x1) {
      if(e.y1==0) break;
      char &c = board[e.y1-1][e.x2];
      if(c=='?') c='\\';
      if(c=='\\') {
        --e.x1;
        --e.y1;
      } else {
        ++e.x2;
        --e.y2;
      }
    } else if (e.y2 > e.y1) {
      if(e.x1==0) break;
      char &c = board[e.y1][e.x1-1];
      if(c=='?') c='/';
      if(c=='/') {
        --e.x1;
        ++e.y1;
      } else {
        --e.x2;
        --e.y2;
      }
    } else {
      assert(false);
    }
  }
  if(e.x1 == goal.x2 && e.y1 == goal.y2 && e.x2 == goal.x1 && e.y2 == goal.y1) {
    colors[start] = -1;
    colors[end] = -1;
  } else {
    throw 0;
  }
}

vector<string> Calc() {
  try {
    board.assign(SY, string(SX, '?'));
    REP(i,SY+SX) FixOneColor();
    REP(y,SY) REP(x,SX) {
      char &c = board[y][x];
      if(c=='?') c='/';
    }
    return board;
  } catch(int) {
    return {"IMPOSSIBLE"};
  }
}

int main(int argc, char **argv) {
  int ntc; cin >> ntc;
  FOR(tc,1,ntc) {
    ReadInput();
    if(argc==2 && tc!=atoi(argv[1])) continue;
    auto res = Calc();
    cout << "Case #" << tc << ":\n";
    for(string line: res) cout << line << "\n";
  }
}

