#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("abhiins2.txt","r",stdin);
    freopen("abhiouts2.txt","w",stdout);
    int i,j,k,n,t,x,r,c;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d%d%d",&x,&r,&c);
        switch(x)
        {
            case 1:
                printf("Case #%d: GABRIEL\n",i);
                break;
            case 2:
                if((r*c)%2==0)
                    printf("Case #%d: GABRIEL\n",i);
                else
                    printf("Case #%d: RICHARD\n",i);
                break;
            case 3:
                if(((r==3 && c==2)||(c==3 && r==2)||(c==3 && r==3))||(c==3 && r==4)||(c==4 && r==3))
                    printf("Case #%d: GABRIEL\n",i);
                else
                    printf("Case #%d: RICHARD\n",i);
                break;
            case 4:
                if(((r==4 && c==4))||(c==3 && r==4)||(c==4 && r==3))
                    printf("Case #%d: GABRIEL\n",i);
                else
                    printf("Case #%d: RICHARD\n",i);
                break;
            default:
                printf("Case #%d: RICHARD\n",i);
                break;
        }
    }
}
