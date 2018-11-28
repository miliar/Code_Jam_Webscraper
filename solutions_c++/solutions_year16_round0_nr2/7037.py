#include <stdio.h>
#include <string.h>
char st[200];
int main()
{
    int t;
   // freopen("B-large.in","r",stdin);
    //freopen("B-small-attempt0.out","w",stdout);
    scanf("%d",&t);
    for (int cas = 1 ; cas <= t ; cas ++ )
    {
        scanf("%s",st);
        int len = strlen (st);
        int temp = len - 1;
        int res = 0;
        int flag = 0 ;
        for (int i = len - 1 ; i >= 0 ;  i-- )
        {
            if ( st[i] == '-')
            {
                flag = 1;
                //continue;
            }
            if ( (st[i] == '+' || i == 0) && flag == 1)
            {
                for (int j = 0 ; j <= i ; j++ )
                {
                    if (st[j] == '-')
                    {
                        st[j] = '+';
                    }
                    else 
                    {
                        st[j] = '-';
                    }
                }
                i++;
                res ++;
                flag = 0;
            }
        }
        printf("Case #%d: %d\n",cas,res);
    }
    return 0;
}