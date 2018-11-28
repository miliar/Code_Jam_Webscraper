#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

int arr[100][100];
int arr2[100][100];
int main()
{
    //freopen("magic.in","r",stdin);
    freopen("magic.out","w",stdout);
    int test,i,j,x,y;
    scanf("%d",&test);
    int cases=0;
    while(test)
    {
        cases++;
        scanf("%d",&x);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&arr[i][j]);
            }
        }
        scanf("%d",&y);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&arr2[i][j]);
            }
        }
        int counter=0;
        int ans;
        for(j=0;j<4;j++)
        {
            int k=arr[x-1][j];
            for(i=0;i<4;i++)
            {
                if(k==arr2[y-1][i])
                {
                    counter++;
                    ans=k;
                    break;
                }
            }
        }
        if(counter==1) printf("Case #%d: %d",cases,ans);
        else if(counter==0) printf("Case #%d: Volunteer cheated!",cases);
        else if(counter>1) printf("Case #%d: Bad magician!",cases);
        test--;
        if(test>0) printf("\n");
    }
    return 0;
}
