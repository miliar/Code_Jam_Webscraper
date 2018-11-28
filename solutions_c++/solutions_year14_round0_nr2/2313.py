//Program: b
//Author: gary
//Date: 12/04/2014
#include <bits/stdc++.h>
using namespace std;
#define SZ(x) ( (int) (x).size() )
#define mp make_pair
#define pb push_back
#define fi first
#define se second
typedef pair<int, int> i2;
typedef long long ll;
const int INF = 1e9;
const int N = 100;

double solve()
{
  double C, F, X, R;
  double t = 0, res = INF; // upper bound is actually maxX / 2.0 (default R value)
  cin >> C >> F >> X;
  R = 2.0;
  while(1)
  {
    if(res > t + X / R)
    {
      res = t + X / R;
    } 
    else 
    {
      break;
    }
    t += C / R;
    R += F;
  }
  return res;
}

int main()
{
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++)
  {
    printf("Case #%d: %.7f\n", i, solve());
  }

  return 0;
}
