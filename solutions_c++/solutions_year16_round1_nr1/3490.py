/* بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ */
/* رَّبِّ زِدْنِى عِلْمًا */



#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <iostream>
#include <string>

using namespace std;

#define OUTPUT freopen("myfile.txt","w",stdout);
#define INPUT freopen("A-large.in","r",stdin);
#define DEBUG(a) cout<<a<<endl;
#define PI acos(-1.0)
#define MAX 220005
#define MOD 1000000007
#define EPS 1e-9
#define BIGGER(a,b) (a>=b ? a : b)
#define SMALLER(a,b) (a<=b ? a : b)
#define getInt(a) scanf("%d",&a);
#define getLong(a) scanf("%lld",&a);
#define pb push_back

int main()
{
    char Array[MAX];
    int T;
    int tp=1;
    int i;
    int len;
    int top,bottom;
    char given[MAX];

    //INPUT
    //OUTPUT

    getInt(T)

    while(T--)
    {
        scanf("%s",given);
        len=strlen(given);

        top=2000;
        bottom=2000;

        Array[top]=given[0];

        for(i=1;i<len;i++)
        {
            if(given[i]>=Array[top])
            {
                top--;
                Array[top]=given[i];
            }

            else
            {
                bottom++;
                Array[bottom]=given[i];
            }
        }

        printf("Case #%d: ",tp);
        tp++;

        for(i=top;i<=bottom;i++)
            printf("%c",Array[i]);
        printf("\n");

    }

    return 0;
}
