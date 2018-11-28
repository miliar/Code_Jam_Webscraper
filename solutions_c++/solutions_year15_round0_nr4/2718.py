//GCJ 2015Q A
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int sm;
char s[1002];
int main()
{
    freopen("D-small-attempt2.in","r",stdin);
    freopen("D-small-attempt2.out","w",stdout);
    int Case,x,r,c;
    scanf("%d",&Case);
    for(int t=1;t<=Case;++t)
    {
        scanf("%d%d%d",&x,&r,&c);
        if(x==1)
        {
            printf("Case #%d: GABRIEL\n",t);
        }
        else if(x==2)
        {
            if( (r*c)%2==0)
                printf("Case #%d: GABRIEL\n",t);
            else
                printf("Case #%d: RICHARD\n",t);
        }
        else if(x==3)
        {
            if( r*c==6 || r*c==12 || r*c==9 )
                printf("Case #%d: GABRIEL\n",t);
            else
                printf("Case #%d: RICHARD\n",t);
        }
        else if(x==4)
        {
            if( r*c==12 || r*c==16)
                printf("Case #%d: GABRIEL\n",t);
            else
                printf("Case #%d: RICHARD\n",t);
        }
    }
    return 0;
}
