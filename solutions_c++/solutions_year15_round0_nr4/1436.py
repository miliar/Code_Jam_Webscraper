#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<iostream>
#include<string>
#include<map>
#include<set>
#include<algorithm>
#include<queue>
#include<vector>
#include<time.h>
using namespace std;
int ans[4][4][4]=
{1,1,1,1,
 1,1,1,1,
 1,1,1,1,
 1,1,1,1,

 0,1,0,1,
 1,1,1,1,
 0,1,0,1,
 1,1,1,1,

 0,0,0,0,
 0,0,1,0,
 0,1,1,1,
 0,0,1,0,

 0,0,0,0,
 0,0,0,0,
 0,0,0,1,
 0,0,1,1};
int main()
{
    freopen("D-small-attempt2.in","r",stdin);
    freopen("out.out","w",stdout);
    int t,ca=0;
    scanf("%d",&t);
    while(t--)
    {
        int x,r,c;
        scanf("%d%d%d",&x,&r,&c);
        if(ans[x-1][r-1][c-1])
            printf("Case #%d: GABRIEL\n",++ca);
        else printf("Case #%d: RICHARD\n",++ca);
    }
}
