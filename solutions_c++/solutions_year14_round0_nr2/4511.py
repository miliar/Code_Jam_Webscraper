#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

//for each number of farm, what time do we reach C and X ? (tc, tx)
//if new_tx > tx then output tx

int main()
{
  int nbcas;
  scanf("%d",&nbcas);
  for(int cas = 1; cas <= nbcas; cas++)
    {
      double c,f,x;
      scanf("%lf%lf%lf",&c,&f,&x);
      double speed = 2.0;
      double tx = x / speed;
      double tc = c / speed;
      int nc = 0;
      while(true)
	{
	  nc++;
	  speed += f;
	  double new_tx = tc + x / speed;
	  if(new_tx > tx)
	    {
	      printf("Case #%d: %.7lf\n",cas,tx);
	      break;
	    }
	  tx = new_tx;
	  tc += c / speed;
	}
    }
  return 0;
}
