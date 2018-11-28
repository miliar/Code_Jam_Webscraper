#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int check(int a[4][4], int b[4][4], int row1, int row2)
{
  int i =0, j=0;
  int val = -1;
  int count = 0;
  //printf("%d %d %d %d \n", a[row1][0], a[row1][1] , a[row1][2], a[row1][3]);
  //printf("%d %d %d %d \n", b[row2][0], b[row2][1] , b[row2][2], b[row2][3]);

  for (i=0;i<4 ;i++)
  {
    for (j=0; j < 4 ; j++)
      if(a[row1][i] == b[row2][j])
      {
         val = a[row1][i];
         count++;
      }
  }
  if (count == 1)
     return val;
  if (count > 1)
     return -999;
  if (count ==0)
     return -1;
}

int main()
{
    int i=0, j=0, t1, t2 =0;
    double min=-1.0, max, total; 
    double C, F, X, farm =0;
    double Xx, ck=2.0;

    cin >> t2;

    for (int t1 = 1; t1 <= t2; ++t1) {
      
      cin >> C >> F >> X;
      
      //printf("\n\n TEST CASES : Cookies : %f , F : %f , Total Req: %f\n", C, F, X);

      max = X/2;
      if (max < 1)
        max = 1;
      min = max;
      farm = 0.0;
      ck = 2.0;
      Xx = 0.0;
      for (i = 0; i < X; i++)
      {

         farm = farm + C/ck;
         ck = ck + F;
         Xx = X/ck;

        
         total = farm + Xx;

       //  printf("Farm[%f] : %f + %f : %f [ %f > %f]\n", ck,farm, Xx,total, max, min) ;
         
         if (total > max) break;
         if (min  == -1)
            min = total;
         if (min > total)
            min = total;

      }      

      printf("Case #%d: %.7f \r\n", t1, min) ;
    }

}
