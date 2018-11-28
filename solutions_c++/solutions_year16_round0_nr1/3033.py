#include<stdio.h>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output1.txt","w",stdout);

    int t;
    scanf("%d",&t);

    int k=1;

    while(t--)
    {
        int n;
        scanf("%d",&n);

        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",k++);
            continue;
        }
        int A[10];

        for(int i=0;i<10;i++)
            A[i]=0;

        int temp=n;
        int cou=1;

        while(1)
        {
            n=temp*cou;

            while(n)
            {
                A[n%10]=1;
                n=n/10;
            }

            int flag=1;

            for(int i=0;i<10;i++)
            {
                if(A[i]==0)
                    flag=0;
            }

            if(flag==1)
                break;

            cou++;
        }

        printf("Case #%d: %d\n",k++,temp*cou);

    }

}
