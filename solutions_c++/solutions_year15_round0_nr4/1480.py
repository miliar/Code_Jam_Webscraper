#include<bits/stdc++.h>


using namespace std;
int main()
{
    freopen("D-small-attempt1.in","r",stdin);
    freopen("4.2.out4small.txt","w",stdout);
    int t,tc=1,x,r,c;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d %d %d",&x,&r,&c);
        if(x==1)printf("Case #%d: GABRIEL\n",tc++);
        else if(x==2){
            if(r==1 && c==1)printf("Case #%d: RICHARD\n",tc++);
            else if((r*c)%2==0)printf("Case #%d: GABRIEL\n",tc++);
            else printf("Case #%d: RICHARD\n",tc++);
        }
        else if(x==3){
            if(r==1 || c==1)printf("Case #%d: RICHARD\n",tc++);
            else if((r*c)%3==0)printf("Case #%d: GABRIEL\n",tc++);
            else printf("Case #%d: RICHARD\n",tc++);
        }
        else{
            if(r==1 || c==1)printf("Case #%d: RICHARD\n",tc++);
            else if(r==2 || c==2)printf("Case #%d: RICHARD\n",tc++);
            else if(r==4 || c==4)printf("Case #%d: GABRIEL\n",tc++);
            else printf("Case #%d: RICHARD\n",tc++);

        }

    }

    return 0;
}
