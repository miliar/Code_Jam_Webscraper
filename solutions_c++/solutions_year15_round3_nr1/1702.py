#include<cstdio>
int main()
{
    freopen("2015_1C_A.in","r",stdin);
    freopen("2015_1C_A.out","w",stdout);
    int T,r,c,w;
    scanf("%d",&T);
    for(int I=1;I<=T;I++)
    {
        scanf("%d%d%d",&r,&c,&w);
        printf("Case #%d: %d\n",I,w>1?r*((c-1)/w)+w :r*c);

    }
}
