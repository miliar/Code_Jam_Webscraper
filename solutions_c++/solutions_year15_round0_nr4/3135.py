#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,i,a[1005],j,k,l,p,q,m,n;
    char z,s[1005];
    freopen("q_2_2.txt","r",stdin);
    freopen("a_2.txt","w",stdout);
    scanf("%d",&t);
    for(l=1;l<=t;l++)
    {
        scanf("%d %d %d",&n,&p,&q);
        k=(p*q);
        i=min(p,q);
        j=max(p,q);
        m=0;
        if(n==1)
            m=1;
        else if(n==2)
        {
            if(p%2==0 || q%2==0)
                m=1;
        }
        else if(n==3)
        {
            if(k%3==0)
               if(i>1)
                    m=1;
        }
        else if(n==4)
        {
            if(k%4==0)
            {
                if(i>2)
                    m=1;
            }
        }
        else if(n==5)
        {
            if(k%5==0)
            {
                if(i>2)
                    m=1;
            }
        }
        else if(n==6)
        {
            if(k%6==0)
            {
                if(i>2)
                    m=1;
            }
        }
        if(m==1)
        printf("Case #%d: GABRIEL\n",l);
        else
            printf("Case #%d: RICHARD\n",l);
    }
    return 0;
}
