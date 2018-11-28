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
#define INPUT freopen("B-large.in","r",stdin);
#define DEBUG(a) cout<<a<<endl;
#define PI acos(-1.0)
#define MAX 300005
#define MOD 1000000007
#define EPS 1e-9
#define BIGGER(a,b) (a>=b ? a : b)
#define SMALLER(a,b) (a<=b ? a : b)
#define getInt(a) scanf("%d",&a);
#define getLong(a) scanf("%lld",&a);
#define pb push_back



int main()
{
    int T,tp=1;
    char inp[MAX];
    int array[MAX];
    int len,i,j,cnt,pre;

    INPUT
    OUTPUT

    getInt(T)

    while(T--)
    {
        scanf("%s",inp);
        len=strlen(inp);

        for(i=0;i<len;i++)
        {
            if(inp[i]=='+')
                array[i]=1;
            else
                array[i]=0;
        }

        /*for(i=0;i<len;i++)
            printf("%d",array[i]);
        printf("\n");*/

        cnt=1;

        pre=array[0];

        for(i=1;i<len;i++)
        {
            if(array[i]!=pre)
            {
                pre=array[i];
                cnt++;
            }
        }

        if(array[len-1]==1)
            cnt--;

        printf("Case #%d: %d\n",tp,cnt);

        tp++;
    }

    return 0;
}


