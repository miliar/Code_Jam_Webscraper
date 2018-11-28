#include <iostream>
#include <cstdio>
using namespace std;

typedef long long ll;

int main()
{
    freopen("cin.txt","r",stdin);
    freopen("cout.txt","w",stdout);
    int test_case, T;
    scanf("%d" , &T);
    for(test_case=1;test_case<=T;test_case++)
    {
        printf("Case #%d:\n" , test_case);
        int i,j;
        int N, J;
        scanf("%d %d" , &N, &J);
        ll X[9];
        for(i=0;i<9;i++)
        {
            X[i]=(ll)(i+2);
            for(j=0;j<N/2-1;j++)
            {
                X[i]=X[i]*(ll)(i+2);
            }
            X[i]=X[i]+1LL;
        }
        char A[N+1];
        A[N]=NULL;
        for(i=0;i<J;i++)
        {
            int tmp=i;
            A[0]=A[N/2-1]=A[N/2]=A[N-1]='1';
            for(j=1;j<N/2-1;j++)
            {
                if(tmp&1)
                {
                    A[j]=A[j+N/2]='1';
                }
                else
                {
                    A[j]=A[j+N/2]='0';
                }
                tmp>>=1;
            }
            printf("%s " , A);
            for(j=0;j<9;j++)
            {
                printf("%lld " , X[j]);
            }
            printf("\n");
        }




    }

    return 0;
}
