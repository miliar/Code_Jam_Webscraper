#include<cstdio>

bool judge(int x,int r,int c)
{
    if(x==1) return true;
    if(x==2) {
        return r*c%2==0;
    }
    if(x==3) return r>=2 && c>=2 && r*c%3==0;
    if(x==4) {
        if(r==4 && c==4) return true;
        if(r==4 && c==3) return true;
        if(r==3 && c==4) return true;
    }
    return false;
}

int main()
{
    freopen("D-small-attempt1.in","r",stdin);
    freopen("d.out","w",stdout);
    int t,x,r,c;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++) {
        scanf("%d%d%d",&x,&r,&c);
        printf("Case #%d: ",cas);
        if(judge(x,r,c)) printf("GABRIEL\n");
        else printf("RICHARD\n");
    }
    return 0;
}
