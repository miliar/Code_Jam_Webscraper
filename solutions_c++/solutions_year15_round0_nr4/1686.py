#include <cstdio>
void swap(int &a,int &b)
{
    int temp=a;
    a=b;
    b=temp;
}
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    bool flg;
    int T,x,r,c,area;
    scanf("%d",&T);
    for(int k=0;k<T;k++)
    {
        flg=0;
        scanf("%d%d%d",&x,&r,&c);
        if(r>c) swap(r,c);
        area=r*c;
        if(area>=x && area%x==0)
        {
            if(x==1) flg=1;
            else if(x==2){
                if(area%2==0) flg=1;
            }
            else if(x==3){
                if(area%3==0&&area!=3) flg=1;
            }
            else if(x==4){
                if(area==12||area==16) flg=1;
            }
        }
        printf("Case #%d: ",k+1);
        printf(flg ? "GABRIEL\n" : "RICHARD\n");

    }

    return 0;
}
