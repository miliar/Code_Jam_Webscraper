#include<bits/stdc++.h>
using namespace std;

int m,n,mark[10],t,X,i;
long long int N;

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);

    while(t--)
    {
        memset(mark,0,sizeof(mark));
        X++;
        scanf("%d",&n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",X);
            continue;
        }

        int j=1;
        while(1)
        {
            N=(long long)n*j;
            while(N)
            {
                m=N%10;
                N=N/10;
                mark[m]=1;
            }
            for(i=0; i<10; i++)
                if(!mark[i])
                    break;
            if(i==10)
                break;
            j++;
        }
        printf("Case #%d: %lld\n",X,(long long)n*j);
    }
    return 0;
}
