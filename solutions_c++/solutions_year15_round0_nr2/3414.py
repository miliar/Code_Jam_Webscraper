#include <cmath>
#include <cstdio>
#include <vector>
#include <stack>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
    freopen("B-large.in","r",stdin);
    freopen("infinite_no_of_pancakes.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for (int i = 1; i <= t; i++)
    {
        int noOfPlates, j, k;
        int noOfMins;

        scanf("%d",&noOfPlates);
        int noOfPancakesOnPlateX[noOfPlates+1];
        for (j = 0; j <= noOfPlates - 1; j++)
        {
            scanf("%d",&noOfPancakesOnPlateX[j]);
        }


        int maxNoOfPancakesOnAPlateInInput = 0;
        for (j = 0; j <= noOfPlates - 1; j++)
        {
            if (noOfPancakesOnPlateX[j] >= maxNoOfPancakesOnAPlateInInput)
            {
                maxNoOfPancakesOnAPlateInInput = noOfPancakesOnPlateX[j];
            }
        }

        int minNoMins = maxNoOfPancakesOnAPlateInInput;
        for (j = 1; j <= maxNoOfPancakesOnAPlateInInput; j++)
        {
            noOfMins = 0;
            for (k = 0; k <= noOfPlates - 1; k++)
            {
                noOfMins += (noOfPancakesOnPlateX[k] - 1)/j;
            }
            noOfMins += j;
            if (noOfMins <= minNoMins)
            {
                minNoMins = noOfMins;
            }
        }
        printf("Case #%d: %d\n",i,minNoMins);
    }

    return 0;
}
