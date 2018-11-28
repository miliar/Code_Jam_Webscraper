#include<cstdio>
#include<cmath>
#include<stdlib.h>
#include<map>
#include<set>
#include<time.h>
#include<vector>
#include<queue>
#include<string>
#include<string.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define eps 1e-8
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
int x,r,c;
int main()
{
    int cas;
    freopen("D-small-attempt2.in","r",stdin);
    freopen("D-small-attempt2.out","w",stdout);
    scanf("%d",&cas);
    for(int i=1;i<=cas;i++)
    {
        scanf("%d%d%d",&x,&r,&c);
        //printf("%d %d %d\n",x,r,c);
        int flag=1;
        if(x>=7)
        {
            printf("Case #%d: RICHARD\n",i);
        }
        else if(r*c%x!=0)
        {
            printf("Case #%d: RICHARD\n",i);
        }
        else
        {
            if(x==1)
                printf("Case #%d: GABRIEL\n",i);
            else if(x==2)
                printf("Case #%d: GABRIEL\n",i);
            else if(x==3)
            {
                if(min(r,c)==1)
                    printf("Case #%d: RICHARD\n",i);
                else
                    printf("Case #%d: GABRIEL\n",i);
            }
            else if(x==4)
            {
                if(min(r,c)==1||min(r,c)==2)
                    printf("Case #%d: RICHARD\n",i);
                else
                    printf("Case #%d: GABRIEL\n",i);
            }
        }
    }
    return 0;
}
