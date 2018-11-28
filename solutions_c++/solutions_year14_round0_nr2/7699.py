#include<iostream>
#include<vector>
#include<cstdio>
#include<string>
#include<algorithm>
#include<numeric>
#include<map>
#include<math.h>

using namespace::std;

int main(void)
{
  int T;
  double C , F , X;

  cin >> T;

  for(int i = 1; i <= T; i++)
    {
      cin >> C >> F >> X;
      double min_time = X / 2;
      double c = 2;
      double cost_time_sum = C / c;

      while(1)
	{
	  if( min_time > cost_time_sum + (X / (F+c)) )
	    {
	      min_time = cost_time_sum + (X / (F+c));
	      c += F;
	      cost_time_sum += (C / c);
	    }
	  else
	    {
	      printf("Case #%d: %.7f\n" , i , min_time);
	      break;
	    }
	}
    }



  return 0;
}
