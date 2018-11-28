#include <iostream>
using namespace std;
#include <cstdio>

int main()
{
    //freopen("A-large.in", "r", stdin);
   // freopen("outAL.txt", "w", stdout);
    int s[1010];
    char inp[1010];
    int smax;
    int numcase;
    scanf("%d", &numcase);
    for( int c = 1; c <= numcase; c++)
    {
        int ans = 0, pnum = 0;
        scanf("%d %s", &smax, inp);
        for( int i = 0; i <= smax; i++)
        {
            s[i] = inp[i] - '0';
        }
        pnum += s[0];

        for( int i = 1; i<=smax; i++)
        {
            if( pnum >= i)
                pnum += s[i];
            else
            {
                ans += i-pnum;
                pnum = i+s[i];
            }
        }


        printf("Case #%d: %d\n", c, ans);
    }
}
