#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <cmath>
#include <bitset>
#include <list>
#include <queue>
#include <sstream>

using namespace std;

#define e '\n'
#define INF 1023456789
#define ll long long

//#define FILE "data"

#ifdef FILE
ifstream f(string (string(FILE) + ".in").c_str());
ofstream g(string (string(FILE) + ".out").c_str());
#endif
#ifndef FILE
#define f cin
#define g cout
#endif

#ifdef CLION
#undef f
#undef g
ifstream f("data.in");
#define g cout
#endif

ll mul_inv(ll a, ll b) {
  ll b0 = b, t, q;
  ll x0 = 0, x1 = 1;
  if (b == 1) return 1;
  while (a > 1) {
    q = a / b;
    t = b, b = a % b, a = t;
    t = x0, x0 = x1 - q * x0, x1 = t;
  }
  if (x1 < 0) x1 += b0;
  return x1;
}

ll t, n, rez, x, m, k, r, p, s;
int i, j, ii;
string s1, s2;

string pp[15];
string rr[15];
string ss[15];
ll v[15][4];
double bestProbs;

double probs[205];
double initProbs[205];
int chosen[205];

double getProbs() {
  for (int i = 0; i <= k; i++) {
    probs[i] = 0.0;
  }
  probs[0] = 1.0;

  for (int i = 1; i <= k; i++) {
    for (int j = k; j > 0; j--) {
      probs[j] = probs[j] * (1 - initProbs[chosen[i]]) + probs[j - 1] * initProbs[chosen[i]];
    }
    probs[0] = probs[0] * (1 - initProbs[chosen[i]]);
  }

  return probs[k / 2];
}

void permute(int pos) {
  if (pos > k) {
    double prob = getProbs();

    if (prob > bestProbs) {
      bestProbs = prob;
    }


    return;
  }

  while (chosen[pos] < n) {
    chosen[pos]++;
    chosen[pos + 1] = chosen[pos];
    permute(pos + 1);
  }

}

int main() {
  f >> t;

  g << fixed << setprecision(7);

  for (int ii = 1; ii <= t; ii++) {

    f >> n >> k;

    for (int i = 1; i <= n; i++) {
      f >> initProbs[i];
    }

    for (int i = 1; i <= k; i++) {
      chosen[i] = 0;
    }

    bestProbs = 0.0;
    permute(1);

    g << "Case #" << ii << ": " << bestProbs << e;
  }
}
