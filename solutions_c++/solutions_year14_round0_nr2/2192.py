#include <cstdio>
#include <cmath>
int main()
{
      freopen("B-large.in","r",stdin);
      freopen("output.out2","w",stdout);

      int cases, i;
      scanf("%d",&cases);
    
      for(int c = 1 ; c <=cases ; c++)
      {
            double tN=0, ttN=0, N=0;
            double C, F, X;
            scanf("%lf%lf%lf",&C,&F,&X);

            //tN=((2*(X/(X-C))-2-F)/(F-F*(X/(X-C))));
            if (X>C)
            {
                tN=ceil((F*X-2*C-C*F)/(F*C));
                //tN=ceil((2*(X/(X-C))-2-F)/(F-F*(X/(X-C))));
                for (i=0; i<=tN-1; i++)
                {
                    ttN=C/(2+F*(i));
                    N=N+ttN;
                }
                N=N+X/(2+F*(tN));
            }
            //if (C>=X)
            else
            {
                  N=(X/2);
            }
          printf("Case #%d: %.7lf\n",c,N);
      }
      return 0 ;
}
