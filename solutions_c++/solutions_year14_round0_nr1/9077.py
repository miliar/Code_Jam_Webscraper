#include<algorithm>
#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<limits.h>
#include<sstream>
#include<stdio.h>
#include<ctype.h>
#include<math.h>
#include<vector>
#include<string>
#include<queue>
#include<stack>
#include<map>
#include<set>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,tt,first,second,arr1[5][5],arr2[5][5],number,flag,i,c;
    scanf("%d",&t);
    for(tt=1;tt<=t;tt++)
    {
        scanf("%d",&first);
        for(i=0;i<4;i++)
            for(c=0;c<4;c++)
                scanf("%d",&arr1[i][c]);

        scanf("%d",&second);
        for(i=0;i<4;i++)
            for(c=0;c<4;c++)
                scanf("%d",&arr2[i][c]);
        flag=0;
        for(i=0;i<4;i++)
        {
            for(c=0;c<4;c++)
            {
                if(arr1[first-1][i]==arr2[second-1][c])
                {
                    number=arr1[first-1][i];
                    flag++;
                }
            }
        }
        printf("Case #%d: ",tt);
        if(flag==0)
            printf("Volunteer cheated!\n");
        else if (flag==1)
            printf("%d\n",number);
        else
            printf("Bad magician!\n");
    }
	return 0;
}
