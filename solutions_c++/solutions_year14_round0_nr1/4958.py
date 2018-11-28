#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
#include <cstdio>
#include <string>
#include <queue>
#include <vector>
#include <cmath>
#include <set>
#include <map>
using namespace std;
int a[5][5],b[5][5];
int main()
{
    freopen("out.txt","w",stdout);
    int T,cas=1;
    scanf("%d",&T);
    while(T--)
    {
        int r1,r2;
        scanf("%d",&r1);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++) scanf("%d",&a[i][j]);
        scanf("%d",&r2);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++) scanf("%d",&b[i][j]);
        int cnt=0,ans;
        r1--;r2--;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(a[r1][i]==b[r2][j])
                {
                    cnt++;
                    ans=a[r1][i];
                }
            }
        }
        if(cnt==0) printf("Case #%d: Volunteer cheated!\n",cas++);
        else if(cnt==1) printf("Case #%d: %d\n",cas++,ans);
             else printf("Case #%d: Bad magician!\n",cas++);
    }
    return 0;
}


