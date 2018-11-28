#include <iostream>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <limits.h>
#include <set>
#include <stack>
#include <vector>
#include <map>
using namespace std;

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int t;
    scanf("%d",&t);
    int z=1;
    while(t--)
    {
        int a1,a2;
        scanf("%d",&a1);
        int ar1[5][5],ar2[5][5];
        for(int i =1;i<5;i++)
            for(int j=1;j<5;j++)
                scanf("%d",&ar1[i][j]);
        scanf("%d",&a2);
        for(int i =1;i<5;i++)
            for(int j=1;j<5;j++)
                scanf("%d",&ar2[i][j]);
        int ans=0;
        int res;
        for(int i =1;i<5;i++)
        {
            for(int j=1;j<5;j++)
            {
                if(ar1[a1][i]==ar2[a2][j])
                {
                    res=ar1[a1][i];
                    ans++;
                }
            }
        }
        printf("Case #%d: ",z++);
        if(ans==0)
            printf("Volunteer cheated!");
        else if (ans>=2)
            printf("Bad magician!");
        else
            printf("%d",res);
        printf("\n");
    }
    return 0;
}
