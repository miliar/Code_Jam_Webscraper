#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#define LL long long
#define MP make_pair
#define PB push_back
#define ff first
#define ss second
#define DEBUG(x) cerr<<#x<<" "<<(x)<<endl;
#define LD long double
using namespace std;
const double INF = 1000000000;
int main()
{
  int t;
  scanf("%d", &t);
  for(int z=1; z<=t; z++)
  {
    printf("Case #%d: ", z);
    double C, F, X;
    double P = 2;
    double T = 0;
    scanf("%lf %lf %lf", &C, &F, &X);
    double ans = X/P;
    
    while(1)
    {
      T += C/P;
      P += F;
      if(T > ans)
	break;
      ans = min(ans, T + X/P);
    }
    printf("%.7lf\n", ans);
  }
  return 0;
}