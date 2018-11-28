#include<bits/stdc++.h>
using namespace std;
int a[15],b[15];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("2A_small.txt","w",stdout);
    int t,r,p,s,i,j,k,fk,n,ct=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d%d%d",&n,&r,&p,&s);
        printf("Case #%d: ",ct++);
        for(i=0;i<p;i++)
            a[i]=1;
        for(i=p;i<r+p;i++)
            a[i]=2;
        for(i=r+p;i<r+p+s;i++)
            a[i]=4;
        fk=0;
        do
        {
            for(i=0;i<1<<n;i++)
                b[i]=a[i];
            for(j=1;j<=n;j++)
            {
                fk=0;
                for(i=0;i<1<<n;i+=1<<j)
                {
                    if(b[i]+b[i+(1<<(j-1))]==5)
                        b[i]=4;
                    else if(b[i]+b[i+(1<<(j-1))]==3)
                        b[i]=1;
                    else if(b[i]+b[i+(1<<(j-1))]==6)
                        b[i]=2;
                    else
                    {
                        fk=1;
                        break;
                    }
                }
                if(fk==1)
                    break;
            }
            if(fk==0)
            {
                for(i=0;i<1<<n;i++)
                {
                    if(a[i]==1)
                        printf("P");
                    else if(a[i]==2)
                        printf("R");
                    else
                        printf("S");
                }
                printf("\n");
                break;
            }
        }
        while(next_permutation(&a[0],&a[1<<n]));
        if(fk==1)
            printf("IMPOSSIBLE\n");
    }

}
