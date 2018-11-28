#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,n,p[100],j,h1,h2,h3;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        scanf("%d",&n);
        for(j=0;j<n;j++)
        {
            scanf("%d",p+j);

        }
        printf("Case #%d: ",i);
        if(n==2)
        {
            if(p[0]<p[1])
            {
                while(p[1]>p[0])
                {
                    printf("B ");
                    p[1]--;
                }
            }
            if(p[0]>p[1])
            {
                while(p[1]<p[0])
                {
                    printf("A ");
                    p[0]--;
                }
            }
            while(p[0]!=0|| p[1]!=0)
            {
                printf("AB ");
                p[0]--;p[1]--;
            }
            cout<<endl;
        }
        if(n==3)
        {
            if(p[0]>=p[1])
            {
                if(p[0]>=p[2])
                    h1=0;
                else
                    h1=2;

            }
            else if(p[1]>=p[2])
            {
                h1=1;

            }
            else h1=2;
            if(h1==0)
            {
                if(p[1]>=p[2])
                {
                    h2=1;h3=2;
                }
                else
                    {h2=2;h3=1;}
            }
            if(h1==1)
            {//cout<<h1<<h2<<h3<<endl;
                if(p[0]>=p[2])
                {
                    h2=0;h3=2;
                }
                else
                    {h2=2;h3=0;}
            }
            if(h1==2)
            {//cout<<h1<<h2<<h3<<endl;
                if(p[1]>=p[0])
                {
                    h2=1;h3=0;
                }
                else
                    {h2=0;h3=1;}
            }
            //cout<<h1<<h2<<h3;
            while(p[h1]>p[h2])
            {
                printf("%c ",h1+65);p[h1]--;//cout<<"1"<<endl;
            }
            while(p[h3]>0)
            {
                printf("%c ",h3+65);p[h3]--;//cout<<"2"<<endl;
            }
            while(p[h1]!=0 || p[h2]!=0)
            {
                printf("%c%c ",h1+65,h2+65);p[h1]--;p[h2]--;
            }
            cout<<endl;
        }
    }
    return 0;
}
