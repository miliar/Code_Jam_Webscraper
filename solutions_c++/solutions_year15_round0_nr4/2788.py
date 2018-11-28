#include<iostream>
#include<cstdio>
#include<cstring>
#define LL long long
using namespace std;

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("input.cpp","r",stdin);
        freopen("output.cpp","w",stdout);
    #endif // ONLINE_JUDGE
    int t,test,i,x,r,c,res,temp;
    scanf("%d",&test);
    t=1;
    while(t<=test)
    {
        scanf("%d%d%d",&x,&r,&c);
        if(r>c)
        {
            temp=r;
            r=c;
            c=temp;
        }
        if(((r*c)%x!=0)||(r*c<x))
        {
            res=0;
        }
        else
        {
            if(x==1)
                res=1;
            else if(x==2)
            {
                res=1;
            }
            else if(x==3)
            {
                if((r==1)&&(c==3))
                    res=0;
                else
                    res=1;
            }
            else if(x==4)
            {
                if((r==1)||(r==2))
                    res=0;
                else
                    res=1;
            }
        }
        if(res==0)
            printf("Case #%d: RICHARD\n",t);
        else
            printf("Case #%d: GABRIEL\n",t);
        t++;
    }
    return 0;
}
