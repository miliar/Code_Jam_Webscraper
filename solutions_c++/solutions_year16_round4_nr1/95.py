#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<vi> vvi;

int N, R, P, S;

string bourrin(int n, char c)
{
  if (n == 0)
    return string(1, c);
  
  string res;
  
  if (c == 'R')
  {
    string a = bourrin(n-1, 'R');
    string b = bourrin(n-1, 'S');
    if (a < b)
      res = a + b;
    else
      res = b + a;
  }
  
  if (c == 'S')
  {
    string a = bourrin(n-1, 'S');
    string b = bourrin(n-1, 'P');
    if (a < b)
      res = a + b;
    else
      res = b + a;
  }
  
  if (c == 'P')
  {
    string a = bourrin(n-1, 'P');
    string b = bourrin(n-1, 'R');
    if (a < b)
      res = a + b;
    else
      res = b + a;
  }
  
  if (n == N)
  { 
    int nS = 0, nR = 0, nP = 0;
    for (auto c: res)
    {
      if (c == 'S') nS++;
      if (c == 'R') nR++;
      if (c == 'P') nP++;
    }
    if (nS != S) return "Z";
    if (nR != R) return "Z";
    if (nP != P) return "Z";
  }
  
  return res;
}

void main2()
{
  cin >> N >> R >> P >> S;
  
  string best = "Z";
  best = min(best, bourrin(N, 'S'));
  best = min(best, bourrin(N, 'P'));
  best = min(best, bourrin(N, 'R'));
  
  if (best == "Z")
    cout << "IMPOSSIBLE" << endl;
  else
    cout << best << endl;
}

int main()
{
  int T;
  cin >> T;
  for (int t=0; t<T; t++)
  {
    cout << "Case #" << t+1 << ": ";
    main2();
  }
}
