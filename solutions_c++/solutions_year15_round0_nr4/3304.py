#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("D-small-attempt5.in","r",stdin);
    freopen("d.txt","w",stdout);
    int t,m=0,x,r,c;
    scanf("%d",&t);
    while(t--)
    {
        bool f=0;
        scanf("%d%d%d",&x,&r,&c);
        if(x==1)
            f=1;
        else if(x==2)
        {
            if(((r*c)%2==0)||((r%2==0&&c%2==0)||(r%2!=0&&c%2==0)||(r%2==0&&c%2!=0)))
                f=1;
        }
        else if(x==3)
        {
             if(((r%2!=0&&c%2==0)||(r%2==0&&c%2!=0)||(r%2!=0&&c%2!=0)||((r*c)%3==0))&&(!((r==1&&c==3)||(r==3&&c==1)||r==1||c==1)))
               //if(r*c%3==0&&!((r==1&&c==3)||(r==3&&c==1)))
                f=1;
        }
        else if(x==4)
        {
             if(((r==4&&c==4)||(r==4&&c==3)||(r==3&&c==4)))
                f=1;
        }
        printf("Case #%d: ",++m);
        if(f)printf("GABRIEL\n");
        else printf("RICHARD\n");
    }
}
