#include<cstdio>
#include<algorithm>

using namespace std;

int t,x,r,c;
bool ch;

int main()
{
//    freopen("D-small-attempt0.in","r",stdin);
//    freopen("D_out_small.txt","w",stdout);
    scanf("%d",&t);
    for(int z=1;z<=t;z++)
    {
        ch=false;
        scanf("%d%d%d",&x,&r,&c);
        if(x==1)        ch=true;
        else if(x==2)
        {
            if((r*c)%2==0)                ch=true;
        }
        else if(x==3)
        {
            if((r*c)%3==0&&min(r,c)>=2)   ch=true;
        }
        else if(x==4)
        {
            if((r*c)%4==0&&min(r,c)>=3)   ch=true;
        }
        printf("Case #%d: %s\n",z,ch?"GABRIEL":"RICHARD");
    }
    return 0;
}
