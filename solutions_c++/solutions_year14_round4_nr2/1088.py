#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int s1[1002], s2[1002], s3[1002];

bool check(int n)
{
    bool flag = false;
    for( int i = 1; i < n; i++ )
    {
        if( !flag && s1[i - 1] < s1[i] );
        else if( !flag ) flag = true;
        else if( flag && s1[i - 1] < s1[i] ) return false;
    }
    return true;
}

int main()
{
    int cases;
    scanf("%d", &cases);
    for( int tt = 1; tt <= cases; tt++ )
    {
        int n, ans = -1;
        scanf("%d", &n);
        for( int i = 0; i < n; i++ )
        {
            scanf("%d", &s1[i]);
            s2[i] = s1[i];
        }
        sort(s1, s1 + n);
        do
        {
            if( check(n) )
            {
                int cnt = 0;
                for( int i = 0; i < n; i++ ) s3[i] = s1[i];
                for( int i = 0; i < n; i++ )
                {
                    if( s3[i] != s2[i] )
                    {
                        int p;
                        for( p = i + 1; p < n; p++ )
                            if( s3[p] == s2[i] ) break;
                        for( int j = p; j > i; j-- )
                        {
                            swap(s3[j], s3[j - 1]);
                            cnt++;
                        }
                    }
                }
                if( ans == -1 ) ans = cnt;
                else ans = min(ans, cnt);
            }
        }
        while( next_permutation(s1, s1 + n) );
        printf("Case #%d: %d\n", tt, ans);
    }
    return 0;
}
