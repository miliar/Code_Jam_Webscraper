#include<cstdio>
using namespace std;
int main()
{
    int t;
#ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif
    scanf("%d",&t);
    for(int i=1; i<=t; i++)
    {
        int x,r,c;
        scanf("%d%d%d",&x,&r,&c);

        if(x-1>r || x-1>c || x>=8 || (r*c)%x!=0)
            printf("Case #%d: RICHARD\n",i);
        else
            printf("Case #%d: GABRIEL\n",i);
    }
    return 0;
}
