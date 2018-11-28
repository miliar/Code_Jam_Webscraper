#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <vector>
#include <queue>
using namespace std;
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,x,r,c;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf("%d %d %d",&x,&r,&c);
        if(r*c%x!=0)
            printf("Case #%d: RICHARD\n",t);
        else if(x==1||x==2||(x==3&&r!=1&&c!=1)||x==4&&(r==3&&c==4||r==4&&c==3||r==4&&c==4))
            printf("Case #%d: GABRIEL\n",t);
        else
            printf("Case #%d: RICHARD\n",t);
    }
    return 0;
}
