#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int test;
    scanf("%d",&test);
    for(int t=1;t<=test;t++)
    {
        int x,r,c;
        scanf("%d%d%d",&x,&r,&c);
        printf("Case #%d: ",t);
        if(x==1)
        {
            printf("GABRIEL\n");
            continue;
        }
        if(x==2)
        {
            if((r*c)%2==0)
                printf("GABRIEL\n");
            else
                printf("RICHARD\n");
            continue;
        }
        if(r>c)
            swap(r,c);
        if((x==3&&r==2&&c==3)||(x==3&&r==3&&c==3)||(x==3&&r==3&&c==4)||(x==4&&r==3&&c==4)||(x==4&&r==4&&c==4))
            printf("GABRIEL\n");
        else
            printf("RICHARD\n");
    }
}
