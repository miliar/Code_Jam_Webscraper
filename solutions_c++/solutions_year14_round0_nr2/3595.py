#include <iostream>
#include <iomanip>
#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

double res;
double C, F, X, R;


void readInput()
{
  cin >> C >> F >> X;
}

double buyOne()
{
  double withone = C/R + X/(F+R);
  double without = X/R;
  if (withone < without)
    {
      res = res + C/R;
      R = R+F;
      return true;
    }
  else
    return false;
  
  
}

void solve()
{
  R = 2.0;
  res = 0.0;
  while(buyOne())
    {}
  res = res+X/R;
}

int main(int arc, char* argv[])
{
  int T;
  cin >> T;
  rep(cas,T)
    {
      readInput();
      solve();
      cout << "Case #" << cas +1 <<  ": " << setprecision(8) << fixed << res << endl;
    }
}

