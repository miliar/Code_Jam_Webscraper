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
    //freopen("magic.in", "r", stdin);
    //freopen("a1.out", "w", stdout);
    int i=0, j=0, k =0;
    int a[4][4], b[4][4];
    int t2; int row1, row2, val=-1;
    cin >> t2;
    //printf("total test cases : %d\n", t2);

    for (int t1 = 1; t1 <= t2; ++t1) {

      cin >> row1;
      for (i = 0;i<4; i++) {
        cin >> a[i][0] >> a[i][1] >> a[i][2] >> a[i][3];
      }

      cin >> row2;
      for (i = 0;i<4; i++)
      {
        cin >> b[i][0] >> b[i][1] >> b[i][2] >> b[i][3];
      }

      row1 = row1 -1;
      row2 = row2 -1;
      //printf("TEST CASES : %d processing %d & %d\n", t1, row1, row2);
      
      val = check(a,b, row1, row2);
      if( -999 == val)
         printf("Case #%d: Bad magician!\n", t1);
      else if ( -1 == val)
         printf("Case #%d: Volunteer cheated!\n", t1);
      else
         printf("Case #%d: %d\n", t1, val) ;
    }

}
