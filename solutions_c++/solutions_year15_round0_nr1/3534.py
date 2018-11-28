#include <cmath>
#include <cstdio>
#include <vector>
#include <stack>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("standing_ovation.txt", "w", stdout);
    int t, i;
    scanf("%d",&t);
    for (i = 1; i <= t; i++)
    {
        //int weDidIt = 0;
        int maxShyness, j, k;
        scanf("%d",&maxShyness);
        char noOfPeopleOfShynessX[maxShyness + 2];
        int noOfPeopleOfShynessY[maxShyness + 2];
        scanf("%s",&noOfPeopleOfShynessX);
        for (j = 0; j <= maxShyness; j++)
        {
            noOfPeopleOfShynessY[j] = noOfPeopleOfShynessX[j] - '0';
        }
        int noOfPeopleStanding = 0;
        //int noOfPeopleInAudience = 0;
        int noOfAudienceToBeAdded = 0;
//        for (j = 0; j <= maxShyness; j++)
//        {
//            noOfPeopleInAudience += noOfPeopleOfShynessY[j];
//        }

        j = 0;
        while (j <= maxShyness)
        {
            if (noOfPeopleStanding >= j)
            {
                noOfPeopleStanding += noOfPeopleOfShynessY[j];
                for (k = j+1; k <= noOfPeopleStanding; k++)
                {
                    noOfPeopleStanding += noOfPeopleOfShynessY[k];
                }
                j = k;
            }
            else
            {
                noOfAudienceToBeAdded += (j - noOfPeopleStanding);
                noOfPeopleStanding = j;
                //noOfPeopleInAudience += (j - noOfPeopleStanding);
            }
//            if (noOfPeopleStanding == noOfPeopleInAudience)
//            {
//                weDidIt = 1;
//                break;
//            }
        }
        printf("Case #%d: %d\n",i, noOfAudienceToBeAdded);
//        if (weDidIt)
//        {
//
//        }
    }
    return 0;
}
