#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>


using namespace std;

#define FOR(i , n) for(int i = 0 ; i < n ; i++)
#define FOT(i , a , b) for(int i = a ; i < b ; i++)
int _a;
#define GETINT (scanf("%d" , &_a) , _a)
#define pb push_back
#define mp make_pair
#define s(a) (int(a.size()))
#define PRINT(a) cerr << #a << " = " << a << endl
#define ALL(a) a.begin(), a.end()


typedef long long ll;
typedef pair< ll , ll > PLL;
typedef vector< PLL > vpll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int , int> PII;
typedef vector< PII > vpii;

int R, N, M, K;
map<int, map < int, double > > productProb;
map<int, ld > curProb;
map<int, map < int, double > >::iterator myIt;

void generateProductProb() {
  productProb.clear();
  FOT(i, 2, M + 1) FOT(j, 2, M + 1) FOT(k, 2, M + 1) {
    int num = i * 100 + j * 10 + k;
    productProb[num] = map<int, double>();
    productProb[num][1] = 1.0 / 8;

    productProb[num][i] += 1.0 / 8;
    productProb[num][j] += 1.0 / 8;
    productProb[num][k] += 1.0 / 8;

    productProb[num][i * j] += 1.0 / 8;
    productProb[num][i * k] += 1.0 / 8;
    productProb[num][k * j] += 1.0 / 8;

    productProb[num][i * j * k] += 1.0 / 8;
  }
}

void solveCase() {
  R = GETINT;
  N = GETINT;
  M = GETINT;
  K = GETINT;

  generateProductProb();
  for (int i = 0; i < R; i++) {
    curProb.clear();
    for (int j = 0; j < K; j++) {
      int product = GETINT;
      for (myIt = productProb.begin(); myIt != productProb.end(); myIt++) {
        int origin = myIt -> first;
        map < int, double > probs = myIt -> second;
        ld prob;
        if (probs.find(product) == probs.end()) {
          prob = 0;
        } else prob = probs[product];
        if (curProb.find(origin) == curProb.end()) {
          if (j == 0) curProb[origin] = prob;
        } else {
          curProb[origin] *= prob;
        }
      }
    }
    int best = 222;
    ld bestProb = -1.0;
    for (map < int, ld >::iterator it = curProb.begin(); it != curProb.end(); it++) {
      int what = it -> first;
      ld prob = it -> second;
      if (prob > bestProb) {
        best = what;
        bestProb = prob;
      }
    }
    cout << best << endl;
  }
}

int main() 
{
  int t = GETINT;
  for (int test = 1; test <= t; test++) {
    printf("Case #%d:\n", test);
    solveCase();
  }
  return 0;
}
