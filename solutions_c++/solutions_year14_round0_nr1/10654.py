#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <map>
#include <string>
#include <sstream>
#include <set>
#include <queue>
#include <list>
#include <algorithm>
#include <iostream>
typedef long long ll;
using namespace std;
int a,b,arr[5][5],brr[5][5];
int main()
{
    freopen("A-small.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,count,ans,i,j,C=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&a);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&arr[i][j]);
            }
        }
        scanf("%d",&b);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&brr[i][j]);
            }
        }
        count=0;
        ans=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(arr[a-1][i]==brr[b-1][j])
                {
                    count++;
                    ans=arr[a-1][i];
                }
            }
        }
        if(count==0)
            printf("Case #%d: Volunteer cheated!\n",C++);
        else if(count==1)
            printf("Case #%d: %d\n",C++,ans);
        else
            printf("Case #%d: Bad magician!\n",C++);
    }

    return 0;
}
