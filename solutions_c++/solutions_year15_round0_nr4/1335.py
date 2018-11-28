#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <string>
#include <vector>
#include <queue>
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define MAXN 100010
#define eps 1e-8
#define pi acos(-1.0)
using namespace std;
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T,x,r,c;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf("%d %d %d",&x,&r,&c);
        if(r*c%x!=0)
            printf("Case #%d: RICHARD\n",t);
        else if(x==1||x==2)
            printf("Case #%d: GABRIEL\n",t);
        else if(x==3)
        {
            if(r==1||c==1)
                printf("Case #%d: RICHARD\n",t);
            else
                printf("Case #%d: GABRIEL\n",t);
        }
        else if(x==4)
        {
            if((r==3&&c==4)||(r==4&&c==3)||(r==4&&c==4))
                printf("Case #%d: GABRIEL\n",t);
            else
                printf("Case #%d: RICHARD\n",t);
        }
    }
    return 0;
}
