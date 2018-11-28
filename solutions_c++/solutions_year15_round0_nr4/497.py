#include<cstdio>
int main()
{
    freopen("2015_Q_D_s.in","r",stdin);
    freopen("2015_Q_D_s.out","w",stdout);
    int T,x,r,c;
    scanf("%d",&T);
    for(int I=1;I<=T;I++)
    {
        scanf("%d%d%d",&x,&r,&c);
        printf("Case #%d: ",I);
        if((r%x==0&&c>=x-1)||(c%x==0&&r>=x-1))
            printf("GABRIEL\n");
        else
            printf("RICHARD\n");
    }
}
