#include <bits/stdc++.h>

#define pi acos(-1)
#define mod 1000000007
typedef long long ll;

char str[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

using namespace std;

int main()
{
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );
    int tc, a[30], i, n;
    scanf("%d", &tc);
    for(i=1; i<=tc; i++)
    {
        scanf("%d", &n);
        int j, sum=0, mx, x;
        for(j=0; j<n; j++)
        {
            scanf("%d", &a[j]);
            sum += a[j];
        }
        printf("Case #%d: ", i);
        while(sum)
        {
            mx = 0;
            if(sum%2==0)
            {
                for(int pp=0; pp<2; pp++)
                {
                    mx = 0;
                    for(j=0; j<n; j++)
                    {
                        if(a[j]>mx)
                        {
                            mx = a[j];
                            x = j;
                        }
                    }
                    printf("%c", str[x]);
                    a[x]--;
                }
                sum-= 2;
                printf(" ");
            }
            else
            {
                for(j=0; j<n; j++)
                {
                    if(a[j]>mx)
                    {
                        mx = a[j];
                        x = j;
                    }
                }
                printf("%c ", str[x]);
                a[x]--;
                sum--;
            }
        }
        printf("\n");
    }
    return 0;
}
