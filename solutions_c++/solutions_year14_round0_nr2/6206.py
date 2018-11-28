#include <stdio.h>
#include <malloc.h>
#include <math.h>
#include <vector>
#include <stdlib.h>

FILE *fpIn;
FILE *fpOut;
double C;
double F;
double X;

bool fequal(double a, double b)
{
   return fabs(a - b) <= 0.00001;
}

double process()
{
   printf(".");

   double worstCaseTime = X / 2.0;
   
   double time = 0;
   double numberOfCookies = 0;
   double cookiePerSecond = 2;
   double resolution = 1000000;//1000000

   {
      double cookiesToReachC = C - numberOfCookies;
      double timeItWillTakeToReachC = cookiesToReachC / cookiePerSecond;

      if (cookiesToReachC > 0 && timeItWillTakeToReachC > 0)
      {
         time += timeItWillTakeToReachC;
         numberOfCookies += cookiesToReachC;
      }
   }

   if (numberOfCookies > X)
   {
      return worstCaseTime;
   }

   while (true)
   {
      if (fequal(numberOfCookies, X) || numberOfCookies >= X)
      {
         return time;
      }

      if (fequal(numberOfCookies, C) || numberOfCookies >= C)
      {
         double time1 = time;
         double time2 = time;
         {
            // buy
            {
               double cookieLeftToGet = X - (numberOfCookies - C);
               time1 += cookieLeftToGet / (cookiePerSecond + F);
            }

            // not buy
            {
               double cookieLeftToGet = X - (numberOfCookies);
               time2 += cookieLeftToGet / cookiePerSecond;
            }
         }

         bool worthBuy = time1 < time2;
         if (worthBuy)
         {
            numberOfCookies -= C;
            cookiePerSecond += F;
         }
         else
         {
            double cookiesToReachX = X - numberOfCookies;
            double timeItWillTakeToReachX = cookiesToReachX / cookiePerSecond;

            if (cookiesToReachX > 0 && timeItWillTakeToReachX > 0)
            {
               time += timeItWillTakeToReachX;
               numberOfCookies += cookiesToReachX;
            }

            return time;
         }
      }
      else
      {
         double cookiesToReachC = C - numberOfCookies;
         double timeItWillTakeToReachC = cookiesToReachC / cookiePerSecond;

         if (cookiesToReachC > 0 && timeItWillTakeToReachC > 0)
         {
            time += timeItWillTakeToReachC;
            numberOfCookies += cookiesToReachC;
         }
         else
         {
            time += ((double)1 / resolution);
            numberOfCookies += cookiePerSecond / resolution;
         }
      }

      //time += ((double)1 / resolution);
      //numberOfCookies += cookiePerSecond / resolution;
   }
}

int main()
{
   int T;  
   double ret;

   fpIn = fopen("c:\\gcj\\in_c", "r");
   fpOut = fopen("c:\\gcj\\out_c", "w");

   fscanf(fpIn, "%d\n", &T);

   for (int i = 0; i < T; ++i)
   {
      fscanf(fpIn, "%lf %lf %lf\n", &C, &F, &X);
      
      fprintf(fpOut, "Case #%d: ", i + 1);
      ret = process();
      fprintf(fpOut, "%.7lf\n", ret);
   }

   fclose(fpIn);
   fclose(fpOut);

   system("pause");

   return 0;
}