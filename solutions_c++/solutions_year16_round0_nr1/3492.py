#include<iostream>
#include<cstdio>

using namespace std;

typedef long long int ll;

int main()
{
    freopen("input.in", "r", stdin);
    freopen ("output.txt","w",stdout);
    int Test,k=0;
    scanf("%d",&Test);
    while(Test--)
    {
        ll N;
        int i;
        k++;
        scanf("%lld",&N);
        bool A[11];
        for( i=0;i<11;i++)
            A[i]=false;
        printf("Case #%d: ",k);
        if(N==0)
        {
            printf("INSOMNIA\n");
        }
        else
        {
            ll cnt=1,M;
            ll p=0;
            while(true)
            {
                p=0;
                M=N*cnt;
                while(M)
                {
                    //if(A[M%10])
                    A[M%10]=true;
                    M=M/10;
                }
                for(i=0;i<10;i++)
                    if(A[i])
                        p++;
                if(p==10)
                    break;
                cnt++;
            }
            printf("%lld\n",cnt*N);
        }
    }
    fclose(stdout);
    return 0;
}
