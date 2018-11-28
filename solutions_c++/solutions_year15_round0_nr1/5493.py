#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

/*
* Google codeJam 2015 Qualifiers
* Standing Ovation (Question A)
****************************************
* Minimum number of friends to be added for ensuring a complete standing ovation based on the input shyness matrix.
*/


int parseShynessMatrix (int maxShy, char * shyness)
{
    char shynessArray[1000];
    strcpy (shynessArray,shyness);
    int standing=0;
    int needed=0;
    for (int i=0; i <= maxShy; i++)
    {
        if (standing < i ) 
        {
            needed=needed >(i-standing)? needed:(i-standing);
        }
        standing+=((((int)shynessArray[i])-48));
    }
    return needed;
}
                   

int main ()
{
    char shynessString[1000];
    int cases,missing,maxShy;
    scanf("%d",&cases);
    for (int tCase=1; tCase <= cases; tCase++)
    {
        scanf("%d %s",&maxShy,&shynessString);
        missing=parseShynessMatrix(maxShy,shynessString);
        printf("Case #%d: %d\n",tCase,missing);

    }
    return 0;
}
