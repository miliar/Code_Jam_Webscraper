#include <cstdio>

int main()
{
   int nbT;
   scanf("%d", &nbT);
   for(int test=0; test<nbT; test++)
   {
      long double cost, prod, goal;
      scanf("%Lf%Lf%Lf", &cost, &prod, &goal);

      long double t = 0;
      long double p=2;
      while(1)
      {
         long double t1 = goal/p;
         long double t2 = cost/p + goal/(p+prod);
         if(t1 <= t2)
         {
            t += t1;
            break;
         }
         t += cost/p;
         p += prod;
      }

      printf("Case #%d: %.07Lf\n", test+1, t);
   }
   return 0;
}
