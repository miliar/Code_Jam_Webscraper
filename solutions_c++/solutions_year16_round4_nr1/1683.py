#include <cstdio>
#include <cstring>
#include <cmath>

int n, a, b, c;


void work(int n, int a, int b, int c)
{
   fprintf(stderr, "%d %d %d %d\n", n, a, b, c);
   if (n == 2)
   {
      if (a == 2)
         printf("PRRS");
      if (b == 2)
         printf("PRPS");
      if (c == 2)
         printf("PSRS");
      return;
   }
   if (n == 1)
   {
      if (b == 1)
         printf("P");
      if (a == 1)
         printf("R");
      if (c == 1)
         printf("S");
      return;
   }
   int ta = a / 2 + a % 2;
   int tb = b / 2 + b % 2;
   int tc = (1 << (n - 1)) - ta - tb;
   if (c < b && c < a)
   {
       tc = c / 2;
       ta = (1 << (n - 1)) - tb - tc;
   }
   work(n - 1, ta, tb, tc);
   work(n - 1, a - ta, b - tb, c - tc);
}

int main() {
   int T;
   scanf("%d", &T);
   for (int ttt = 1; ttt <= T; ++ttt)
   {
   	    printf("Case #%d: ", ttt);

   	    scanf("%d %d %d %d\n", &n, &a, &b, &c);

          bool flag = true;
          int ta = a, tb = b, tc = c;
          int t = 1 << n;
          if (n == 1)
          {
            if (ta == 2 || tb == 2 || tc == 2)
               flag = false;
         }
         else if (n == 2)
         {
            if (ta == 0 || tb == 0 || tc == 0)
               flag = false;
         }
         else
         {
            t /= 2;
          if (a >= t || b >= t || c >= t)
            flag = false;
      }
         //  if (b > ta)
         //    ta = b;
         // if (c > ta)
         //    ta = c;
          // // int t = 1 << n;
          // for (int i = n; i ; --i)
          // {
          //   // t /= 2;
          //   if (ta > i / 2)
          //   {
          //      flag = false;
          //      break;
          //   }
          //   ta = ta / 2 + ta % 2;
          // }
          if (flag)
            work(n, a, b, c);
   //          while (a || b || c){
   // // fprintf(stderr, "%d %d %d %d\n", n, a, b, c);
   //             if (a && b && a >= c)
   //             {
   //                printf("PR");
   //                --a; --b;
   //             }
   //             if (b && c)
   //             {
   //                printf("PS");
   //                --b; --c;
   //             }
   //             if (a && c)
   //             {
   //                printf("RS");
   //                --a; --c;
   //             }
            // }
         else
            printf("IMPOSSIBLE");
         printf("\n");
   }

   return 0;
}