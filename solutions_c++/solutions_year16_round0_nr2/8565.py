#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,i,j,len,p,m;
    scanf("%d",&t);
    char a[109];
    for( j=1; j<=t; j++)
    {
        p=0; m=0;
        scanf("%s",a);
        len = strlen(a);
        for( i=0; i<len; i++)
        {
            if (a[i] == '+')
                p++;
            else
                m++;
        }
        if( p == len)
        {
            printf("Case #%d: 0\n",j);
            continue;
        }
        if( m == len)
        {
            printf("Case #%d: 1\n",j);
            continue;
        }

        p=0; m=0;
        for( i=1; i<len; i++)
        {
            if( a[i-1] == '+' && a[i] == '-')
                m += 2;
        }
        for ( i=1; i<len; i++)
        {
            if ( a[i-1] == '-' && a[i] == '+')
            {
                 m++;
                 break;
            }
            if( a[i-1] == '+' && a[i] == '-')
            {
                break;
            }
        }

        printf("Case #%d: %d\n",j,m);
    }
    return 0;
}
