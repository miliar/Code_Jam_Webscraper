#include<stdio.h>
#include<stdlib.h>

using namespace std;
int main()
{
  int T, t;
  scanf("%d", &T);
  for(t=1;t<=T;t++)
    {
      double C, F, X, time=0;
      int i, k;
      scanf("%lf %lf %lf", &C, &F, &X);
      k = (int) (X/C -2/F);
      if(k < 0) k=0;
      for(i=0;i<k;i++)
	time += C/(2+i*F);
      time += X/(2+(k*F));
      printf("Case #%d: %.7lf\n", t, time);
    }
}
