#include <iostream>
#include <cstdio>
#include <vector>
#include <utility>
 
using namespace std;
 
int main()
{
    freopen("ain.txt","r",stdin);
    freopen("aout.txt","w",stdout);
    int test_case, T;
    scanf("%d" , &T);
    for(test_case=1;test_case<=T;test_case++)
    {
        printf("Case #%d: " , test_case);
        int i, j;
        int N;
        scanf("%d" , &N);
        int P[N];
        int sum=0;
        for(i=0;i<N;i++)
        {
            scanf("%d" ,&P[i]);
            sum+=P[i];
        }
        if(sum%2==1)
        {
            int tmp=0, ind=-1;
            for(i=0;i<N;i++)
            {
                if(P[i]>=tmp)
                {
                    tmp=P[i];
                    ind=i;
                }
            }
            P[ind]--;
            sum--;
            printf("%c " , 'A'+ind);
        }
 
        for(j=0;j<sum/2;j++)
        {
            int iter=2;
            while(iter--)
            {
            int tmp=0, ind=-1;
            for(i=0;i<N;i++)
            {
                if(P[i]>=tmp)
                {
                    tmp=P[i];
                    ind=i;
                }
            }
            P[ind]--;
            printf("%c" , 'A'+ind);
            }
            printf(" ");
 
        }
        printf("\n");
 
    }
 
    return 0;
}

