#include<stdio.h>

void play(int t)
{
    double c,f,x,ans,tod=0,cnt=2;
    scanf ("%lf %lf %lf",&c,&f,&x);
    ans = x/cnt;
    while(1)
    {
        tod += c/cnt;
        cnt += f;
        if (tod >= ans)break;
        if (tod + x/cnt < ans)ans = tod+x/cnt;
    }
    printf ("Case #%d: %.7lf\n",t,ans);
    //return 0;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("txt.txt","w",stdout);
    int t,i;
    scanf ("%d",&t);
    for (i=0;i<t;++i)
    {
        play(i+1);
    }
    return 0;
}
