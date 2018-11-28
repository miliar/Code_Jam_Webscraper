#include <cstdio>

using namespace std;

int main()
{
    int t, c;
    scanf("%d",&t);

    for (c=1;c<=t;c++)
    {
        int n, nCopy, i, flag=0, j=0;
        scanf("%d",&n);

        

        int a[10];
        for (i=0;i<10;i++)
            a[i]=0;

        

        if (n==0)
            flag=1;
        while (flag!=1)
        {
            j++;
            nCopy = n * j;

            while(nCopy!=0)
            {
                a[nCopy%10]=1;
                nCopy=nCopy/10;
            }

            flag=1;

            for (i=0;i<10;i++)
            {
                if (a[i]!=1)
                {
                    flag=0;
                    break;
                }
            }
        }
        if (n!=0)
            printf("Case #%d: %d\n",c,n*j);
        else
            printf("Case #%d: INSOMNIA\n",c);

    }

    return 0;
}