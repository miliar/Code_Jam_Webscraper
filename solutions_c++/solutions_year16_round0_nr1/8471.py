#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("A-large.txt","r",stdin);
    //freopen("out1.txt","w",stdout);

    int t,n,cnt,i,temp,d,a[10],ans,j,temp1;
    scanf("%d",&t);
    for(j=1; j<=t; j++)
    {
        scanf("%d",&n);
        cnt = 10;
        temp = n;
        ans = 0;
        if( n == 0)
        {
            printf("Case #%d: INSOMNIA\n",j);
            continue;
        }
        for(i=0;i<10;i++)
            a[i] = 0;

        while(cnt != 0)
        {
            temp = ans + n ;
            ans = temp;
            while(temp>0)
            {
                d = temp%10;
                if(a[d]==0)
                    {
                        cnt--;
                        a[d] = 1;
                    }
                temp = temp/10;
            }

        }
        printf("Case #%d: %d\n",j,ans);
    }
    return 0;
}
