#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>
#include <numeric>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define pb push_back
#define sz(v) ((int)(v).size())

int main()
{
  int i=0,j=0,k=0; char buf[100000]="";
  int _cases=0, _case=0;
  scanf("%d",&_cases);
  for(_case=1;_case<=_cases;_case++) {
    double C, F, X;
    scanf("%lf %lf %lf", &C, &F, &X);
    double best=50000;
    double t=0;
    int farms=0;
    while(t<50000.0&&farms<1000000) {
      double persec = 2.0 + F*farms;
      double dt_without_extra_farms = X / persec;
      best = min(best, t + dt_without_extra_farms);
      double dt_for_extra_farm = C / persec;
      t += dt_for_extra_farm;
      farms++;
    }

    printf("Case #%d: %.7lf\n", _case, best);
  }
  return 0;
}
