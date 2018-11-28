#include<stdio.h>

int main()
{
    freopen("D-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,ti,x,r,c;
    scanf ("%d",&t);
    for (ti=0;ti<t;++ti)
    {
        scanf ("%d %d %d",&x,&r,&c);
        printf ("Case #%d: ",ti+1);
        if (x==1 || (x==2 && (r*c)%x==0))printf ("GABRIEL\n");
        else if (x>=7 || !((r>x/2&&c>=x)||(r>=x&&c>x/2)))printf ("RICHARD\n");
        else if ((r*c)%x)printf ("RICHARD\n");
        else printf ("GABRIEL\n");
    }
    return 0;
}
