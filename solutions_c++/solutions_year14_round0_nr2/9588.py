#include <iostream>
#include <cstdio>

using namespace std;

double C, F, X;

double dfs(double pck, double fcost, double mcost)
{
  double tfcost = fcost + C/pck;
  double cost = tfcost + X/(pck+F);

  if(cost > mcost) return mcost;
  return dfs(pck+F, tfcost, cost);
}

double solve()
{
  double mcost = X/2.0;
  double pck = 2.0;
  double fcost = 0;
  return dfs(pck, fcost, mcost);
}

int main()
{
  int tcs;

  cin >> tcs;
  for(int cs = 1; cs <= tcs; ++cs){
    cin >> C >> F >> X;
    printf("Case #%d: %.7lf\n", cs, solve());
  }

  return 0;
}
