#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
    freopen("A-large.out", "w", stdout);

    int T;
    scanf("%d", &T);

    int test = 1;
    while( test <= T )
    {
        int s_max, ans = 0;
        scanf("%d", &s_max);
        char S[1010];
        scanf("%s", S);
        int people = 0;
        for( int i = 0; i < s_max+1; i++ )
        {
            if( S[i] != '0' )
            {
                int need = i-people;
                if( need > 0 )
                {
                    ans += need;
                    people += need;
                }
                people += (S[i]-'0');
            }
        }
        printf("Case #%d: %d\n", test, ans);
        test++;
    }

    return 0;
}
