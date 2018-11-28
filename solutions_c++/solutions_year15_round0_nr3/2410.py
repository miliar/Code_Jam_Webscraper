#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#define MAXL 40000
#define ll long long
using namespace std;

int T = 0;
struct Quan{
public:
  explicit Quan(){
    t = x = y = z = 0;
  }
  explicit Quan(int _t, int _x, int _y, int _z){
    t = _t;
    x = _x;
    y = _y;
    z = _z;
  };
  explicit Quan(char c){
    t = x = y = z = 0;
    switch (c) {
    case 'i':x = 1; break;
    case 'j':y = 1; break;
    case 'k':z = 1; break;
    default:
      break;
    }
  };
  int t;
  int x;
  int y;
  int z;
};

Quan operator*(Quan& p, Quan& q){
  auto a = q.t;
  auto b = q.x;
  auto c = q.y;
  auto d = q.z;
  auto t = p.t;
  auto x = p.x;
  auto y = p.y;
  auto z = p.z;
  return Quan(a*t-b*x-c*y-d*z,b*t+a*x+d*y-c*z,c*t+a*y+b*z-d*x,d*t+z*a+c*x-b*y);
}

bool operator==(Quan& p, Quan& q){
  return p.t == q.t && p.x == q.x && p.y == q.y && p.z == q.z;
}

Quan Qi('i');
Quan Qj('j');
Quan Qk('k');
Quan Q1(1, 0, 0, 0);

Quan pow(Quan& p,int n){
  switch (n) {
  case 0: return Q1;
  case 1: return p;
  case 2: return p*p;
  case 3: return p*p*p; 
  default:
    break;
  }
}

Quan l[MAXL];
Quan r[MAXL];

void solve(ifstream& fin,ofstream& fout){
  int T = 0;

  fin >> T;
  for (size_t t = 0; t < T; t++) {
    int L = 0;
    ll X = 0;
    fin >> L >> X;
    string s;
    fin >> s;
    l[0] = Quan(1, 0, 0, 0);
    r[0] = Quan(1, 0, 0, 0);
    for (size_t i = 1; i < 4*L; i++) {
      auto p = (i - 1) % L;
      l[i] = l[i - 1] * Quan(s[p]);
      r[i] = Quan(s[L - p - 1]) * r[i - 1];
    }
    int m = X & 3;
    Quan total = pow(l[L], m);
    ll fi = X*L + 1;
    ll fk = X*L + 1;
    for (size_t i = 0; i < 4*L; i++) {
      if (l[i] == Qi) {
        fi = ll(i);
        break;
      }
    }
    for (size_t i = 0; i < 4 * L; i++) {
      if (r[i] == Qk) {
        fk = ll(i);
        break;
      }
    }
    if (total == Quan(-1, 0, 0, 0) && fi + fk < X*L)
      fout << "Case #" << t + 1 << ": " << "YES" << endl;
    else
      fout << "Case #" << t + 1 << ": " << "NO" << endl;
  }
}