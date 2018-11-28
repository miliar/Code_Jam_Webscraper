#include<iostream>
#include<stdio.h>
using namespace std;
#include<string.h>
int main()
{
   #ifndef ONLINE_JUDGE
        freopen("input3.cpp","r",stdin);
        freopen("output6.cpp","w",stdout);
    #endif // ONLINE_JUDGE
    int t;
    cin>>t;
    int k=1;
    while(t--)
    {
        int x,r,c,i,j,p,te;
        cin>>x>>r>>c;
        if(r>c)
        {
            te=r;
            r=c;
            c=te;
        }
        if(((r*c)%x!=0)||(r*c<x))
        {
            p=0;
        }
        else
        {
            if(x==1)
                p=1;
            else if(x==2)
            {
                p=1;
            }
            else if(x==3)
            {
                if((r==1)&&(c==3))
                    p=0;
                else
                    p=1;
            }
            else if(x==4)
            {
                if((r==1)||(r==2))
                    p=0;
                else
                    p=1;
            }
            else if(x==5)
            {
                if((r==1)||(r==2))
                    p=0;
                else
                    p=1;
            }
            else if(x==6)
            {
                if((r==1)||(r==2)||((r==3)&&(c==4)))
                    p=0;
                else
                    p=1;
            }
            else if(x>=7)
                p=0;
        }
        if(p==0)
            printf("Case #%d: RICHARD\n",k);
        else
            printf("Case #%d: GABRIEL\n",k);
            k++;
    }
    return 0;
}
