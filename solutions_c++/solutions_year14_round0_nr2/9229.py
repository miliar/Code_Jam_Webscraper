#include <cstdio>
#include <algorithm>

int main()
{
  int ntest;
  double X, C, F, cr = 2.0 , cc = 0.0 , t = 0.0 ;

  scanf(" %d", &ntest);

  for (int i = 1; i <= ntest; ++i)
  {
    scanf(" %lf %lf %lf", &C, &F, &X );

    if(i > 1)
      printf("\n");

    printf("Case #%d: ", i);

    cr = 2.0;
    cc = t = 0.0;
    while( cc < X )
    {
      if( X/cr <= C/cr + X/(cr + F) )
      {
        cc += X; 
        t  += X/cr;
      }
      else
      {
        t += C/cr;
        cr += F;
      }      
    }

    printf("%.7lf", t);
  }




  return 0;
}
