#include<stdio.h>

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("large_output.txt","w",stdout);

    int cases;
    scanf("%d",&cases);
    for(int T = 1; T <= cases; T++)
    {
        int n;
        scanf("%d",&n);

        int ans = n;

        bool has[10] = {false};


        for(int i = 1; i <= 100; i++)
        {
            int cur = n*i;
            if( cur == 0 )
                has[0] = true;
            else
                while(cur>0)
                {
                    has[cur%10] = true;
                    cur /= 10;
                }

            bool check = true;
            for(int j = 0; j < 10; j++)
                check &= has[j];
            if(check)
            {
                ans = n*i;
                break;
            }
        }

        if( ans > 0 )
            printf("Case #%d: %d\n",T,ans);
        else
            printf("Case #%d: INSOMNIA\n",T);

    }
}

