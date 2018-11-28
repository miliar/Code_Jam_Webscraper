#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("inp.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,c=1,x,r,c1,i;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d %d %d",&x,&r,&c1);
        if(x==1)
            printf("Case #%d: GABRIEL\n",c);
        else if(x==2)
        {
            if(r%2==0||c1%2==0)
                printf("Case #%d: GABRIEL\n",c);
            else
                printf("Case #%d: RICHARD\n",c);
        }
        else if(x==3)
        {
            if(r>c1)
            {
                i=r;
                r=c1;
                c1=i;
            }
            if((r==3&&c1==4)||(r==2&&c1==3)||(r==3&&c1==3))
                printf("Case #%d: GABRIEL\n",c);
            else
                printf("Case #%d: RICHARD\n",c);
        }
        else
        {
            if(r>c1)
            {
                i=r;
                r=c1;
                c1=i;
            }
            if(!((c1==4&&r==4)||(r==3&&c1==4)))
                printf("Case #%d: RICHARD\n",c);
            else
                printf("Case #%d: GABRIEL\n",c);
        }
        c++;
    }
    return 0;
}
