#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
//#include <utility>
//#include <set>
//#include <map>
//#include <queue>
#include <iomanip>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vint;
//typedef vector<string> vstr;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

vector<int> p;

int solve(int t) {
  int d = p.size();
  for (int moves = 0; moves < t; moves++) {
    int eat = t - moves;
    int i = 0;
    while (i < d && p[i] <= eat) i++;
    int move_need = 0;
    while (i < d) {
      move_need += (p[i] - 1) / eat;
      i++;
    }
    if (move_need <= moves) return true;
  }
  return false;
}


int main()
{
  int tcase = 0;
  ifstream fin("z.in");
  ofstream fout("z.out");
  fin >> tcase;
  for (int tind = 1; tind <= tcase; tind++) {
    int d;
    fin >> d;
    p.clear();
    p.resize(d);
    for (int i = 0; i < d; i++) {
      fin >> p[i];
    }
    sort(p.begin(), p.end());
    int mint = 0, maxt = p[d-1];
    while (mint + 1 < maxt) {
      int mid = (mint + maxt) / 2;
      if (solve(mid))
        maxt = mid;
      else
        mint = mid;
    }
    fout << "Case #" << tind << ": " << maxt << endl;
  }
  return 0;
}
