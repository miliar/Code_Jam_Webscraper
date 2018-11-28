#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <stack>
#include <queue>
#include <cmath>

#define debug if(1)

using namespace std;

int main()
{
    int t,r1,cnt,r2,arr1[4][4],arr2[4][4],ans,caseno=1;;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&r1);
        for (int i = 0; i < 4; i++) 
        {
            for (int j = 0; j < 4; j++) 
            {
                scanf("%d",&arr1[i][j]);
            }
        }
        scanf("%d",&r2);
        r1--;r2--;
        for (int i = 0; i < 4; i++) 
        {
            for (int j = 0; j < 4; j++) 
            {
                scanf("%d",&arr2[i][j]);
            }
        }
        cnt=0;
        for (int i = 0; i < 4; i++) 
        {
            for (int j = 0; j < 4; j++) 
            {
                if(arr1[r1][i]==arr2[r2][j])
                {cnt++;ans=arr1[r1][i];}
            }
        }
        printf("Case #%d: ",caseno++);
        if(cnt>1)
        {puts("Bad magician!");}
        else if(cnt==0)
        {puts("Volunteer cheated!");}
        else
        {printf("%d\n",ans);}
    }
    return 0;
}
