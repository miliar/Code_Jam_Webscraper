#include <cstdio>

using namespace std;

int main()
{
  int tcase;
  scanf("%d",&tcase);
  for(int tnum = 1; tnum <= tcase; tnum++)
    {
      printf("Case #%d: ",tnum);
      
      double c,f,x;
      scanf("%lf%lf%lf",&c,&f,&x);//Cost,FarmProduce,Target
      //Initially 2 cookies per second
      double p = 2,ans = 0;

      //x / p > c / p + x / (p + f)
      while( (x - c) * (p + f) > x * p ) 
	{
	  ans += c / p;
	  p += f;
	}
      ans += x / p;

      printf("%.10f\n",ans);
    }
  return 0;
}
