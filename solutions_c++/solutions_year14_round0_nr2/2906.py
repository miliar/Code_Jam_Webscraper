/*
UVa 10684 : The Jackpot

Brief Problem Description: There will be a series of bets, calculate the
consecutive gains and losses and determine whether its a winning or
lossing streak. If its a winning streak, then print the maximum
winning streak.

Solution methodology: Input size is quite large (10000), so ANY
O(N^2) algorithm will get a plain and straight TLE.
I needed a O(N) algorithm for this, and after thinking some time,
I observed the last loop was redundant and as for gains, that path can be dropped.

Algorithm (Maximum Consecutive sub-sequence sum):

public static int MCSS(int [] a) {

     int max = 0, sum = 0, start = 0, end = 0, i=0;

     // Cycle through all possible end indexes.
     for (j = 0; j < a.length; j++) {

          sum += a[j]; // No need to re-add all values.
          if (sum > max) {
              max = sum;
              start = i; // Although method doesn't return these
              end = j;  // they can be computed.
          }
          else if (sum < 0) {
               i = j+1; // Only possible MCSSs start with an index >j.
               sum = 0; // Reset running sum.
          }
     }
     return max;
}

It took me 40 minutes to solve this :-)
*/

#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
    int T;
    //int arng1[4][4], arng2[4][4];
    //int chc1, chc2;
    //int i, j, cm, cmcnt;
    double C, F, X, tots, pw;
    freopen("BL.in", "r", stdin);
    freopen("BL.out", "w", stdout);
    cin>>T;
    int csno = 1;
    while(T--)
    {
        cin>>C>>F>>X;
        //initialize pw and tots
        pw = 2.0;
        tots = 0.0;
        while(1)
        {
            if (((C / pw) + (X / (pw + F))) < (X / pw))
            {
                //increase tots
                tots += (C / pw);
                pw += F;
            }
            else
            {
                tots += (X / pw);
                break;
            }
        }
        cout<<"Case #"<<csno<<": ";
        printf("%.7f\n", tots);
        csno += 1;
    }
    return 0;
}
