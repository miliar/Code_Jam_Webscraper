#include <stdio.h>
#include <string.h>
#include <vector>
#include <queue>
#include <deque>
#include <algorithm>
#include<iostream>
using namespace std;
bool arr[20];
int main()
{
freopen("S.in","r",stdin);
freopen("out.txt","w",stdout);

    int t,a,b,c,g;
    g=1;
    scanf("%d",&t);
    while(t--)
    {
        fill(&arr[0],&arr[20],false);
        vector<int>ans;
        scanf("%d",&a);
        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            {
                scanf("%d",&b);
                if(i==a-1)
                    arr[b]=1;
            }
        }
        scanf("%d",&c);
        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            {
                scanf("%d",&b);
                if(i==c-1)
                {
                    if(arr[b]==true)
                        ans.push_back(b);
                }
            }
        }
        if(ans.size()==0)
            printf("Case #%d: Volunteer cheated!\n",g++);
        else if(ans.size()==1)
            printf("Case #%d: %d\n",g++,ans[0]);
        else
            printf("Case #%d: Bad magician!\n",g++);

    }


    return 0;

}
