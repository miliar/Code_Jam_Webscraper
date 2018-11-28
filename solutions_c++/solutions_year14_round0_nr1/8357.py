/// Google Code Jam 2014 Quals
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <map>
#include <cstring>
#include <string>
#include <cstdio>
using namespace std;

int main()
{
    freopen("A-small.in","r",stdin);
    freopen("A_answer.txt","w",stdout);
    int t,T,i,n,m;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        int ans,a1,a2;
        map <int,int> pos;
        scanf("%d",&a1);
        for(int i=1;i<=4;i++)
        {
           for(int j=1;j<=4;j++)
           {
                if(i==a1)
                {
                    scanf("%d",&n);
                    pos[n]++;
                }
                else
                    scanf("%d",&n);
           }
        }
        scanf("%d",&a2);
        int found=0,ret;
        for(int i=1;i<=4;i++)
        {
            for(int j=0;j<4;j++)
            if(i==a2)
            {
                scanf("%d",&n);
                if(pos[n]==1)
                {
                    found++;
                    ret=n;
                }
            }
            else
                scanf("%d",&n);
        }
        printf("Case #%d: ",t);
        if(found==1)
            printf("%d\n",ret);
        else if(found==0)
            printf("Volunteer cheated!\n");
        else
            printf("Bad magician!\n");
    }

}
