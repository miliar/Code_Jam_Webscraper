#include <cstdio>
#include <algorithm>
using namespace std;

typedef long long int ll;
double X,F,C;

double solve(int nC)
{
  double ans=0;
  double R = 2.0;
  for(int i = 0; i < nC;i++)
    {
      ans = ans + C/R;
      R += F;
    }
  ans += X/R;
  return ans;
}


double bruteForceSearch()
{
  double ans = solve(0);
  for(int i = 1; i < (X+1/2);i++)
    ans = min(ans,solve(i));
  return ans;
}
double ternarySearch()
{
  int l=0,r=X+1,lT,rT;
  while(r-l>3)
    {
      lT = l+(r-l)/3;
      rT = r-(r-l)/3;
      if(solve(lT) < solve(rT))
	r = rT;
      else
	l = lT;
    }
  double ans = solve(max(0,l-1));
  for(int i = l; i <= r;i++)
    ans = min(ans,solve(i));
  return ans;
  }
int main()
{
  int T;
  scanf(" %d",&T);
  for(int t = 1; t <= T;t++)
    {
      scanf("%lf %lf %lf",&C,&F,&X);
      printf("Case #%d: ",t);
	    
      
      printf("%.7lf\n",ternarySearch());
      
    }
  return 0;
}
