#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,n,k,t,m,p;
    scanf("%d",&t);
    for(j=1;j<=t;j++)
    {
        scanf("%d",&n);
        if(n==0) printf("Case #%d: INSOMNIA\n",j);
        else{
        int a[10];
        m=0;
        for(i=0;i<10;i++)
        {
            a[i]=0;
        }
        i=1;
        while(m!=10)
        {
            k=i*n;
            while(k>0)
            {
                p=k%10;
                if(a[p]==0) {
                    a[p]=1;
                    m++;
                }
                k=k/10;
            }
            i++;
        }
        printf("Case #%d: %d\n",j,(i-1)*n);
        }

    }
    return 0;
}
