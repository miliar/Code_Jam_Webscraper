#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<cstring>
#include<queue>
#include<set>
#include<map>
#include<vector>
#include<cmath>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t=1; t<=T; t++)
    {
        map<int,bool> mp;
        int i,j,x,y,z,p=0;

        scanf("%d",&x);
        for(i=1; i<=4; i++)
        for(j=1; j<=4; j++)
        {
            scanf("%d",&y);
            if(i==x) mp[y]=true;
        }

        scanf("%d",&x);
        for(i=1; i<=4; i++)
        for(j=1; j<=4; j++)
        {
            scanf("%d",&y);
            if(i==x && mp[y]==true) { z=y; p++; }
        }
        if(p==0) printf("Case #%d: Volunteer cheated!\n",t);
        if(p==1) printf("Case #%d: %d\n",t,z);
        if(p> 1) printf("Case #%d: Bad magician!\n",t);
    }
    return 0;
}
