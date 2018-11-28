#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cassert>

using namespace std;
#define CHECK(x) assert(x)

struct LM {
  LM(int N, int M) : n(N), m(M), incnt(0) { d = new int[N*M]; }
  ~LM() { delete[] d; }
  void add(int v) { d[incnt++] = v; }
  bool test();
  int& at(int *p, int x, int y) { return p[y*m+x]; }
  int& at(int x, int y) { return d[y*m+x]; }
  int n, m;
  int *d;
  int incnt;
};

struct comp1 {
  bool operator()(const pair<int,int> &a, const pair<int,int> &b) {
    return a.first < b.first;
  };
};

bool LM::test() {
  CHECK(incnt == n*m);
  vector<int> rowmax(n, -1);
  vector<int> colmax(m, -1);
  for (int j = 0; j < n; j++)
    for (int i = 0; i < m; i++) {
      rowmax[j] = max(at(i,j), rowmax[j]);
      colmax[i] = max(at(i,j), colmax[i]);
    }
    
  for (int j = 0; j < n; j++)
    for (int i = 0; i < m; i++) {
      if (at(i,j) != rowmax[j] && at(i,j) != colmax[i]) {
cerr << "early filtered" << endl;
        return false;
      }
    }

  int *tmp = new int[n*m];
  for (int k = 0; k < n*m; k++) tmp[k] = 10000;
    
  vector<pair<int,int> > order(n+m);
  for (int j = 0; j < n; j++) order[j] = pair<int,int>(rowmax[j], j);
  for (int i = 0; i < m; i++) order[n+i] = pair<int,int>(colmax[i], 1000+i);
  sort(order.begin(), order.end(), comp1());
  
  while (order.size() > 0) {
    int h = order.back().first;
    int k = order.back().second;
    if (k < 1000) {
      for (int i = 0; i < m; i++) at(tmp,i,k) = min(h, at(tmp,i,k));
    } else {
      for (int j = 0; j < n; j++) at(tmp,k-1000,j) = min(h, at(tmp,k-1000,j));
    }
    order.pop_back();
  }

  bool r = true;
  for (int j = 0; j < n; j++)
    for (int i = 0; i < m; i++) {
      if (at(tmp,i,j) != at(i,j)) {
cerr << "late filtered" << endl;
        r = false;
        goto fin;
      }
    }
  
fin:
  delete[] tmp;
  return r;
}

int main(int argc, char *argv[]) {
  if (argc < 2) return -1;
  ofstream ofs;
  if (argc >= 3) ofs.open(argv[2]);
  ostream &os = (argc >= 3) ? ofs : cout;

  ifstream ifs;
  ifs.open(argv[1]);
  string s;
  
  int T;
  ifs >> T;
  for (int t = 1; t <= T; t++) {
    int N, M;
    ifs >> N >> M;
    int a;
    LM lm(N, M);
    for (int n = 0; n < N; n++)
      for (int m = 0; m < M; m++) {
        ifs >> a;
        lm.add(a);
      }
    os << "Case #" << t << ": " << (lm.test() ? "YES" : "NO") << endl;;
  }
  
  getline(ifs, s);
  getline(ifs, s);
  CHECK(ifs.eof());
  
  ifs.close();
  ofs.close();
  return 0;
}