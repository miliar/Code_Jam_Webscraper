#include<stdio.h>
#include<algorithm>
main()
{
    freopen("A-large.in","a+",stdin);
    freopen("output.txt","w+",stdout);
    int t;
    scanf("%d",&t);
    for(int l=1;l<=t;l++)
    {
        int n;
        scanf("%d",&n);
        int A[30];
        int sum = 0;
        bool E[30];
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&A[i]);
            sum = sum +A[i];
            E[i]=true;
        }
        printf("Case #%d: ",l);
        while(sum>0)
        {
            sum--;
            //printf("%d",sum);
            for(int i=1;i<=n;i++)
            {
                if(A[i]==0)
                    E[i]=false;
                else if(sum/2<=A[i] && E[i])
                {

                    printf("%c",'A'+i-1);
                    A[i]--;
                    break;
                }
                else if(i==n)
                {
                    for(int j=1;j<=n;j++)
                    {
                        if(E[j])
                        {
                            printf("%c",'A'+j-1);
                            A[j]--;
                            break;
                        }
                    }
                }

            }
            if(sum == 2)
            {
                printf(" ");
                continue;
            }
            sum--;
            for(int i=1;i<=n;i++)
            {
                if(A[i]==0)
                    E[i]=false;
                else if(sum/2<A[i] && E[i])
                {
                    printf("%c",'A'+i-1);
                    A[i]--;
                    break;
                }
                else if(i==n)
                {
                    for(int j=1;j<=n;j++)
                    {
                        if(E[j])
                        {
                            printf("%c",'A'+j-1);
                            A[j]--;
                            break;
                        }
                    }
                }
            }
            /*printf("S");
            for(int i=1;i<=n;i++)
                printf("%d ",A[i]);*/
            printf(" ");
        }
        printf("\n");
    }
}
