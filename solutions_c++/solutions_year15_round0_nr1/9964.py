#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <vector>

using namespace std;


int solveCurrCase()
{
    int Smax;
    scanf("%d", &Smax);
    int SmaxVector;
    scanf("%d", &SmaxVector);

    vector<int> SmaxSeq(Smax+1, 0);
    for(int i = Smax; i>=0 ; i--)
    {
        if (SmaxVector <= 0 )
            break;
        SmaxSeq[i] = SmaxVector % 10;
        SmaxVector = SmaxVector /10 ;

    }
    //cout<< "\n"<<Smax<< "--> ";
    for(int i = 0 ; i<= Smax ; i++)
     {
         //cout<< SmaxSeq[i]<< "\t";
     }
    //cout<< "\n";

    int added_ppl = 0;
    int noPplUp = 0;
    for(int i = 0 ; i<= Smax ; i++)
     {
         //deadlock-->add ppl
         while ( noPplUp < (i ) )
         {
             added_ppl++;
             noPplUp++;
         }
         noPplUp += SmaxSeq[i];

     }
    //cout<< "\t"<<added_ppl<<"\n";

    return added_ppl;
}
int main()
{
      freopen("small2.in", "r", stdin);
      freopen("out1", "w", stdout);

      int testCases;
      scanf("%d", &testCases);
      for (int currCase = 1 ; currCase <= testCases ; currCase++ )
      {
          int res = solveCurrCase();
          printf("\nCase #%d: %d",currCase, res);
      }

       return 0;
}
