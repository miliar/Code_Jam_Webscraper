#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

int main()
{
    int t,n,k,mk;
    char z[1010];
    freopen("A-large.in","r",stdin);
    freopen("out.in","w",stdout);
    scanf("%d", &t);
    for(int i=1;i<=t;i++)
    {
        scanf("%d", &n);
        scanf("%s", &z);
        k=0;
        mk=0;

        if(n==0) {printf("Case #%d: %d\n",i,n);}
        else
        {
            k=z[0]-48;
            for(int j=1;j<strlen(z);j++)
            {
                if(k<j)
                {
                    mk=mk+j-k;
                    k=j;
                }

                k=k+(z[j]-48);

            }

            printf("Case #%d: %d\n",i,mk);
        }
    }

return 0;
}
