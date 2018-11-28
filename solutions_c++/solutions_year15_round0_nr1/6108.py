#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int cases,caseno=0,n,i,d,cnt;
    char str[1002];

    scanf("%d", &cases);

    while(cases--)
    {
        scanf("%d %s", &n,str);
        cnt=0;
        d = str[0]-48;

        for(i=1; i<=n; i++)
        {
            if(d<i)
            {
                d++;
                cnt++;
            }
            d += str[i]-48;
        }

        printf("Case #%d: %d\n", ++caseno,cnt);
    }

    return 0;
}
