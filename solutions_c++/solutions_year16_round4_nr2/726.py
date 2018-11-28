#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

vector<double> probs;

inline int popcount(int bmap) {
  int resp=0;
  while (bmap>0) {
    resp += (bmap&1);
    bmap>>=1;
  }
  return resp;
}

double myMax(double a, double b) {
  return (a>b?a:b);
}

map<pair<int,pair<int,int> >, double> memo;
double bestprob(int from, int yes, int no) {
  if (yes<0 || no<0)
    return 0;
  if (from == probs.size()) {
    return (yes+no==0 ? 1 : 0);
  }
  pair<int,pair<int,int> > input(from, make_pair(yes, no));
  if (memo.count(input))
    return memo[input];
  double ret = myMax(bestprob(from+1, yes, no), bestprob(from+1, yes-1, no)*probs[from] + bestprob(from+1, yes, no-1)*(1-probs[from]));
  memo[input] = ret;
  //cout << from << ' ' << yes << ' ' << no << ' ' << ret << endl;
  return ret;
}

int main() {
  int t;
  cin >> t;
  for (int ta=1; ta<=t; ++ta) {
    cout << "Case #" << ta << ": ";
    int n, k;
    cin >> n >> k;
    vector<double> input(n);
    for (int i=0;i<n;++i)
      cin >> input[i];
    double best = 0;
    for (int bmap=0; bmap < (1<<n); ++bmap) {
      if (popcount(bmap)==k) {
        memo.clear();
        probs.clear();
        for (int b=0;b<n;++b) {
          if (bmap & (1<<b))
            probs.push_back(input[b]);
        }
        best = myMax(best, bestprob(0, k/2, k/2));
      }
    }
    cout << best << endl;
  }
}