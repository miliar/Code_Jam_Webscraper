/***    google_code_jam_pro4    ***/

#include <stdio.h>

int T;
int x,r,c;

void swap(int &a,int &b){int temp=a;a=b;b=temp;}

bool g_win()
{
    if(x==1){return 1;}
    else if(x==2){return (((r*c)&1)?(0):(1));}
    else if(x==3)
    {
        if(r>c) swap(r,c);
        if((r==2&&c==3)||(r==3&&c==3)||(r==3&&c==4)) return 1;
        else return 0;
    }
    else
    {
        if(r>c) swap(r,c);
        if(c<4) return 0;
        else if(r<3) return 0;
        else return 1;
    }
}

void work()
{
    scanf("%d",&T);getchar();
    for(int i=1;i<=T;++i)
    {
        scanf("%d %d %d",&x,&r,&c);getchar();
        printf("Case #%d: %s\n",i,((g_win())?("GABRIEL"):("RICHARD")));
    }
}



int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);

    work();

    fclose(stdin);
    fclose(stdout);

    return 0;
}
