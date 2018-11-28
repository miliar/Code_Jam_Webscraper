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
    int arng1[4][4], arng2[4][4];
    int chc1, chc2;
    int i, j, cm, cmcnt;
    freopen("AS.in", "r", stdin);
    freopen("AS.out", "w", stdout);
    cin>>T;
    int csno = 1;
    while(T--)
    {
        cin>>chc1;
        for (i = 0; i < 4; i++)
        {
            for (j = 0; j < 4; j++)
            {
                cin>>arng1[i][j];
            }
        }
        cin>>chc2;
        for (i = 0; i < 4; i++)
        {
            for (j = 0; j < 4; j++)
            {
                cin>>arng2[i][j];
            }
        }
        //find com and comcount betn arng1/2
        cmcnt = 0;
        for (i = 0; i < 4; i++)
        {
            if (cmcnt > 1) break;
            for (j = 0; j < 4; j++)
            {
                if (arng1[chc1 - 1][i] == arng2[chc2 - 1][j])
                {
                    cm = arng1[chc1 - 1][i];
                    cmcnt += 1;


                }
            }
        }
        if (cmcnt == 0)
        {
            cout<<"Case #"<<csno<<": Volunteer cheated!"<<endl;
        }
        else
            if (cmcnt == 1)
        {
            cout<<"Case #"<<csno<<": "<<cm<<endl;
        }
        else
        {
            cout<<"Case #"<<csno<<": Bad magician!"<<endl;
        }
        csno += 1;
    }
    return 0;
}
