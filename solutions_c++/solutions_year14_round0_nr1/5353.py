#include <algorithm>
#include <cmath>
#include <cstring>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <cstdlib>
#include <set>
#define DEBUG printf("TEST\n")

using namespace std;

int itc, TC;
int N, M[5][5], r, i, j, mark[20];

int hit, miss;

int main()
{
     
     scanf("%d", &TC);
     for(itc = 1; itc <= TC; ++itc)
     {
          
          hit = miss = 0;
          for(i = 1; i <= 16; ++i) mark[i] = 0;
          
          scanf("%d", &r);
          for(i = 1; i <= 4; ++i)
          {
               for(j = 1; j <= 4; ++j)
               {
                    scanf("%d", &M[i][j]);
                    
                    if(i == r)
                    {
                         mark[M[i][j]] = 1;
                    }
               }
          }
          scanf("%d", &r);
          for(i = 1; i <= 4; ++i)
          {
               for(j = 1; j <= 4; ++j)
               {
                    scanf("%d", &M[i][j]);
                    
                    if(i == r)
                    {
                         if(mark[M[i][j]])
                         {
                              ++hit;
                              N = M[i][j];
                         }
                         else
                         {
                              ++miss;
                         }
                    }
               }
          }
          
          printf("Case #%d: ", itc);
          if(hit > 1)
          {
               printf("Bad magician!\n");
          }
          else if(hit == 1)
          {
               printf("%d\n", N);
          }
          else{
               printf("Volunteer cheated!\n");
          }
          
     }
     
     return 0;
}
