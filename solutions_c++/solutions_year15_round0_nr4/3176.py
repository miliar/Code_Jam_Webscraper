#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("D-small-attempt6.in","r",stdin);
    freopen("zxc.out","w",stdout);
    int i,x,r,c,t,d=0;//printf("Case #%d: RICHARD\n",++d);printf("Case #%d: GABRIEL\n",++d);
    cin>>t;
    while(t--){
        cin>>x>>r>>c;
        if(x > r*c)
            printf("Case #%d: RICHARD\n",++d);
        else if(x==1)
            printf("Case #%d: GABRIEL\n",++d);
        else if(x==2)
        {
            if(r*c %2==0)
                printf("Case #%d: GABRIEL\n",++d);
            else
                printf("Case #%d: RICHARD\n",++d);
        }
        else if(x==3)
        {
            if(r==1 || c==1)
                printf("Case #%d: RICHARD\n",++d);
            else if(r*c %3==0)
                printf("Case #%d: GABRIEL\n",++d);
            else
                printf("Case #%d: RICHARD\n",++d);
        }
        else if(x==4)
        {
            if(r*c %4==0){
                if(r==2 || c==2||r==1 ||c==1)
                    printf("Case #%d: RICHARD\n",++d);
                else
                    printf("Case #%d: GABRIEL\n",++d);
            }
            else
                printf("Case #%d: RICHARD\n",++d);
        }
    }
    return 0;
}
