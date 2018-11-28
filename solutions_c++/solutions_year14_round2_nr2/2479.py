#include<bits/stdc++.h>

using namespace std;


int main()
{
    int t;
    long int ans;
    scanf("%d",&t);
    int t1;

    for(t1=1;t1<=t;t1++)
    {
        int a,b,k;
        scanf("%d",&a);
        scanf("%d",&b);
        scanf("%d",&k);
        int i,j;
        ans=0;
        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                if((i&j)<k)
                    ans++;

            }
        }

        printf("Case #%d: %ld\n",t1,ans);
    }
    return 0;
}
